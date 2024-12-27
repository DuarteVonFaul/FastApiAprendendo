from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSChema(BaseModel):
    username:str
    password:str
    email:EmailStr

class UserDB(UserSChema):
    id: int
    ...

class UserPublic(BaseModel):
    id: int
    username:str
    email:EmailStr