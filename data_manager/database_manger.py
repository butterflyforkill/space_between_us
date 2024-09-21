from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config_files import APIkeys
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = f"postgresql://user:{APIkeys.DATABASEpass}@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
