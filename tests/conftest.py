import pytest
# from flask import Flask
from app import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        yield client


@pytest.fixture
def db():
    from app import app, db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

    yield db

    # Teardown
    db.session.remove()
    db.drop_all()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='dev', password='pass'):
        return self._client.post(
            '/login', data=dict(
                username=username,
                password=password
            )
        )


@pytest.fixture
def auth(client):
    return AuthActions(client)