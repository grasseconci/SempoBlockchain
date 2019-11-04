"""empty message

Revision ID: 08176a025509
Revises: 5de7c462a1e6
Create Date: 2019-11-04 22:05:13.495741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08176a025509'
down_revision = '5de7c462a1e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transfer_usage', sa.Column('_name', sa.String(), nullable=True))
    op.drop_constraint('transfer_usage_name_key', 'transfer_usage', type_='unique')
    op.create_unique_constraint(None, 'transfer_usage', ['_name'])
    op.drop_column('transfer_usage', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transfer_usage', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'transfer_usage', type_='unique')
    op.create_unique_constraint('transfer_usage_name_key', 'transfer_usage', ['name'])
    op.drop_column('transfer_usage', '_name')
    # ### end Alembic commands ###
