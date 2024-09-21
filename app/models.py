from typing import Optional
from pydantic import BaseModel
from datetime import datetime, time
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())

    telegram_tokens = relationship("TelegramToken", backref="user")
    subscriptions = relationship("UserSubscription", backref="user")
    notifications = relationship("UserNotification", backref="user")

class TelegramToken(Base):
    __tablename__ = "telegram_tokens"

    token_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    telegram_token = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())

class SubscribeCategory(Base):
    __tablename__ = "subscribe_categories"

    category_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    subscription_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    category_id = Column(Integer, ForeignKey("subscribe_categories.category_id"))
    created_at = Column(TIMESTAMP, default=func.now())

class UserNotification(Base):
    __tablename__ = "user_notifications"

    notification_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    notification_time = Column(Time, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())

# Pydantic models (data validation and serialization)
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