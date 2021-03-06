"""empty message

Revision ID: 59e2d53158fb
Revises: 9e8f04ce938b
Create Date: 2019-09-16 13:32:27.437125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59e2d53158fb'
down_revision = '9e8f04ce938b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('credit_transfer', sa.Column('blockchain_task_id', sa.Integer(), nullable=True))
    op.drop_column('credit_transfer', 'blockchain_transaction_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('credit_transfer', sa.Column('blockchain_transaction_hash', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('credit_transfer', 'blockchain_task_id')
    # ### end Alembic commands ###
