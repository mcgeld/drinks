"""Auto-save: Tue 18 Feb 06:38:43 GMT 2025 (DB migration)

Revision ID: f988e856b968
Revises: 4b58e208d0d1
Create Date: 2025-02-18 06:38:45.998577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f988e856b968'
down_revision: Union[str, None] = '4b58e208d0d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
