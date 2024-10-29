from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from src.db.models import TelegramToken, SubscribeCategory, UserSubscription, UserNotification
from .schemas import CategoryCreateModel, UserSubcribeCategory, CategoryUpdateModel


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
    
    
    def get_category_by_id(self, category_id: int, db: Session):
        return db.query(SubscribeCategory).filter(SubscribeCategory.category_id==category_id).first()
    
    
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
    
    
    def delete_category(self, category_id: int, db: Session):
        category_to_delete = self.get_category_by_id(category_id, db)
        if not category_to_delete:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        db.delete(category_to_delete)
        db.commit()
        return {"msg": f"You delete category successfully"}
    
    
    def update_category(self, category_id: int, category_data: CategoryUpdateModel, db: Session):
        category_to_update = self.get_category_by_id(category_id, db)
        print(category_to_update)
        if not category_to_update:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        updated_data = category_data.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(category_to_update, key, value)
        db.add(category_to_update)
        db.commit()
        return category_to_update
    
    
    def subscribe(self, subscribe_data: UserSubcribeCategory, category_id: int, user_id: int, db: Session):
        notification_time = subscribe_data.notification
        exist_category = self.get_category_by_id(category_id, db)
        if not exist_category:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        new_subscribe = UserSubscription(user_id=user_id, category_id=category_id)
        new_notification = UserNotification(user_id=user_id, notification_time=notification_time)
        db.add_all([new_subscribe, new_notification])
        db.commit()
        db.refresh(new_subscribe)
        db.refresh(new_notification)
        return {"msg": f"You subscribe successfully"}
        


    def unsubscribe(self, category_id: int, user_id: int, db: Session):
        subscribe_to_delete = db.query(UserSubscription).filter(UserSubscription.category_id==category_id, user_id==user_id).first()
        notification_to_delete = db.query(UserNotification).filter(UserNotification.user_id==user_id).first()
        if subscribe_to_delete is not None and notification_to_delete is not None:
            db.delete(subscribe_to_delete)
            db.delete(notification_to_delete)
            db.commit()
            return {}
        return None
        


