from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from data_manager.database_manger import Base


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
