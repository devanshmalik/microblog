from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    user = {'username': 'Dev'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Wowghan'
        },
        {
            'author': {'username': 'Renuka'},
            'body': 'Support the artists!'
        }
    ]
    return render_template('index.html', title=title, user=user, posts=posts)