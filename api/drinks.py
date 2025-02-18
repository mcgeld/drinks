from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Drink
from pydantic import BaseModel
from fastapi import HTTPException

router = APIRouter()

##########
# DRINKS #
##########
@router.get("/drinks")
def get_drinks(db: Session = Depends(get_db)):
    drinks = db.query(Drink).all()
    return drinks

# Schema for incoming drink data
class DrinkCreate(BaseModel):
    name: str
    description: str
    image_url: str

@router.post("/drinks")
def create_drink(drink_data: DrinkCreate, db: Session = Depends(get_db)):
    new_drink = Drink(**drink_data.dict())
    db.add(new_drink)
    db.commit()
    db.refresh(new_drink)
    return new_drink

class DrinkUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    image_url: str | None = None

@router.put("/drinks/{drink_id}")
def update_drink(drink_id: int, drink_data: DrinkUpdate, db: Session = Depends(get_db)):
    drink = db.query(Drink).filter(Drink.id == drink_id).first()
    if not drink:
        raise HTTPException(status_code=404, detail="Drink not found")

    for field, value in drink_data.dict(exclude_unset=True).items():
        setattr(drink, field, value)

    db.commit()
    db.refresh(drink)
    return drink

@router.delete("/drinks/{drink_id}")
def delete_drink(drink_id: int, db: Session = Depends(get_db)):
    drink = db.query(Drink).filter(Drink.id == drink_id).first()
    if not drink:
        raise HTTPException(status_code=404, detail="Drink not found")

    db.delete(drink)
    db.commit()
    return {"message": "Drink deleted successfully"}
