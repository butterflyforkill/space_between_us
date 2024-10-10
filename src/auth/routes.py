from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from datetime import timedelta
from .dependencies import AccessTokenBearer
from .schemas import UserCreateModel, UserModel, UserLoginModel
from src.db.dependencies import get_db
from .service import UserService
from .utils import (
    create_access_token, 
    decode_token, 
    verify_password
    )


auth_router = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXPIRY = 2

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


@auth_router.post('/login')
async def login_user(login_data: UserLoginModel, session: Session = Depends(get_db)):
    email = login_data.email
    password = login_data.password
    user = user_service.get_user_by_email(session, email)
    if user_service.user_exists(email, session):
        if verify_password(password, user.password):
            access_token = create_access_token(
                user_data={
                    'email': user.email,
                    'user_id': user.user_id
                }
            )
            
            refresh_token = create_access_token(
                user_data={
                    'email': user.email,
                    'user_id': user.user_id
                },
                refresh=True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY)
            )
            
            return JSONResponse(
                content={
                    "message": "Login is successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {
                        "email": user.email,
                        "user_id": user.user_id
                    }
                }
            )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid email or password"
        )