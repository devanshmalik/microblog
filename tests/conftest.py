import pytest
# from flask import Flask
from microblog import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        yield client

# from microblog.forms import LoginForm
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/login', data=dict(
                username=username,
                password=password
            )
        )


@pytest.fixture
def auth(client):
    return AuthActions(client)