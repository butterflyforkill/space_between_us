from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime, time


class UserCreateModel(BaseModel):
    username: str = Field(max_length=25)
    email: Optional[str] = Field(max_length=40)
    password: str = Field(min_length=8)