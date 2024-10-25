from fastapi import FastAPI, HTTPException, Depends
import src.db.models as models
from src.db.database import engine
from src.auth.routes import auth_router
from src.subscribe.routes import subscribe_router


version = "v1"

description = """
Space Beetween Us - Telegram-Based News Delivery Platform
    """

version_prefix =f"/api/{version}"

app = FastAPI(
    title="Space Beetween Us",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
)

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(subscribe_router, prefix="/subscribe", tags=["subscribe"])