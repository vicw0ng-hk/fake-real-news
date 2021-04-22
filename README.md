# fake-real-news
Classifier for fake news and real news by [HUANG, Sheng](https://github.com/vicw0ng-hk) & [LI, Yik Wai](https://github.com/liyikwai). :handshake:

- Group project for [COMP3359 Artificial Intelligence Applications](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2020/comp3359.html, "COMP3359 Artificial Intelligence Applications [Section 2A, 2020]") @ [HKU](https://hku.hk, "The University of Hong Kong") :school:

> :label: "If you tell a lie big enough and keep repeating it, people will eventually come to believe it. The lie can be maintained only for such time as the State can shield the people from the political, economic and/or military consequences of the lie. It thus becomes vitally important for the State to use all of its powers to repress dissent, for the truth is the mortal enemy of the lie, and thus by extension, the truth is the greatest enemy of the State."

[Joseph Goebbels](https://en.wikipedia.org/wiki/Joseph_Goebbels), [Reich Minister of Propaganda](https://en.wikipedia.org/wiki/Reich_Ministry_of_Public_Enlightenment_and_Propaganda), [Nazi Germany](https://en.wikipedia.org/wiki/Nazi_Germany)

### Reports :books:
- Proposal :bookmark_tabs: [pdf](reports/proposal.pdf)
- Interim Report :bookmark_tabs: [pdf](reports/prototype.pdf)

### Running :running_man: :running_woman:
It's highly recommended to run the app on a POSIX system. :bangbang: Using Windows may cause some issues when installing dependencies. :cry:
#### 1. Installing environment :palm_tree:
This may be different depending on the virtualization technology you are using :shrug:, but generally do
```bash
cd app/
pip install -r requirements.txt
```

#### 2. Run the app! :bullettrain_front:
```bash
python app.py
```

### Methodology :gear:

Used the [FakeNewCorpus](https://github.com/several27/FakeNewsCorpus) by [@serveral27](https://github.com/several27). :pray: 

Size of Original Corpus is 29 GB :astonished:, after deleting certain columns, it came to 25 GB :cry:. Due to the large size of the corpus, [Dask](https://dask.org/), instead of [Pandas](https://pandas.pydata.org/), is used to process the data for its [out-of-core](https://en.wikipedia.org/wiki/External_memory_algorithm) characteristics. :+1:
