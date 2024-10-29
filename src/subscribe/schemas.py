from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class SubscribeCategoryModel(BaseModel):
    category_id: int
    name: Optional[str] = Field(max_length=50)
    description: Optional[str] = Field(max_length=250)
    creator: int
    created_at: datetime
    updated_at: datetime

class CategoryCreateModel(BaseModel):
    name: Optional[str] = Field(max_length=50)
    description: Optional[str] = Field(max_length=250)


class CategoryUpdateModel(BaseModel):
    name: str = Field(max_length=50)
    description: str = Field(max_length=250)


class UserSubcribeCategory(BaseModel):
    notification: str


class SubscribeResponse(BaseModel):
    pass
    
