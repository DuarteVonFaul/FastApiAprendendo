import pytest
from fastapi.testclient import TestClient
from api.app import app
from api.database import DataBase




#Sempre que eu tiver um metodo de teste que recebe um client
# ele recebera essa função como parametro
@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():

    database = DataBase('sqlite:///test_database.db')
    database.migration()
    return database.mySession()
    