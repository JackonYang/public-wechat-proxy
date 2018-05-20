

def test_auth_fake(client):
    response = client.get('/listener/?echostr=123')

    assert response.status_code == 200

    data = response.content

    assert data == '123'
