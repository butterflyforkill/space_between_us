from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.config_files import APIkeys
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = f"postgresql://postgres:{APIkeys.DATABASEpass}@localhost:5432/space_beetween_us"

engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


