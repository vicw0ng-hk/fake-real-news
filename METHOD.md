# Methodology :monocle_face:

This project comprises of two :v: major parts: [Model](#model) and [Web App](#web-app). 

### Model

Undoubtedly, we need data to train our model. :blush: Thanks to  [@serveral27](https://github.com/several27) :pray:, we have a [FakeNewCorpus](https://github.com/several27/FakeNewsCorpus). :smile:

Size of Original Corpus is 29 GB :astonished:, but we don't need all columns.

In the first phase of the project, we deleted certain not-so-useful columns and trimmed the data down to 25 GB. :cry:

```python
import dask.dataframe as dd
df = dd.read_csv('news_cleaned_2018_02_13.csv', usecols=['url', 'title', 'authors', 'content', 'type'], 
                 engine='python', error_bad_lines=False)
df.to_csv('fake.csv', index=False)
```

Due to the large size of the corpus, [Dask](https://dask.org/), instead of [Pandas](https://pandas.pydata.org/), is used to process the inital data for its [out-of-core](https://en.wikipedia.org/wiki/External_memory_algorithm) characteristics. :+1: We saved the data into hundreds of smaller files. 

In the second phase of the project, we concatenated some of the columns together as they can all be handled by a language model. :wink: We also deleted rows without a valid type and content. 

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



### Web app
