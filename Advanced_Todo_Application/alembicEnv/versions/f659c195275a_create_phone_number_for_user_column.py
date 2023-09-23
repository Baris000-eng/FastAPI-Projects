"""Create phone number for user column

Revision ID: f659c195275a
Revises: b94ef3b662fd
Create Date: 2023-09-23 11:59:26.917004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f659c195275a'
down_revision: Union[str, None] = 'b94ef3b662fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
