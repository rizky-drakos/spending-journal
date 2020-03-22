"""empty message

Revision ID: 4ed5b0eb6e92
Revises: 
Create Date: 2020-03-21 08:06:41.664733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ed5b0eb6e92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item_types', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item_types', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item_types', type_='foreignkey')
    op.drop_column('item_types', 'user_id')
    # ### end Alembic commands ###
