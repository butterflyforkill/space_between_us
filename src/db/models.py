from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, Time
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, server_default="user")
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())

    subscriptions = relationship("UserSubscription", backref="user")
    notifications = relationship("UserNotification", backref="user")


class TelegramToken(Base):
    __tablename__ = "telegram_tokens"

    token_id = Column(Integer, primary_key=True)
    tg_user_id = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default=func.now())

class SubscribeCategory(Base):
    __tablename__ = "subscribe_categories"

    category_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    creator = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())

class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    subscription_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    category_id = Column(Integer, ForeignKey("subscribe_categories.category_id", ondelete='CASCADE'))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())

class UserNotification(Base):
    __tablename__ = "user_notifications"

    notification_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    notification_time = Column(Time, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())
