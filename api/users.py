from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    name: str

@router.post("/users")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user_data.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

