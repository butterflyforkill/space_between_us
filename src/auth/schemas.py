from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class UserCreateModel(BaseModel):
    username: str = Field(max_length=25)
    email: Optional[str] = Field(max_length=40)
    password: str = Field(min_length=8)


class UserModel(BaseModel):
    user_id : int
    username : str
    email : str
    password: str = Field(exclude=True)
    created_at : datetime
    updated_at : datetime ###!!!!! migration
    

class UserLoginModel(BaseModel):
    email: Optional[str] = Field(max_length=40)
    password: str = Field(min_length=8)