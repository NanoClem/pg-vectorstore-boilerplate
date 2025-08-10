"""init vectorstore

Revision ID: f1d8cbc97814
Revises: 
Create Date: 2025-08-10 22:13:31.610004

"""
from typing import Sequence, Union

import pgvector.sqlalchemy as pgvector_sa
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f1d8cbc97814'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('vectorstore',
        sa.Column('id', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('embedding', pgvector_sa.VECTOR(dim=768), nullable=False),
        sa.Column('metadata', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('content'),
        schema='public'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('vectorstore', schema='public')
