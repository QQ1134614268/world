from sqlalchemy import Column, Enum, String, Text, PrimaryKeyConstraint, TIMESTAMP, DateTime
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, MEDIUMTEXT

from src.config.mysql_db import db


class MysqlTables(db.Model):
    __tablename__ = 'tables'
    __bind_key__ = 'information_schema'
    TABLE_CATALOG = Column(String(64))
    TABLE_SCHEMA = Column(String(64))
    TABLE_NAME = Column(String(64))
    TABLE_TYPE = Column(Enum('BASE TABLE', 'VIEW', 'SYSTEM VIEW'))
    ENGINE = Column(String(64))
    VERSION = Column(INTEGER(2))
    ROW_FORMAT = Column(Enum('Fixed', 'Dynamic', 'Compressed', 'Redundant', 'Compact', 'Paged'))
    TABLE_ROWS = Column(BIGINT(21))
    AVG_ROW_LENGTH = Column(BIGINT(21))
    DATA_LENGTH = Column(BIGINT(21))
    MAX_DATA_LENGTH = Column(BIGINT(21))
    INDEX_LENGTH = Column(BIGINT(21))
    DATA_FREE = Column(BIGINT(21))
    AUTO_INCREMENT = Column(BIGINT(21))
    CREATE_TIME = Column(TIMESTAMP)
    UPDATE_TIME = Column(DateTime)
    CHECK_TIME = Column(DateTime)
    TABLE_COLLATION = Column(String(64))
    CHECKSUM = Column(BIGINT(21))
    CREATE_OPTIONS = Column(String(256))
    TABLE_COMMENT = Column(Text)
    PrimaryKeyConstraint(TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME)


class MysqlColumns(db.Model):
    __tablename__ = 'columns'
    __bind_key__ = 'information_schema'
    # __table_args__ = {
    #     'schema': 'information_schema'
    # }
    # __mapper_args__ = {
    #     'primary_key': []
    # }
    TABLE_CATALOG = Column('TABLE_CATALOG', String(64))
    TABLE_SCHEMA = Column('TABLE_SCHEMA', String(64))
    TABLE_NAME = Column('TABLE_NAME', String(64), comment="表名")
    COLUMN_NAME = Column('COLUMN_NAME', String(64), comment="字段名")
    ORDINAL_POSITION = Column('ORDINAL_POSITION', INTEGER(10), comment="顺序?")
    COLUMN_DEFAULT = Column('COLUMN_DEFAULT', Text, comment="默认值")
    IS_NULLABLE = Column('IS_NULLABLE', String(3), comment="是否可以None")
    DATA_TYPE = Column('DATA_TYPE', LONGTEXT, comment="数据类型")
    CHARACTER_MAXIMUM_LENGTH = Column('CHARACTER_MAXIMUM_LENGTH', BIGINT(21), comment="字符串最大长度?")
    CHARACTER_OCTET_LENGTH = Column('CHARACTER_OCTET_LENGTH', BIGINT(21), comment="?")
    NUMERIC_PRECISION = Column('NUMERIC_PRECISION', BIGINT(10), comment="??")
    NUMERIC_SCALE = Column('NUMERIC_SCALE', BIGINT(10), comment="?")
    DATETIME_PRECISION = Column('DATETIME_PRECISION', INTEGER(10), comment="?")
    CHARACTER_SET_NAME = Column('CHARACTER_SET_NAME', String(64), comment="?")
    COLLATION_NAME = Column('COLLATION_NAME', String(64), comment="表名")
    COLUMN_TYPE = Column('COLUMN_TYPE', MEDIUMTEXT, comment="??")
    COLUMN_KEY = Column('COLUMN_KEY', Enum('', 'PRI', 'UNI', 'MUL'), comment="??")
    EXTRA = Column('EXTRA', String(256), comment="表名")
    PRIVILEGES = Column('PRIVILEGES', String(154), comment="表名")
    COLUMN_COMMENT = Column('COLUMN_COMMENT', Text, comment="字段注释")
    GENERATION_EXPRESSION = Column('GENERATION_EXPRESSION', LONGTEXT, comment="表名")
    SRS_ID = Column('SRS_ID', INTEGER(10), comment="")
    PrimaryKeyConstraint(TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME)


class JsForm(db.Model):
    __bind_key__ = 'code'
    __tablename__ = 'js_form'
    __table_args__ = {
        'mysql_engine': "InnoDB",
        'mysql_collate': 'utf8mb4_general_ci',
        'mysql_charset': 'utf8mb4',
        'comment': 'js_form',
        'schema': 'code'
    }
    TABLE_CATALOG = Column(String(64))
    TABLE_SCHEMA = Column(String(64))
    TABLE_NAME = Column(String(64))
    COLUMN_NAME = Column(String(64))
    ORDINAL_POSITION = Column(String(64))
    COLUMN_DEFAULT = Column(String(64))
    IS_NULLABLE = Column(String(64))
    DATA_TYPE = Column(String(64))
    CHARACTER_MAXIMUM_LENGTH = Column(String(64))
    CHARACTER_OCTET_LENGTH = Column(String(64))
    NUMERIC_PRECISION = Column(String(64))
    NUMERIC_SCALE = Column(String(64))
    DATETIME_PRECISION = Column(String(64))
    CHARACTER_SET_NAME = Column(String(64))
    COLLATION_NAME = Column(String(64))
    COLUMN_TYPE = Column(String(64))
    COLUMN_KEY = Column(String(64))
    EXTRA = Column(String(64))
    PRIVILEGES = Column(String(64))
    COLUMN_COMMENT = Column(String(64))
    GENERATION_EXPRESSION = Column(String(64))
    SRS_ID = Column(String(64))
    PrimaryKeyConstraint(TABLE_CATALOG, TABLE_SCHEMA, COLUMN_NAME)

    name_cn = Column(String(64))
    data_type2 = Column(String(64))
    num_max = Column(String(64))
    num_min = Column(String(64))
    valid_regx = Column(String(64))
