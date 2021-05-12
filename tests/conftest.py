import pytest
# from flask import Flask
from microblog import app

# @pytest.fixture
# def microblog():
#     microblog = Flask(__name__)
#     yield microblog


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client
