from flask import Flask, render_template, request, redirect
from flask_wtf.csrf import CSRFProtect
import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/', methods=['POST'])
def result():
    url = request.form['url']
    title = request.form['title']
    authors = request.form['authors']
    content = request.form['content']
    context = {'url': url, 'title': title, 'authors': authors, 'content': content}
    return render_template('result.html', context=context)

if __name__ == "__main__":
    app.run(debug=True)