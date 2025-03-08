from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Session as DrinkSession
from datetime import datetime

router = APIRouter()

@router.get("/sessions/current")
def get_current_session(db: Session = Depends(get_db)):
    now = datetime.utcnow()

    session = (
        db.query(DrinkSession)
        .filter(DrinkSession.start_time <= now)
        .filter((DrinkSession.end_time == None) | (DrinkSession.end_time > now))
        .order_by(DrinkSession.start_time.desc())
        .first()
    )
    if session is None:
        raise HTTPException(status_code=404, detail="No current session")
    return session

