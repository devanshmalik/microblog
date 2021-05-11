from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import routes

# def create_app(test_config=None):
