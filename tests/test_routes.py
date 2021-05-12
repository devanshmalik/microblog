

def test_index(client):
    response = client.get('/index')
    assert response.status_code == 200
    assert b'Home - Microblog' in response.data
    assert b'Login' in response.data
    assert b'<a href="/index">Home</a>' in response.data
