from http import HTTPStatus

def test_create_user(client):

    # UserSchema
    response = client.post(
        '/users/',
        json={
            'username': 'testeuser',
            'password': 'pass123',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'testeuser',
        'email': 'test@test.com',
        'id': 1,
    }
    ...
