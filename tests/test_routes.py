from flask import url_for, request
import pytest


def test_index_without_login(client):
    response = client.get('/index')
    assert response.headers['Location'] == 'http://localhost/login?next=%2Findex'

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes'])
        assert 'Please log in to access this page.' in flash_message['message']


# def test_login_successful(client, auth):
#     assert client.get('/login').status_code == 200
#     response = auth.login(username='dev', password='pass')
#     assert response.headers['Location'] == 'http://localhost/index'
#
#     response = client.get('/index')
#     assert response.status_code == 200
#     assert b'<title>Home - Microblog</title>' in response.data
#
#     response = client.get('/login')
#     assert response.headers['Location'] == 'http://localhost/index'


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
    assert message in response.data