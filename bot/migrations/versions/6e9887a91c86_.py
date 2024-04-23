"""empty message

Revision ID: 6e9887a91c86
Revises: c2cf07b4c618
Create Date: 2024-04-23 21:30:28.642002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e9887a91c86'
down_revision: Union[str, None] = 'c2cf07b4c618'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timetables',
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timetables')
    # ### end Alembic commands ###