from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Drink

app = FastAPI()

@app.get("/api/drinks")
def get_drinks(db: Session = Depends(get_db)):
    drinks = db.query(Drink).all()
    return drinks
