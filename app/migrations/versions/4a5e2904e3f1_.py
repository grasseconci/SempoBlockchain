"""empty message

Revision ID: 4a5e2904e3f1
Revises: 7583891c4ae5
Create Date: 2018-09-23 19:02:45.126669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a5e2904e3f1'
down_revision = '7583891c4ae5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('_is_subvendor', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('_is_vendor', sa.Boolean(), nullable=True))
    op.drop_column('user', 'is_vendor')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_vendor', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('user', '_is_vendor')
    op.drop_column('user', '_is_subvendor')
    # ### end Alembic commands ###
