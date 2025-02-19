from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Order, User
from schemas import OrderCreate

router = APIRouter()

@router.post("/sessions/{session_id}/close")
def close_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(Session).filter(Session.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Delete guest users linked to this session
    guest_users = db.query(User).filter(User.is_guest == True).all()
    for guest in guest_users:
        db.delete(guest)

    db.commit()
    return {"message": f"Session {session_id} closed, guest users deleted"}

