from fastapi import FastAPI
from http import HTTPStatus
from api.schemas import Message, UserSChema, UserPublic

app = FastAPI()


@app.get('/', 
         status_code=HTTPStatus.OK, 
         response_model=Message)
def read_root(): 
    return {'message': 'Hello World'}


@app.post('/users/', 
          status_code=HTTPStatus.CREATED, 
          response_model= UserPublic)
def create_user(user:UserSChema):
    return user



