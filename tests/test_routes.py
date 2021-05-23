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
#     response = auth.login(username='admin', password='password')
#     assert response.headers['Location'] == 'http://localhost/index'
#
#     response = client.get('/index')
#     assert b'Login requested for user admin, remember_me=False' in response.data
#
#
# @pytest.mark.parametrize(
#     ('username', 'password', 'message'),
#     (
#         ('', '', b'[This field is required.]'),
#         ('test', '', b'[This field is required.]'),
#         ('', 'test', b'[This field is required.]'),
#     )
# )
# def test_login_validation(auth, username, password, message):
#     response = auth.login(username, password)
#     # print(response.data)
#     assert message in response.data