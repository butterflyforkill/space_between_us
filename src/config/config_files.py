import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
@dataclass(frozen=True)
class Settings:
    APIkey: str = os.getenv('apikey')
    JWT_SECRET_KEY: str = os.getenv('jwt_secret_key')
    JWT_ALGORITHM: str = os.getenv('jwt_algorithm')
    REDIS_HOST: str = os.getenv('redis_host')
    REDIS_PORT: int = os.getenv('redis_port')
    REDIS_PASS: int = os.getenv('redis_password')
    EXT_DATABASE_URL: str = os.getenv('ext_database_url')
    INT_DATABASE_URL: str = os.getenv('int_database_url')
    
    