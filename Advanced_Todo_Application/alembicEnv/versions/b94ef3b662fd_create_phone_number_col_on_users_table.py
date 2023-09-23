"""create phone number col on users table

Revision ID: b94ef3b662fd
Revises: 
Create Date: 2023-09-23 11:05:14.263978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b94ef3b662fd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Docs:

    It modifies the table called 'users'. This function performs
    this modification by adding a new column called 'phone_number',
    of type String, and is nullable.
    :return:
    """
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    pass
