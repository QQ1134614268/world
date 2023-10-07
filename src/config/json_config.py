# -*- coding:utf-8 -*-
"""
@Time: 2021/3/14
@Description:
"""
import decimal
import json
import uuid
from datetime import date, datetime
from enum import Enum

from sqlalchemy.engine import Row

from config.conf import DATE_FORMAT, DATE_TIME_FORMAT
from config.log_conf import logger
from config.mysql_db import db


class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, db.Model):
            dic = o.__dict__
            if "_sa_instance_state" in dic:
                del dic["_sa_instance_state"]
            return dic
        if isinstance(o, Row):
            return dict(o)
        if isinstance(o, Enum):
            return o.name
        if isinstance(o, datetime):
            return o.strftime(DATE_TIME_FORMAT)
        if isinstance(o, date):
            return o.strftime(DATE_FORMAT)
        elif isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        try:
            return super().default(o)
        except:
            logger.error(f"自定义序列化失败,数据类型: {str(type(o))}")
            return str(o)
