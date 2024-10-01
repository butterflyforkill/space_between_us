from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends

from .models import User



def get_user_by_email(db: Session, email: str):
    """
    returns user by its email

    Args:
        db (Session): _description_
        email (str): _description_

    """
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    """
    returns user by its id

    Args:
        db (Session): _description_
        user_id (int): _description_
    """
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found in the db")
    return user


