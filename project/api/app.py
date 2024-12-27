from fastapi import FastAPI
from http import HTTPStatus
from api.schemas import (
    Message, 
    UserSChema, 
    UserPublic,
    UserDB
    )

app = FastAPI()

database = []

@app.get('/', 
         status_code=HTTPStatus.OK, 
         response_model=Message)
def read_root(): 
    return {'message': 'Hello World'}


@app.post('/users/', 
          status_code=HTTPStatus.CREATED, 
          response_model= UserPublic)
def create_user(user:UserSChema):

    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id



