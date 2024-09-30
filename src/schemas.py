from typing import Optional
from pydantic import BaseModel
from datetime import datetime, time


class User(BaseModel):
    username: str
    email: Optional[str]
    password_hash: str
    created_at: datetime

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