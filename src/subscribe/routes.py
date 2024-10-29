from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from telethon import TelegramClient
from sqlalchemy.orm import Session
from src.db.dependencies import get_db
from .schemas import SubscribeCategoryModel, CategoryCreateModel, UserSubcribeCategory, CategoryUpdateModel
from src.auth.dependencies import AccessTokenBearer, RoleChecker
from .service import SubscribeService
from src.tg_handler.tg_client import get_telegram_client

acccess_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(["admin", "user"]))
subscribe_router = APIRouter()
subscribe_service = SubscribeService()

@subscribe_router.post('/profile/telegram_auth')
async def telegram_auth(client: TelegramClient = Depends(get_telegram_client)):
    """
    Initiates Telegram authentication flow.

    Raises:
        HTTPException: If Telegram authentication fails.
    """

    # 1. Generate a unique link for Telegram Login Widget
    try:
        auth_link = await client.cl
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate Telegram login link: {e}")

    # 2. Return the link to the frontend for user redirection
    return {"message": "Please open this link in Telegram to authorize:", "link": auth_link}


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


@subscribe_router.patch(
    '/update_category/{category_id}',
    response_model=SubscribeCategoryModel,
    dependencies=[role_checker]
)
async def update_category(
    category_id: int,
    category_model: CategoryUpdateModel,
    session: Session = Depends(get_db),
    _: dict = Depends(acccess_token_bearer)
):
    print(category_id)
    return subscribe_service.update_category(category_id, category_model, session)


@subscribe_router.delete(
    '/delete_category/{category_id}',
    status_code=status.HTTP_200_OK,
    dependencies=[role_checker]
)
async def delete_category(
    category_id: int,
    session: Session = Depends(get_db),
    _: dict = Depends(acccess_token_bearer)
):
    return subscribe_service.delete_category(category_id, session)


@subscribe_router.post(
    '/{categorie_id}/subscribe',
    status_code=status.HTTP_201_CREATED,
    dependencies=[role_checker]
    )
async def subscribe(
    categorie_id: int,
    subscribe_model: UserSubcribeCategory,
    session: Session = Depends(get_db),
    token_details: dict = Depends(acccess_token_bearer)
    ):
    """
    user choose the categorie and subscribe to it 
    in the form where he can put the time when he want to receive news

    Args:
        categorie_id (int): _description_
    """
    user_id = token_details.get("user")["user_id"]
    return subscribe_service.subscribe(subscribe_model, categorie_id, user_id, session)


@subscribe_router.delete(
    '/{categorie_id}/unsubscribe',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[role_checker]
    )
async def unsubscribe(
    categorie_id: int,
    session: Session = Depends(get_db),
    token_details: dict = Depends(acccess_token_bearer)
    ):
    """
    user unsubscribes from the news categorie
    (it'll delete it from the table UserSubscription and UserNotification)

    Args:
        categorie_id (int): _description_
    """
    user_id = token_details.get("user")["user_id"]
    unsubscribe = subscribe_service.unsubscribe(categorie_id, user_id, session)
    if unsubscribe is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return {"msg": f"You unsubscribe successfully"}
