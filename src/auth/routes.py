from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import UserCreateModel, UserModel
from src.db.dependencies import get_db
from .service import UserService


auth_router = APIRouter()
user_service = UserService()

@auth_router.post(
    '/sign_up', 
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED
    )
async def create_user_account(user_data: UserCreateModel, session: Session = Depends(get_db)):
    email = user_data.email

    user_exists = user_service.user_exists(email, session)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with email:{email} already exists")
    
    new_user = user_service.create_user(user_data, session)
    
    return new_user