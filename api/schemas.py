from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str

class CoasterCreate(BaseModel):
    description: str

class OrderBase(BaseModel):
    user_id: Optional[int] = Field(None, ge=1, description="User ID, will be auto-created for guests if missing")
    coaster_id: int = Field(..., ge=1, description="Coaster ID where the order is placed")
    drink_id: int = Field(..., ge=1, description="ID of the drink being ordered")

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True