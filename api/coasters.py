from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/coasters/{coaster_id}")
def get_coaster(coaster_id: int, db: Session = Depends(get_db)):
    coaster = db.query(Coaster).filter(Coaster.id == coaster_id).first()
    if not coaster:
        raise HTTPException(status_code=404, detail="Coaster not found")
    # FastAPI automatically handles status codes for successful responses.
    # Returning a tuple here results in an unexpected response body. Instead,
    # return just the coaster instance so FastAPI can serialize it correctly.
    return coaster
