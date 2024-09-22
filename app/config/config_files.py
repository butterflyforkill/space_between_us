import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
@dataclass(frozen=True)
class APIkeys:
    TOKENkey: str = os.getenv('token')
    APIkey: str = os.getenv('apikey')
    DATABASEpass: str = os.getenv('databasepass')