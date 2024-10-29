import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
@dataclass(frozen=True)
class Settings:
    TOKENkey: str = os.getenv('token')
    TG_API_ID: int = os.getenv('tg_api_id')
    TG_API_HASH: str = os.getenv('tg_api_hash')
    DATABASEpass: str = os.getenv('databasepass')