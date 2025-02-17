"""Initial migration

Revision ID: 8f3217136551
Revises: 
Create Date: 2025-02-17 01:26:35.347554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f3217136551'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coasters',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drinks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(length=300), nullable=True),
    sa.Column('is_custom', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sessions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('start_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('end_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('units',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('abbreviation', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('abbreviation'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=True),
    sa.Column('is_guest', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.Column('abv', sa.Float(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('drink_id', sa.Integer(), nullable=False),
    sa.Column('coaster_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'completed', name='order_status'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['coaster_id'], ['coasters.id'], ),
    sa.ForeignKeyConstraint(['drink_id'], ['drinks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_conversions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('from_unit_id', sa.Integer(), nullable=False),
    sa.Column('to_unit_id', sa.Integer(), nullable=False),
    sa.Column('conversion_factor', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['from_unit_id'], ['units.id'], ),
    sa.ForeignKeyConstraint(['to_unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drink_ingredients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('drink_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('override_unit_id', sa.Integer(), nullable=True),
    sa.Column('special_instruction', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['drink_id'], ['drinks.id'], ),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['override_unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('last_updated', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_modifications',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.Column('modification', sa.Enum('add', 'remove', name='modification_type'), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_modifications')
    op.drop_table('inventory')
    op.drop_table('drink_ingredients')
    op.drop_table('unit_conversions')
    op.drop_table('orders')
    op.drop_table('ingredients')
    op.drop_table('users')
    op.drop_table('units')
    op.drop_table('sessions')
    op.drop_table('drinks')
    op.drop_table('coasters')
    # ### end Alembic commands ###
