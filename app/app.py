from flask import Flask, render_template, request, redirect
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from fastai.text.all import load_learner
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    text = db.Column('content', db.Text)

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __repr__(self):
        return self.type

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
    context = {'url': url, 'title': title, 'authors': authors, 
               'text': text, 'pred': ranking}
    return render_template('result.html', context=context)

@app.route('/hidden/', methods=['POST'])
def hidden():
    fb = Feedback(request.form['type'], request.form['text'])
    db.session.add(fb)
    db.session.commit()
    return 'Feedback recorded!'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
