from passlib.context import CryptContext
from datetime import timedelta, datetime
import jwt
import uuid
from src.config.config_files import Settings

ACCESS_TOKEN_EXPIRY = 3600


password_context = CryptContext(
    schemes=["bcrypt"]
)

def generate_pass_hash(password: str) -> str:
    """
    hashing password

    Args:
        password (str): password from user

    Returns:
        str: hasshed password
    """
    return password_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    """
    verifing password

    Args:
        password (str): password from user
        hash (str): password hash frrom db

    Returns:
        bool: True or False
    """
    return password_context.verify(password, hash)


def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    payload = {}
    payload['user'] = user_data
    payload['exp'] = datetime.now() + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY))
    payload['jti'] = str(uuid.uuid4())
    token = jwt.encode(
        payload=payload,
        key=Settings.JWT_SECRET_KEY,
        algorithm=Settings.JWT_ALGORITHM
    )
    return token