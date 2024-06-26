"""empty message

Revision ID: 7a68e1d1dd73
Revises: 8f0ba34400e4
Create Date: 2022-08-21 22:58:39.128143

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a68e1d1dd73'
down_revision = '8f0ba34400e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_info_t',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True, comment='修改时间'),
    sa.Column('create_by', sa.Integer(), nullable=True, comment='创建者id'),
    sa.Column('update_by', sa.Integer(), nullable=True, comment='修改者id'),
    sa.Column('order_id', sa.Integer(), nullable=True, comment='订单id'),
    sa.Column('goods_id', sa.Integer(), nullable=True, comment='商品id'),
    sa.Column('goods_img', sa.String(length=256), nullable=True, comment='商品图片path'),
    sa.Column('goods_name', sa.String(length=256), nullable=True, comment='商品名'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='用户id'),
    sa.Column('num', sa.Integer(), nullable=True, comment='数量'),
    sa.Column('price', sa.Float(precision='14,2'), nullable=True, comment='价格(每个)'),
    sa.Column('cooker_status', sa.String(length=256), nullable=True, comment='是否做完菜'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_info_t_goods_id'), 'order_info_t', ['goods_id'], unique=False)
    op.create_index(op.f('ix_order_info_t_goods_name'), 'order_info_t', ['goods_name'], unique=False)
    op.create_index(op.f('ix_order_info_t_order_id'), 'order_info_t', ['order_id'], unique=False)
    op.create_index(op.f('ix_order_info_t_user_id'), 'order_info_t', ['user_id'], unique=False)
    op.drop_table('columns')
    op.drop_table('tables')
    op.add_column('order_t', sa.Column('total_price', sa.Float(precision='14,2'), nullable=True, comment='总价'))
    op.drop_index('ix_order_t_goods_id', table_name='order_t')
    op.drop_index('ix_order_t_goods_name', table_name='order_t')
    op.drop_index('ix_order_t_user_id', table_name='order_t')
    op.drop_column('order_t', 'num')
    op.drop_column('order_t', 'goods_img')
    op.drop_column('order_t', 'user_id')
    op.drop_column('order_t', 'cooker_status')
    op.drop_column('order_t', 'goods_name')
    op.drop_column('order_t', 'goods_id')
    op.drop_column('order_t', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_t', sa.Column('price', mysql.FLOAT(precision=14, scale=2), nullable=True, comment='价格(每个)'))
    op.add_column('order_t', sa.Column('goods_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='商品id'))
    op.add_column('order_t', sa.Column('goods_name', mysql.VARCHAR(length=256), nullable=True, comment='商品名'))
    op.add_column('order_t', sa.Column('cooker_status', mysql.VARCHAR(length=256), nullable=True, comment='是否做完菜'))
    op.add_column('order_t', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='用户id'))
    op.add_column('order_t', sa.Column('goods_img', mysql.VARCHAR(length=256), nullable=True, comment='商品图片path'))
    op.add_column('order_t', sa.Column('num', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='数量'))
    op.create_index('ix_order_t_user_id', 'order_t', ['user_id'], unique=False)
    op.create_index('ix_order_t_goods_name', 'order_t', ['goods_name'], unique=False)
    op.create_index('ix_order_t_goods_id', 'order_t', ['goods_id'], unique=False)
    op.drop_column('order_t', 'total_price')
    op.create_table('tables',
    sa.Column('TABLE_CATALOG', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('TABLE_SCHEMA', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('TABLE_NAME', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('TABLE_TYPE', mysql.ENUM('BASE TABLE', 'VIEW', 'SYSTEM VIEW'), nullable=True),
    sa.Column('ENGINE', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('VERSION', mysql.INTEGER(display_width=2), autoincrement=False, nullable=True),
    sa.Column('ROW_FORMAT', mysql.ENUM('Fixed', 'Dynamic', 'Compressed', 'Redundant', 'Compact', 'Paged'), nullable=True),
    sa.Column('TABLE_ROWS', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('AVG_ROW_LENGTH', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('DATA_LENGTH', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('MAX_DATA_LENGTH', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('INDEX_LENGTH', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('DATA_FREE', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('AUTO_INCREMENT', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('CREATE_TIME', mysql.TIMESTAMP(), nullable=True),
    sa.Column('UPDATE_TIME', mysql.DATETIME(), nullable=True),
    sa.Column('CHECK_TIME', mysql.DATETIME(), nullable=True),
    sa.Column('TABLE_COLLATION', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('CHECKSUM', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True),
    sa.Column('CREATE_OPTIONS', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('TABLE_COMMENT', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('TABLE_CATALOG', 'TABLE_SCHEMA', 'TABLE_NAME'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('columns',
    sa.Column('TABLE_CATALOG', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('TABLE_SCHEMA', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('TABLE_NAME', mysql.VARCHAR(length=64), nullable=False, comment='表名'),
    sa.Column('COLUMN_NAME', mysql.VARCHAR(length=64), nullable=False, comment='字段名'),
    sa.Column('ORDINAL_POSITION', mysql.INTEGER(display_width=10), autoincrement=False, nullable=True, comment='顺序?'),
    sa.Column('COLUMN_DEFAULT', mysql.TEXT(), nullable=True, comment='默认值'),
    sa.Column('IS_NULLABLE', mysql.VARCHAR(length=3), nullable=True, comment='是否可以None'),
    sa.Column('DATA_TYPE', mysql.LONGTEXT(), nullable=True, comment='数据类型'),
    sa.Column('CHARACTER_MAXIMUM_LENGTH', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True, comment='字符串最大长度?'),
    sa.Column('CHARACTER_OCTET_LENGTH', mysql.BIGINT(display_width=21), autoincrement=False, nullable=True, comment='?'),
    sa.Column('NUMERIC_PRECISION', mysql.BIGINT(display_width=10), autoincrement=False, nullable=True, comment='??'),
    sa.Column('NUMERIC_SCALE', mysql.BIGINT(display_width=10), autoincrement=False, nullable=True, comment='?'),
    sa.Column('DATETIME_PRECISION', mysql.INTEGER(display_width=10), autoincrement=False, nullable=True, comment='?'),
    sa.Column('CHARACTER_SET_NAME', mysql.VARCHAR(length=64), nullable=True, comment='?'),
    sa.Column('COLLATION_NAME', mysql.VARCHAR(length=64), nullable=True, comment='表名'),
    sa.Column('COLUMN_TYPE', mysql.MEDIUMTEXT(), nullable=True, comment='??'),
    sa.Column('COLUMN_KEY', mysql.ENUM('', 'PRI', 'UNI', 'MUL'), nullable=True, comment='??'),
    sa.Column('EXTRA', mysql.VARCHAR(length=256), nullable=True, comment='表名'),
    sa.Column('PRIVILEGES', mysql.VARCHAR(length=154), nullable=True, comment='表名'),
    sa.Column('COLUMN_COMMENT', mysql.TEXT(), nullable=True, comment='字段注释'),
    sa.Column('GENERATION_EXPRESSION', mysql.LONGTEXT(), nullable=True, comment='表名'),
    sa.Column('SRS_ID', mysql.INTEGER(display_width=10), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('TABLE_CATALOG', 'TABLE_SCHEMA', 'TABLE_NAME', 'COLUMN_NAME'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_order_info_t_user_id'), table_name='order_info_t')
    op.drop_index(op.f('ix_order_info_t_order_id'), table_name='order_info_t')
    op.drop_index(op.f('ix_order_info_t_goods_name'), table_name='order_info_t')
    op.drop_index(op.f('ix_order_info_t_goods_id'), table_name='order_info_t')
    op.drop_table('order_info_t')
    # ### end Alembic commands ###
