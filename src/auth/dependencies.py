from typing import Coroutine
from fastapi.security.http import HTTPAuthorizationCredentials
from typing_extensions import Annotated, Doc
from fastapi import Depends, Request, HTTPException, status
from fastapi.security import HTTPBearer
from .utils import decode_token


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        token = creds.credentials

        token_data = decode_token(token)

        if not self.token_valid(token):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or expired token"
                )

        if token_data['refresh']:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide a valid token"
                )
            

        return token_data
    
    def token_valid(self, token: str) -> bool:
        token_data = decode_token(token)

        return token_data is not None


class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and not token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )