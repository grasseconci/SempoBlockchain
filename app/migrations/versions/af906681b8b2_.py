"""empty message

Revision ID: af906681b8b2
Revises: 1a8a9213e85d
Create Date: 2019-10-10 11:41:33.047381

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af906681b8b2'
down_revision = '1a8a9213e85d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ussd_sessions', sa.Column('session_data', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    op.drop_column('ussd_sessions', 'sessions_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ussd_sessions', sa.Column('sessions_data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.drop_column('ussd_sessions', 'session_data')
    # ### end Alembic commands ###