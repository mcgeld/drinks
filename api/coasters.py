from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Coaster
from pydantic import BaseModel

router = APIRouter()

class CoasterCreate(BaseModel):
    description: str

@router.post("/coasters")
def create_coaster(coaster_data: CoasterCreate, db: Session = Depends(get_db)):
    new_coaster = Coaster(description=coaster_data.description)
    db.add(new_coaster)
    db.commit()
    db.refresh(new_coaster)
    return new_coaster

