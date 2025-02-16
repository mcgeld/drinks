from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Coaster(Base):
    __tablename__ = "coasters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=True)

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=False)
    end_time = Column(TIMESTAMP, nullable=True)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    coaster_id = Column(Integer, ForeignKey("coasters.id"))
    session_id = Column(Integer, ForeignKey("sessions.id"))

class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    image_url = Column(String(300), nullable=True)
    is_custom = Column(Boolean, default=False)

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    unit = Column(String(50), nullable=False)
    alcohol_content = Column(Float, default=0.0)

class DrinkIngredient(Base):
    __tablename__ = "drink_ingredients"

    drink_id = Column(Integer, ForeignKey("drinks.id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)
    amount = Column(Float, nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    drink_id = Column(Integer, ForeignKey("drinks.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    status = Column(Enum("pending", "completed", name="order_status"), default="pending")
    created_at = Column(TIMESTAMP, nullable=False)

class OrderModification(Base):
    __tablename__ = "order_modifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    modification = Column(Enum("add", "remove", name="modification_type"), nullable=False)

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    quantity = Column(Float, nullable=False)
    last_updated = Column(TIMESTAMP, nullable=False)

