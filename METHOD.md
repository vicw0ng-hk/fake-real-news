# Methodology :monocle_face:

This project comprises of two :v: major parts: [Model](#model) and [Web App](#web-app). 

We built both parts on GNU/Linux, with model trained on the [HKU CS GPU Farm](https://www.cs.hku.hk/gpu-farm/home) and web app developed on [Pop!_OS 20.10](https://pop.system76.com/). :blush:

### Model

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

To build a text classifier model we must first build a language model. :speech_balloon:

[fastai](https://www.fast.ai/) handles tokenization and numericalization automatically when `TextBlock` is passed to `DataBlock`. All of the arguments that can be passed to `Tokenizer` and `Numericalize` can also be passed to `TextBlock`.

```python
dls_lm = DataBlock(blocks=TextBlock.from_df('content', is_lm=True),
                   get_x=ColReader('text'), splitter=RandomSplitter(0.1)
                  ).dataloaders(df, bs=32, seq_len=80)
```

The reason that `TextBlock` is special is that setting up the numericalizer’s vocab can take a long time (we have to read and tokenize every document to get the vocab). 

fastai has some optimization on this:

> - It saves the tokenized documents in a temporary folder, so it doesn’t have to tokenize them more than once.
> - It runs multiple tokenization processes in parallel, to take advantage of your computer’s CPUs.

Now that we have handled our data, let's fine-tune the pretrained language model. 

### Web app
