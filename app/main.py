from fastapi import FastAPI, HTTPException, Depends
import models
import schemas
from database import engine, SessionLocal


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
         db.close()


