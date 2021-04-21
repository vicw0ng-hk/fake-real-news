from flask import Flask, render_template, request, redirect
from flask_wtf.csrf import CSRFProtect
from fastai.text.all import load_learner
import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

learn = load_learner(app.root_path + '/model/model.pkl')
vocab = ['bias', 'clickbait', 'conspiracy', 'fake', 'hate', 
         'junksci', 'political', 'reliable', 'satire', 'unreliable']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/', methods=['POST'])
def result():
    url = request.form['url']
    title = request.form['title']
    authors = request.form['authors']
    content = request.form['content']
    text = ' | '.join([url, title, authors, content])
    res = learn.predict(text)[2].tolist()
    prob = {vocab[i]: res[i] for i in range(10)}
    ranking = sorted(prob.items(), key=lambda x: x[1], reverse=True)
    context = {'url': url, 'title': title, 'authors': authors, 'text': text, 'pred': ranking}
    return render_template('result.html', context=context)

@app.route('/hidden/', methods=['POST'])
def hidden():
    print(request.form)
    return 'Feedback recorded!'

if __name__ == "__main__":
    app.run(debug=True)