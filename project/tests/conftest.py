import pytest
from fastapi.testclient import TestClient
from api.app import app


#Sempre que eu tiver um metodo de teste que recebe um client
# ele recebera essa função como parametro
@pytest.fixture()
def client():
    return TestClient(app)