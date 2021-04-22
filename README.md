# fake-real-news

Classifier for fake news and real news by [HUANG, Sheng](https://github.com/vicw0ng-hk) & [LI, Yik Wai](https://github.com/liyikwai). :handshake:

- Group project for [COMP3359 Artificial Intelligence Applications](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2020/comp3359.html, "COMP3359 Artificial Intelligence Applications [Section 2A, 2020]") @ [HKU](https://hku.hk, "The University of Hong Kong") :school:

> :label: "If you tell a lie big enough and keep repeating it, people will eventually come to believe it. The lie can be maintained only for such time as the State can shield the people from the political, economic and/or military consequences of the lie. It thus becomes vitally important for the State to use all of its powers to repress dissent, for the truth is the mortal enemy of the lie, and thus by extension, the truth is the greatest enemy of the State."

[Joseph Goebbels](https://en.wikipedia.org/wiki/Joseph_Goebbels), [Reich Minister of Propaganda](https://en.wikipedia.org/wiki/Reich_Ministry_of_Public_Enlightenment_and_Propaganda), [Nazi Germany](https://en.wikipedia.org/wiki/Nazi_Germany)

### Mission :anchor:

THERE IS NO ALGORITHM FOR TRUTH. 

[![YouTube](https://img.youtube.com/vi/leX541Dr2rU/0.jpg)](https://www.youtube.com/watch?v=leX541Dr2rU&t=3377s)



### Reports :books:

- Proposal :bookmark_tabs: [pdf](reports/proposal.pdf)
- Interim Report :bookmark_tabs: [pdf](reports/prototype.pdf)

### Running :running_man: :running_woman:

It's highly :top: recommended to run the app on a Unix-like system (Linux, macOS, ...). :bangbang: Using Windows may cause some issues when installing dependencies. :cry:

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

Due to the large size of our model, it is stored with [Git LFS](https://docs.github.com/en/github/managing-large-files/versioning-large-files), and because of [GitHub's bandwidth limit](https://docs.github.com/en/github/managing-large-files/about-storage-and-bandwidth-usage) :construction:, please use this [link](https://drive.google.com/file/d/1iKYjwwRu4ihJApT1ZoZosCAPXkhX9qAk/view?usp=sharing) :point_left: to download [`model.pkl`](app/model/model.pkl) and replace the file in the cloned directory. 

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

### Methodology :gear:

Check out the [Methodology](METHOD.md) document.

### Functionalities :gear:

Check out the [Functionalities](FUNCTION.md) document. 

### Limitations :triangular_ruler:

### Terms and Conditions :scroll:

In addition to the restrictions of [GNU Affero General Public License v3.0](LICENSE) of this repo, you also agree to the following terms and conditions:

```
YOUR USE OF THIS WEB APP CONSTITUTES YOUR AGREEMENT TO BE BOUND BY THESE TERMS AND CONDITIONS OF USE.

1. The classification of the text you submit to this web app is in no way legal recognition. The web 
app and/or its authors bear no legal responsiblities for its result. If you choose to publish the 
result, the web app and/or its authors shall not bear any legal consequences relating to this action.  
2. You shall be liable for the legal reponsibilities of the copyright of the text you submit to this 
web app. You shall gain the right to copy the text before you submit it to the web app. 
3. This web app shall not be used by any political party and/or any entity, partially or entirely, 
funded and/or controlled by a political party in any jurisdiction. 
4. In case of any discrepency with any other license, terms or conditions associated with this web app 
and/or its repository, this agreement shall prevail. 
```
