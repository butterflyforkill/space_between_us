from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.db.dependencies import get_db
from .schemas import SubscribeCategoryModel, CategoryCreateModel
from src.auth.dependencies import AccessTokenBearer, RoleChecker
from .service import SubscribeService

acccess_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(["admin", "user"]))
subscribe_router = APIRouter()
subscribe_service = SubscribeService()

@subscribe_router.post('/profile/telegram_auth')
async def telegram_auth():
    """
    telegram auth
    """
    pass


@subscribe_router.get(
    '/subscription_categories',
    response_model=List[SubscribeCategoryModel],
    dependencies=[role_checker]
    )
async def subscription_list(session: Session = Depends(get_db),  _: dict = Depends(acccess_token_bearer)):
    """
    the list of categories for subscribe
    """
    return subscribe_service.get_all_subscrivbe_categories(session)


@subscribe_router.post(
    '/create_category',
    status_code=status.HTTP_201_CREATED,
    response_model=SubscribeCategoryModel,
    dependencies=[role_checker]
    )
async def create_category(
    category_model: CategoryCreateModel,
    session: Session = Depends(get_db),
    token_details: dict = Depends(acccess_token_bearer)
    ) -> dict:
    """
    available only for the admin
    going to the form to create the catogory and send it to database
    """
    creator_id = token_details.get("user")["user_id"]
    return subscribe_service.create_category(category_model, creator_id, session)
    


# @subscribe_router.route('/subscription_categories/{int:categorie_id}/subscribe', methods=['GET', 'POST'])
# async def subscribe(categorie_id):
#     """
#     user choose the categorie and subscribe to it 
#     in the form where he can put the time when he want to receive news

#     Args:
#         categorie_id (int): _description_
#     """
#     pass


# @subscribe_router.delete('/subscription_categories/{int:categorie_id}/unsubscribe')
# async def unsubscribe(categorie_id):
#     """
#     user unsubscribes from the news categorie
#     (it'll delete it from the table UserSubscription and UserNotification)

#     Args:
#         categorie_id (int): _description_
#     """
#     pass
