"""empty message

Revision ID: 0a5b123d9ba3
Revises: 46766e23a8f6
Create Date: 2023-10-22 17:37:50.819094

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a5b123d9ba3'
down_revision = '46766e23a8f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('js_form',
    sa.Column('TABLE_CATALOG', sa.String(length=64), nullable=False),
    sa.Column('TABLE_SCHEMA', sa.String(length=64), nullable=False),
    sa.Column('TABLE_NAME', sa.String(length=64), nullable=True),
    sa.Column('COLUMN_NAME', sa.String(length=64), nullable=False),
    sa.Column('ORDINAL_POSITION', sa.String(length=64), nullable=True),
    sa.Column('COLUMN_DEFAULT', sa.String(length=64), nullable=True),
    sa.Column('IS_NULLABLE', sa.String(length=64), nullable=True),
    sa.Column('DATA_TYPE', sa.String(length=64), nullable=True),
    sa.Column('CHARACTER_MAXIMUM_LENGTH', sa.String(length=64), nullable=True),
    sa.Column('CHARACTER_OCTET_LENGTH', sa.String(length=64), nullable=True),
    sa.Column('NUMERIC_PRECISION', sa.String(length=64), nullable=True),
    sa.Column('NUMERIC_SCALE', sa.String(length=64), nullable=True),
    sa.Column('DATETIME_PRECISION', sa.String(length=64), nullable=True),
    sa.Column('CHARACTER_SET_NAME', sa.String(length=64), nullable=True),
    sa.Column('COLLATION_NAME', sa.String(length=64), nullable=True),
    sa.Column('COLUMN_TYPE', sa.String(length=64), nullable=True),
    sa.Column('COLUMN_KEY', sa.String(length=64), nullable=True),
    sa.Column('EXTRA', sa.String(length=64), nullable=True),
    sa.Column('PRIVILEGES', sa.String(length=64), nullable=True),
    sa.Column('COLUMN_COMMENT', sa.String(length=64), nullable=True),
    sa.Column('GENERATION_EXPRESSION', sa.String(length=64), nullable=True),
    sa.Column('SRS_ID', sa.String(length=64), nullable=True),
    sa.Column('name_cn', sa.String(length=64), nullable=True),
    sa.Column('data_type2', sa.String(length=64), nullable=True),
    sa.Column('num_max', sa.String(length=64), nullable=True),
    sa.Column('num_min', sa.String(length=64), nullable=True),
    sa.Column('valid_regx', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('TABLE_CATALOG', 'TABLE_SCHEMA', 'COLUMN_NAME'),
    comment='js_form',
    mysql_charset='utf8mb4',
    mysql_collate='utf8mb4_general_ci',
    mysql_engine='InnoDB'
    )
    op.drop_index('ix_store_role_t_role_name', table_name='store_role_t')
    op.drop_table('store_role_t')
    op.add_column('enum_config', sa.Column('label', sa.String(length=255), nullable=False, comment='枚举value翻译'))
    op.alter_column('enum_config', 'value',
               existing_type=mysql.VARCHAR(length=255),
               comment='枚举value数据,一般映射成数字',
               existing_comment='枚举value数据',
               existing_nullable=False)
    op.drop_index('ix_order_info_t_user_id', table_name='order_info_t')
    op.drop_column('order_info_t', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_info_t', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='用户id'))
    op.create_index('ix_order_info_t_user_id', 'order_info_t', ['user_id'], unique=False)
    op.alter_column('enum_config', 'value',
               existing_type=mysql.VARCHAR(length=255),
               comment='枚举value数据',
               existing_comment='枚举value数据,一般映射成数字',
               existing_nullable=False)
    op.drop_column('enum_config', 'label')
    op.create_table('store_role_t',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('create_time', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='创建时间'),
    sa.Column('update_time', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True, comment='修改时间'),
    sa.Column('create_by', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='创建者id'),
    sa.Column('update_by', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='修改者id'),
    sa.Column('role_name', mysql.VARCHAR(length=256), nullable=True, comment='角色,翻译'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_store_role_t_role_name', 'store_role_t', ['role_name'], unique=False)
    op.drop_table('js_form')
    # ### end Alembic commands ###
