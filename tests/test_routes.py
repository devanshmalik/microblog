from flask import url_for, request
import pytest


def test_index(client):
    response = client.get('/index')
    assert response.status_code == 200
    assert b'Home - Microblog' in response.data
    assert b'Login' in response.data

    assert b'<a href="/index">Home</a>' in response.data
    assert b'<a href="/login">Login</a>' in response.data


def test_login_successful(client, auth):
    assert client.get('/login').status_code == 200
    response = auth.login(username='admin', password='password')
    assert response.headers['Location'] == 'http://localhost/index'

    response = client.get('/index')
    assert b'Login requested for user admin, remember_me=False' in response.data


@pytest.mark.parametrize(
    ('username', 'password', 'message'),
    (
        ('', '', b'[This field is required.]'),
        ('test', '', b'[This field is required.]'),
        ('', 'test', b'[This field is required.]'),
    )
)
def test_login_validation(auth, username, password, message):
    response = auth.login(username, password)
    # print(response.data)
    assert message in response.data