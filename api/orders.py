from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Order, Drink, User, Coaster
from pydantic import BaseModel

router = APIRouter()

class OrderCreate(BaseModel):
    drink_id: int
    user_id: int
    coaster_id: int

@router.post("/orders")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    # Validate drink exists
    drink = db.query(Drink).filter(Drink.id == order_data.drink_id).first()
    if not drink:
        raise HTTPException(status_code=400, detail="Invalid drink ID")

    # Validate user exists
    user = db.query(User).filter(User.id == order_data.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid user ID")

    # Validate coaster exists
    coaster = db.query(Coaster).filter(Coaster.id == order_data.coaster_id).first()
    if not coaster:
        raise HTTPException(status_code=400, detail="Invalid coaster ID")

    new_order = Order(drink_id=order_data.drink_id, user_id=order_data.user_id, coaster_id=order_data.coaster_id)

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

