from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Coaster(Base):
    __tablename__ = "coasters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=True)

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=True) # Null for guests
    email = Column(String(100), unique=True, nullable=True) # Null for guests
    hashed_password = Column(String(255), nullable=True) # Null for guests
    is_guest = Column(Boolean, default=True) # True for guests, False for real users
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    image_url = Column(String(300), nullable=True)
    is_custom = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    abv = Column(Float, default=0.0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

class DrinkIngredient(Base):
    __tablename__ = "drink_ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    drink_id = Column(Integer, ForeignKey("drinks.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    amount = Column(Float, nullable=True)
    override_unit_id = Column(Integer, ForeignKey("units.id"), nullable=True)
    special_instruction = Column(String(255), nullable=True)

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    abbreviation = Column(String(10), unique=True, nullable=False)

class UnitConversion(Base):
    __tablename__ = "unit_conversions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    to_unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    conversion_factor = Column(Float, nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    drink_id = Column(Integer, ForeignKey("drinks.id"), nullable=False)
    coaster_id = Column(Integer, ForeignKey("coasters.id"), nullable=True)
    status = Column(Enum("pending", "completed", name="order_status"), default="pending")
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

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
    last_updated = Column(TIMESTAMP, server_default=func.now())

