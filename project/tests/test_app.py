from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from api.app import app

#Sempre que eu tiver um metodo de teste que recebe um client
# ele recebera essa função como parametro
@pytest.fixture()
def client():
    return TestClient(app)

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
