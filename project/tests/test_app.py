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


def test_read_users(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == { 'users':[
        {
        'username': 'testeuser',
        'email': 'test@test.com',
        'id': 1
        }]
    }
    ...
