from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )

#Database Init
def get_db():
    conn = sqlite3.connect("drinks.db")
    conn.row_factory = sqlite3.Row
    return conn

class OrderRequest(BaseModel):
    drink_id: int

@app.get("/api/drinks")
def get_drinks():
    conn = get_db()
    drinks = conn.execute("SELECT * FROM drinks").fetchall()
    conn.close()
    return [dict(row) for row in drinks]

@app.post("/api/order")
def place_order(order: OrderRequest):
    conn = get_db()
    conn.execute("INSERT INTO orders (drink_id) VALUES (?)", (order.drink_id,))
    conn.commit()
    conn.close()
    return {"message":"Order placed!"}
