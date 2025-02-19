from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Coaster
from api.schemas import CoasterCreate

router = APIRouter()

@router.post("/coasters")
def create_coaster(coaster: CoasterCreate, db: Session = Depends(get_db)):
    new_coaster = Coaster(**coaster.dict())
    db.add(new_coaster)
    db.commit()
    db.refresh(new_coaster)
    return new_coaster

