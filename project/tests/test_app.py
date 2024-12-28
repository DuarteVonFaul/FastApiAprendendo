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


def test_update_user(client):

    response = client.put('/users/1',
        json={
            'username': 'testeuser',
            'password': 'pass123',
            'email': 'user@exemple.com',
        },)

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'username': 'testeuser',
        'email': 'user@exemple.com',
        'id': 1
        }
    ...

def test_update_user_not_found_error(client):

    response = client.put('/users/2',
        json={
            'username': 'testeuser',
            'password': 'pass123',
            'email': 'user@exemple.com',
        },)

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {
        'detail': 'USER NOT FOUND'
        }

def test_user_delete(client):

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'message':'User deleted'
        }


def test_user_delete_not_found_error(client):

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {
        'detail': 'USER NOT FOUND'
        }