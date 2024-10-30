from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.config_files import Settings
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = Settings.DATABASE_URL
engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


