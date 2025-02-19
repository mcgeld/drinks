from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Coaster, Drink, Order, User
from api.schemas import OrderCreate, OrderResponse
import random
import string

router = APIRouter()

def generate_guest_username():
    """Creates a random guest username like Guest-AB123."""
    return "Guest-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

@router.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Validate coaster_id (it must always be present)
    coaster = db.query(Coaster).filter(Coaster.id == order.coaster_id).first()
    if not coaster:
        raise HTTPException(status_code=404, detail="Coaster not found")

    # Validate drink_id
    drink = db.query(Drink).filter(Drink.id == order.drink_id).first()
    if not drink:
        raise HTTPException(status_code=404, detail="Drink not found")

    # Handle missing user_id (create a guest user)
    if order.user_id is None:
        guest_user = User(is_guest=True, username=generate_guest_username())
        db.add(guest_user)
        db.commit()
        db.refresh(guest_user)
        order.user_id = guest_user.id

    # Validate user_id
    user = db.query(User).filter(User.id == order.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Create and save the order
    new_order = Order(
        drink_id=order.drink_id,
        user_id=order.user_id,
        coaster_id=order.coaster_id,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order
