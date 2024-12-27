from http import HTTPStatus

from fastapi.testclient import TestClient
from api.app import app


def test_create_user():
    client = TestClient(app)

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
