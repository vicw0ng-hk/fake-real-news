# Methodology :monocle_face:

This project comprises of two :v: major parts: [Model](#model) and [Web App](#web-app). 

We built both parts on GNU/Linux, with model trained on the [HKU CS GPU Farm](https://www.cs.hku.hk/gpu-farm/home) and web app developed on [Pop!_OS 20.10](https://pop.system76.com/). :blush:

### Model

#### Data

Undoubtedly, we need data to train our model. Thanks to  [@serveral27](https://github.com/several27) :pray:, we have a [FakeNewCorpus](https://github.com/several27/FakeNewsCorpus). :smile:

Size of Original Corpus is 29 GB :astonished:, but we don't need all the data.

In the first phase of the project, we deleted certain not-so-useful columns and trimmed the data down to 25 GB. :cry:

```python
import dask.dataframe as dd
df = dd.read_csv('news_cleaned_2018_02_13.csv', usecols=['url', 'title', 'authors', 'content', 'type'], 
                 engine='python', error_bad_lines=False)
df.to_csv('fake.csv', index=False)
```

Due to the large size of the corpus, [Dask](https://dask.org/), instead of [Pandas](https://pandas.pydata.org/), is used to process the inital data for its [out-of-core](https://en.wikipedia.org/wiki/External_memory_algorithm) characteristics. :+1: We saved the data into hundreds of smaller files. 

In the second phase of the project, we concatenated some of the columns together as they can all be handled by a language model. :wink: We also deleted rows without a valid type and content and the size came down to 22 GB. 

```python
df = df.dropna(subset=['type', 'content'])
label = ['fake', 'satire', 'bias', 'conspiracy', 'junksci', 'hate', 'clickbait', 'unreliable', 'political', 'reliable']

for i in range(459):
    df = pd.read_csv('fake.csv/{0:03}.part'.format(i), engine='python', error_bad_lines=False, keep_default_na=False)
    df = df[df['type'].isin(label)]
    df['content'] = df['url'].str.cat(df[['title', 'authors', 'content']], sep=' | ')
    df = df.drop(['url', 'title', 'authors'], axis=1)
    df.to_csv('fake1.csv/{0:03}.part'.format(i), index=False)
```

#### Language Model

To build a text classifier model we must first build a language model. :speech_balloon:

[fastai](https://www.fast.ai/) handles tokenization and numericalization automatically when `TextBlock` is passed to `DataBlock`. All of the arguments that can be passed to `Tokenizer` and `Numericalize` can also be passed to `TextBlock`. :+1:

```python
from fastai.text.all import *

dls_lm = DataBlock(blocks=TextBlock.from_df('content', is_lm=True),
                   get_x=ColReader('text'), splitter=RandomSplitter(0.1)
                  ).dataloaders(df, bs=32, seq_len=80)
```

The reason that `TextBlock` is special is that setting up the numericalizer’s vocab can take a long time (we have to read and tokenize every document to get the vocab). 

fastai has some optimization on this: :point_down:

> - It saves the tokenized documents in a temporary folder, so it doesn’t have to tokenize them more than once.
> - It runs multiple tokenization processes in parallel, to take advantage of your computer’s CPUs.

Now that we have handled our data, let's fine-tune the pretrained language model. 

To convert the integer word indices into activations that we can use for our neural network, we will use [embeddings](https://en.wikipedia.org/wiki/Word_embedding). Then we’ll feed those embeddings into a [recurrent neural network (RNN)](https://en.wikipedia.org/wiki/Recurrent_neural_network), using an architecture called [AWD-LSTM](https://docs.fast.ai/text.models.awdlstm.html). (Check out [Smerity et al.](https://arxiv.org/pdf/1708.02182.pdf)) :eyes:

the embeddings in the pretrained model are merged with random embeddings added for words that weren’t in the pretraining vocabulary. This is handled automatically inside [`language_model_learner`](https://docs.fast.ai/text.learner.html#language_model_learner):

```python
learn = language_model_learner(
        dls_lm, AWD_LSTM, drop_mult=0.3,
        metrics=[accuracy, Perplexity()]).to_fp16()
```

The loss function used by default is cross-entropy loss, since we essentially have a classification problem. The perplexity metric used here is often used in NLP for language models: it is the exponential of the loss (`torch.exp(cross_entropy)`). We also include the accuracy metric to see how many times our model is right when trying to predict the next word, since cross entropy is both hard to interpret and tells us more about the model’s confidence than its accuracy.

Then we can start to use `learn.fit_one_cycle()` to train our language model (we also uesd `learn.lr_find()` to find a good learning rate). After each time we trained, we would use `learn.save()` to save a copy of the state of our model as it takes quite a while to train an epoch. When come back to training after leaving for something else, we can use `learn = learn.load()` to load the state back, unfreeze the state by `learn.unfreeze()` and continue training. We would substitude new data using `learn.dls = dls_lm_new` as the RAM limits on GPU Farm does not allow us to use all data in one go. The accuracy of the language model came to upper 30s to 40s percent.

After training language model, we saved the model (excluding the final layer, of course) using `learn.save_encoder('finetuned')`. :fist:

#### Classifier Model

This is similar to what we have done above :arrow_up:, with dataloaders as:

```python
dls_clas = DataBlock(blocks=(TextBlock.from_df('content'),CategoryBlock),
                     get_x=ColReader('text'), get_y=ColReader('type'), 
                     splitter=RandomSplitter(0.1)
                    ).dataloaders(df, bs=32, seq_len=80)
```

The major difference is that `is_lm` is gone because this is no longer training for a language model, and there is an additional [`CategoryBlock`](https://docs.fast.ai/data.block.html#CategoryBlock). 

We can now create a model using [`text_classifier_learner`](https://docs.fast.ai/text.learner.html#text_classifier_learner) to classify our texts:

```python
learn = text_classifier_learner(dls_clas, AWD_LSTM, drop_mult=0.5,
                                metrics=accuracy).to_fp16()
```

And then load the encoder we saved earlier:

```python
learn = learn.load_encoder('finetuned')
```

Then we start training using `learn.fit_one_cycle()`. We also used `learn.freeze_to()` to freeze some parameters and then train the model, after which we use `learn.unfreeze()` to unfreeze the parameters and then train for a few more epochs. The accuracy came to about 90% for the validation set of the data we used for training. However, since the RAM limits we could not use most of our data and the accuracy on some other data may vary from 30% - 98% (check out one [testing example](test.ipynb)). :slightly_smiling_face: This doesn't seem top-notch, but it's acceptable since news articles generally fit into multiple categories and yet we only have a single-label dataset. More on this in our discussion of limitations. :thinking:

### Web app

We used [Flask](https://flask.palletsprojects.com/en/1.1.x/), a minimal Python web framework. :hugs: We love its simplicity. And you can see this by the only main part of our server side :point_right: [app.py](app/app.py). 

#### Some Highlights :camera:

- Since Flask supports [Jinja](https://jinja.palletsprojects.com/en/2.11.x/), we ued it for our [HTML templates](app/templates), adding a dynamic component to static templates.
- We used [Bootstrap](https://getbootstrap.com/) to customize the look and feel of our web pages. We also included JavaScript and [jQuery](https://jquery.com/) to implement certain styles.  
- We implemented CSRF Protection ([CSRFProtec](https://flask-wtf.readthedocs.io/en/stable/api.html#flask_wtf.csrf.CSRFProtect) from [Flask-WTF](https://flask-wtf.readthedocs.io/)) in POST form submissions. 
- We used [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) to interact with [SQLite3](https://www.sqlite.org/index.html), which stores use feedback and we can us the feedback to better train our model. Mode on this in our discussion of functionalities. 
- We used [`load_learner`](https://docs.fast.ai/learner.html#load_learner) from fastai to load the trained model and then use the model to get predictions on our input. 
