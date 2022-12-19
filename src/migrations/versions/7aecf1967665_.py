"""empty message

Revision ID: 7aecf1967665
Revises: e470a5a8a99e
Create Date: 2022-03-03 01:42:48.701040

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7aecf1967665'
down_revision = 'e470a5a8a99e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('store_role_t',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.Column('create_by', sa.Integer(), nullable=True, comment='创建者id'),
    sa.Column('update_by', sa.Integer(), nullable=True, comment='修改者id'),
    sa.Column('role_name', sa.String(length=256), nullable=True, comment='角色,翻译'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_store_role_t_role_name'), 'store_role_t', ['role_name'], unique=False)
    op.alter_column('qr_code_t', 'url_dic',
               existing_type=mysql.JSON(),
               comment='url参数',
               existing_comment='下单桌号',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'url',
               existing_type=mysql.VARCHAR(length=255),
               comment='网址',
               existing_comment='下单桌号',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'img_path',
               existing_type=mysql.VARCHAR(length=255),
               comment='二维码中间头像',
               existing_comment='下单桌号',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'img_width',
               existing_type=mysql.VARCHAR(length=255),
               comment='二维码中间头像的宽度',
               existing_comment='下单桌号',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'img_height',
               existing_type=mysql.VARCHAR(length=255),
               comment='二维码中间头像的高度',
               existing_comment='下单桌号',
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('qr_code_t', 'img_height',
               existing_type=mysql.VARCHAR(length=255),
               comment='下单桌号',
               existing_comment='二维码中间头像的高度',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'img_width',
               existing_type=mysql.VARCHAR(length=255),
               comment='下单桌号',
               existing_comment='二维码中间头像的宽度',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'img_path',
               existing_type=mysql.VARCHAR(length=255),
               comment='下单桌号',
               existing_comment='二维码中间头像',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'url',
               existing_type=mysql.VARCHAR(length=255),
               comment='下单桌号',
               existing_comment='网址',
               existing_nullable=True)
    op.alter_column('qr_code_t', 'url_dic',
               existing_type=mysql.JSON(),
               comment='下单桌号',
               existing_comment='url参数',
               existing_nullable=True)
    op.drop_index(op.f('ix_store_role_t_role_name'), table_name='store_role_t')
    op.drop_table('store_role_t')
    # ### end Alembic commands ###
