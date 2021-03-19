# fake-real-news
Classifier for fake news and real news by [HUANG, Sheng](https://github.com/vicw0ng-hk) & [LI, Yik Wai](https://github.com/liyikwai).

- Group project for [COMP3359 Artificial Intelligence Applications](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2020/comp3359.html, "COMP3359 Artificial Intelligence Applications [Section 2A, 2020]") @ [HKU](https://hku.hk, "The University of Hong Kong")

> "If you tell a lie big enough and keep repeating it, people will eventually come to believe it. The lie can be maintained only for such time as the State can shield the people from the political, economic and/or military consequences of the lie. It thus becomes vitally important for the State to use all of its powers to repress dissent, for the truth is the mortal enemy of the lie, and thus by extension, the truth is the greatest enemy of the State."

[Joseph Goebbels](https://en.wikipedia.org/wiki/Joseph_Goebbels), [Reich Minister of Propaganda](https://en.wikipedia.org/wiki/Reich_Ministry_of_Public_Enlightenment_and_Propaganda), [Nazi Germany](https://en.wikipedia.org/wiki/Nazi_Germany)

### Project Proposal
[pdf](reports/proposal.pdf)

### Data Engineering
[notebook](notebooks/data_processing.ipynb)

Used the [FakeNewCorpus](https://github.com/several27/FakeNewsCorpus) by [@serveral27](https://github.com/several27). 

Size of Original Corpus is 29 GB, after deleting certain columns, it came to 25 GB. Due to the large size of the corpus, [Dask](https://dask.org/), instead of [Pandas](https://pandas.pydata.org/), is used to process the data for its [out-of-core](https://en.wikipedia.org/wiki/External_memory_algorithm) characteristics.

### Progress
We are in the phase of developing an interim prototype. See [Projects](https://github.com/vicw0ng-hk/fake-real-news/projects/1).

There will be two phases of development during the second semester of academic year 2020-21. More plan in proposal. 
