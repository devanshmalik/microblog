from flask import render_template, redirect, url_for, flash
from microblog import app
from microblog.forms import LoginForm


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


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data)
        )
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)