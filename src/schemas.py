from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime, time


class UserCreateModel(BaseModel):
    username: str = Field(max_length=25)
    email: Optional[str] = Field(max_length=40)
    password: str = Field(min_length=8)

class TelegramToken(BaseModel):
    user_id: int
    telegram_token: str
    created_at: datetime

class SubscribeCategory(BaseModel):
    name: str
    description: Optional[str]

class UserSubscription(BaseModel):
    user_id: int
    category_id: int
    created_at: datetime

class UserNotification(BaseModel):
    user_id: int
    notification_time: time
    created_at: datetime