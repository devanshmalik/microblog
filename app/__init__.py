from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.add_url_rule('/', endpoint='index')

from app import routes

# def create_app(test_config=None):
