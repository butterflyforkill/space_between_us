import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
@dataclass(frozen=True)
class Settings:
    TOKENkey: str = os.getenv('token')
    APIkey: str = os.getenv('apikey')
    DATABASEpass: str = os.getenv('databasepass')
    JWT_SECRET_KEY: str = os.getenv('jwt_secret_key')
    JWT_ALGORITHM: str = os.getenv('jwt_algorithm')
    REDIS_HOST: str = os.getenv('redis_host')
    REDIS_PORT: int = os.getenv('redis_port')