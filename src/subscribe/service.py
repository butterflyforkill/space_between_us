from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from src.db.models import TelegramToken, SubscribeCategory, UserSubscription, UserNotification
from .schemas import CategoryCreateModel


class SubscribeService():
    
    def get_all_subscrivbe_categories(self, db: Session):
        """
        Rtrun all the subscribe categories

        Args:
            db (Session): _description_

        Returns:
            _type_: _description_
        """
        return db.query(SubscribeCategory).all()
    
    
    def create_category(self, category_data: CategoryCreateModel, creator: int, db: Session):
        """_summary_

        Args:
            db (Session): _description_
        """
        category_dict = category_data.model_dump()
        new_category = SubscribeCategory(**category_dict)
        new_category.creator = creator
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
        


