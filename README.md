# fake-real-news

![python](https://img.shields.io/badge/python-v3.8.6-yellow) ![fastai](https://img.shields.io/badge/fastai-v2.3.0-blue) ![flask](https://img.shields.io/badge/flask-v1.1.2-lightgrey)

A news classifier in the fight against disinformation by [HUANG, Sheng](https://github.com/vicw0ng-hk) & [LI, Yik Wai](https://github.com/liyikwai). :handshake:

- Group project for [COMP3359 Artificial Intelligence Applications](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2020/comp3359.html "COMP3359 Artificial Intelligence Applications [Section 2A, 2020]") @ [HKU](https://hku.hk "The University of Hong Kong") :school:

> :label: "If you tell a lie big enough and keep repeating it, people will eventually come to believe it. The lie can be maintained only for such time as the State can shield the people from the political, economic and/or military consequences of the lie. It thus becomes vitally important for the State to use all of its powers to repress dissent, for the truth is the mortal enemy of the lie, and thus by extension, the truth is the greatest enemy of the State."

[Joseph Goebbels](https://en.wikipedia.org/wiki/Joseph_Goebbels), [Reich Minister of Propaganda](https://en.wikipedia.org/wiki/Reich_Ministry_of_Public_Enlightenment_and_Propaganda), [Nazi Germany](https://en.wikipedia.org/wiki/Nazi_Germany)

### Mission :anchor:

What is our relationship with the truth (or, the reality)? :confused: That is a philosophical question. :nerd_face:

Great minds struggle with this question. 

[![Young Sheldon Cooper](https://img.youtube.com/vi/nO88009AJ80/0.jpg)](https://www.youtube.com/watch?v=nO88009AJ80)

Young Sheldon Cooper struggled with this problem and wanted to switch major to philosophy. But in the end, he returned to science when he realized physics theories could explain more patterns in nature. 

[![Young Sheldon Cooper 2](https://img.youtube.com/vi/Bx8HXPfc9LE/0.jpg)](https://www.youtube.com/watch?v=Bx8HXPfc9LE&t=140s)

As fake news spreads wildly today, we have been in a similar crisis. :scream: With so much information, how can you tell what is real and what is not? :fearful: Especially, with the cost of reading a news article so low and the cost of verifying the facts so high, how can anyone make judgments on the authenticity of the news content? :frowning_face: Some may say nothing is real and lead a life without any thoughts on the world. :tired_face: Some may say they trust authoritative sources. But how do you define authoritative source? Is everything put out by these authoritative sources guaranteed to be true? :confounded: Can we find patterns on these articles, also taking into account its sources, and then make a better judgment, or a more educated guess? :roll_eyes:

Indeed we CAN find linguistic patterns in news articles. :smiley: These patterns may well have correlations to the realness or fakeness of these articles. But it's not that simple. :upside_down_face: Remember that news media have biases. For example, in the United States, conservative media such as *Fox News* and liberal news media such as *MSNBC* and *CNN* have different styles when reporting news :cold_face:, but that doesn't automatically mean that one style is equal to fake news reporting. (Check out [Media Biad Ratings](https://www.allsides.com/media-bias/media-bias-ratings)) To avoid such biases when training our model, we recognize news articles that cannot be easily categorized as real or fake, such as pieces that are strong in opinions. (Check out the types we have [here](METHOD.md#types) :point_left:)

We concede that this approach is still flawed, which will be discussed in [Limitations](#limitations-triangular_ruler). However, it can give us somewhat of a reference when we are judging the authenticity of an article, as we have given explicit descriptions on how we categorize the articles. Still, users should keep in mind that we are not the arbitor of truth and that the model cannot replace the work of a professional fact checker - it cannot visit the places where events happened; it cannot interview people involved in the stories; it cannot know the intention of the publishers when they put out the story.

THERE IS NO ALGORITHM FOR TRUTH. 

[![Tom Scott](https://img.youtube.com/vi/leX541Dr2rU/0.jpg)](https://www.youtube.com/watch?v=leX541Dr2rU&t=3377s)

### Reports :books:

- Proposal :bookmark_tabs: [pdf](reports/proposal.pdf)
- Interim Report :bookmark_tabs: [pdf](reports/prototype.pdf)

### Running :running_man: :running_woman:

It's highly :top: recommended to run the app on a Unix-like system (GNU/Linux, macOS, ...). :bangbang: Using Windows may cause some issues when installing dependencies. :cry:

#### 0. Cloning the repository :arrow_down:

```bash
git clone https://github.com/vicw0ng-hk/fake-real-news.git
```

Or, clone through SSH for better security. :closed_lock_with_key:

```bash
git clone git@github.com:vicw0ng-hk/fake-real-news.git
```

Or, clone with [GitHub CLI](https://cli.github.com/) :octocat:

```bash
gh repo clone vicw0ng-hk/fake-real-news
```

Due to the large size of our model, it is stored with [Git LFS](https://docs.github.com/en/github/managing-large-files/versioning-large-files), and because of [GitHub's bandwidth limit](https://docs.github.com/en/github/managing-large-files/about-storage-and-bandwidth-usage) :construction:, please use this [link](https://drive.google.com/file/d/1iKYjwwRu4ihJApT1ZoZosCAPXkhX9qAk/view?usp=sharing) :point_left: to download [`app/model/model.pkl`](app/model/model.pkl) and replace the file in the cloned directory. 

#### 1. Installing environment :palm_tree:

This may be different depending on the virtualization technology you are using :shrug:, but generally do
```bash
cd app/
pip3 install -r requirements.txt
```

#### 2. Run the app! :bullettrain_front:

```bash
python3 app.py
```

### Methodology :hammer_and_wrench:

Check out the [Methodology](METHOD.md) document.

### Functionalities :gear:

Check out the [Functionalities](FUNCTION.md) document. 

### Limitations :triangular_ruler:

### Terms and Conditions :scroll:

In addition to the restrictions of [GNU Affero General Public License v3.0](LICENSE) of this repo, you also agree to the following terms and conditions:

```
YOUR USE OF THIS WEB APP CONSTITUTES YOUR AGREEMENT 
TO BE BOUND BY THESE TERMS AND CONDITIONS OF USE.

1. The classification of the text you submit to this 
web app is in no way legal recognition. The web app 
and/or its authors bear no legal responsiblities for 
its result. If you choose to publish the result, the 
web app and/or its authors shall not bear any legal 
consequences relating to this action.  
2. You shall be liable for the legal reponsibilities 
of the copyright of the text you submit to this web 
app. You shall gain the right to copy the text before 
you submit it to the web app. 
3. This web app shall not be used by any political 
organization and/or any entity, partially or entirely, 
directly or indirectly, funded and/or controlled by a 
political organization in any jurisdiction. 
4. In case of any discrepency with any other license, 
terms or conditions associated with this web app 
and/or its repository, this agreement shall prevail. 
```
