from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSChema(BaseModel):
    username:str
    password:str
    email:EmailStr

class UserPublic(BaseModel):
    username:str
    email:EmailStr