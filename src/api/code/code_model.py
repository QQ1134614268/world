from sqlalchemy import Column, String, PrimaryKeyConstraint

from config.mysql_db import db


class JsForm(db.Model):
    # __bind_key__ = 'code'
    __tablename__ = 'js_form'
    __table_args__ = {
        'mysql_engine': "InnoDB",
        'mysql_collate': 'utf8mb4_general_ci',
        'mysql_charset': 'utf8mb4',
        'comment': 'js_form',
        # 'schema': 'code'
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
