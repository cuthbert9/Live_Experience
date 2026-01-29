"""genres as attributes 

Revision ID: 7ac6f5281c71
Revises: 34485d8e00b1
Create Date: 2026-01-29 17:18:53.139475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = '7ac6f5281c71'
down_revision: Union[str, Sequence[str], None] = '34485d8e00b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
