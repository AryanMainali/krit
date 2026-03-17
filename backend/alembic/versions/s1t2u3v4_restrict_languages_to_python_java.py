"""Restrict active languages to Python and Java.

Revision ID: s1t2u3v4
Revises: r0s1t2u3
Create Date: 2026-03-17

"""
from typing import Sequence, Union

from alembic import op


revision: str = "s1t2u3v4"
down_revision: Union[str, None] = "r0s1t2u3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Keep only Python and Java active in existing installations.
    op.execute(
        """
        UPDATE languages
        SET is_active = CASE
            WHEN lower(name) IN ('python', 'java') THEN TRUE
            ELSE FALSE
        END
        """
    )


def downgrade() -> None:
    # Re-activate all languages.
    op.execute("UPDATE languages SET is_active = TRUE")
