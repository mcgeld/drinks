"""Actually add initial tables for drinks system

Revision ID: 15f3472b82af
Revises: b9cb4c48293e
Create Date: 2025-02-15 00:39:04.155218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15f3472b82af'
down_revision: Union[str, None] = 'b9cb4c48293e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Migration script for setting up initial tables

def upgrade():
    # Create coasters table
    op.create_table(
        "coasters",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("description", sa.Text, nullable=True),
    )

    # Create sessions table
    op.create_table(
        "sessions",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("start_time", sa.TIMESTAMP, server_default=sa.func.current_timestamp()),
        sa.Column("end_time", sa.TIMESTAMP, nullable=True),
    )

    # Create customers table
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("coaster_id", sa.Integer, sa.ForeignKey("coasters.id")),
        sa.Column("session_id", sa.Integer, sa.ForeignKey("sessions.id")),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.func.current_timestamp()),
    )

    # Create drinks table
    op.create_table(
        "drinks",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("image_url", sa.String(255), nullable=True),
        sa.Column("is_custom", sa.Boolean, server_default="false"),
    )

    # Create ingredients table
    op.create_table(
        "ingredients",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("unit", sa.String(50), nullable=False),  # "oz", "ml", etc.
        sa.Column("alcohol_content", sa.Float, server_default="0"),  # Percentage (e.g., 40 = 40%)
    )

    # Create drink_ingredients table (Many-to-Many relationship between drinks & ingredients)
    op.create_table(
        "drink_ingredients",
        sa.Column("drink_id", sa.Integer, sa.ForeignKey("drinks.id"), primary_key=True),
        sa.Column("ingredient_id", sa.Integer, sa.ForeignKey("ingredients.id"), primary_key=True),
        sa.Column("amount", sa.Float, nullable=False),  # e.g., 2 oz
    )

    # Create orders table
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("drink_id", sa.Integer, sa.ForeignKey("drinks.id")),
        sa.Column("customer_id", sa.Integer, sa.ForeignKey("customers.id")),
        sa.Column("status", sa.Enum("pending", "completed", name="order_status"), server_default="pending"),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.func.current_timestamp()),
    )

    # Create order_modifications table (stores ingredient changes)
    op.create_table(
        "order_modifications",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("order_id", sa.Integer, sa.ForeignKey("orders.id")),
        sa.Column("ingredient_id", sa.Integer, sa.ForeignKey("ingredients.id")),
        sa.Column("modification", sa.Enum("add", "remove", name="modification_type"), nullable=False),
    )

    # Create inventory table
    op.create_table(
        "inventory",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("ingredient_id", sa.Integer, sa.ForeignKey("ingredients.id")),
        sa.Column("quantity", sa.Float, nullable=False),  # How much of the ingredient is left
        sa.Column("last_updated", sa.TIMESTAMP, server_default=sa.func.current_timestamp()),
    )

def downgrade():
    op.drop_table("inventory")
    op.drop_table("order_modifications")
    op.drop_table("orders")
    op.drop_table("drink_ingredients")
    op.drop_table("ingredients")
    op.drop_table("drinks")
    op.drop_table("customers")
    op.drop_table("sessions")
    op.drop_table("coasters")

