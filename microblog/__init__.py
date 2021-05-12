from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from microblog import routes

# def create_app(test_config=None):
