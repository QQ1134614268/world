"""empty message

Revision ID: 33c5d895e1bc
Revises: 0887a8251cb6
Create Date: 2022-02-28 23:39:40.854253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33c5d895e1bc'
down_revision = '0887a8251cb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_t', sa.Column('goods_img', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_t', 'goods_img')
    # ### end Alembic commands ###
