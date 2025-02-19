from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from api.schemas import UserCreate

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

