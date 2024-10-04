from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends

from src.db.models import User
from .utils import generate_pass_hash
from .schemas import UserCreateModel


class UserService:
    def get_user_by_email(self, db: Session, email: str):
        """
        returns user by its email

        Args:
            db (Session): _description_
            email (str): _description_

        """
        return db.query(User).filter(User.email == email).first()


    def user_exists(self, email: str, db: Session):
        """
        check if the email is already exists in db

        Args:
            email (str): _description_
            db (Session): _description_

        Returns:
            bool: _description_
        """
        user = self.get_user_by_email(db, email)
        return True if user is not None else False


    def get_user_by_id(self, user_id: int, db: Session):
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


    def create_user(self, user_data: UserCreateModel, db: Session):
        """
        creating a new user

        Args:
            user_data (UserCreateModel): data about user
            db (Session): session of db

        Returns:
            User
        """
        user_data_dict = user_data.model_dump()
        print(user_data_dict)
        new_user = User(**user_data_dict)
        print(new_user)
        new_user.password = generate_pass_hash(user_data_dict["password"])
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

