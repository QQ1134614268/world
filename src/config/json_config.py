# -*- coding:utf-8 -*-
"""
@Time: 2021/3/14
@Description:
"""
import dataclasses
import decimal
import json
import uuid
from datetime import date, datetime

from itsdangerous import json as _json
from sqlalchemy.engine import Row

from config.conf import DATE_FORMAT, DATE_TIME_FORMAT
from config.mysql_db import db


# app JSONEncoder ->itsdangerous.json -json
#

# 类变量是不会存储到 dict中，只有实例变量才可以
class JSONEncoder(_json.JSONEncoder):

    def default(self, o):
        #     todo  直接获取列名
        # o.table.cl
        if isinstance(o, db.Model):
            dic = o.__dict__
            if "_sa_instance_state" in dic:
                del dic["_sa_instance_state"]
            return dic
        if isinstance(o, Row):
            return dict(o)
        # if isinstance(o, Pagination):
        #     return {
        #         "data": o.items,
        #         "total": o.total,
        #         "page": o.page,
        #         "page_size": o.per_page,
        #     }
        if isinstance(o, datetime):
            return o.strftime(DATE_TIME_FORMAT)
        if isinstance(o, date):
            return o.strftime(DATE_FORMAT)
        if isinstance(o, uuid.UUID):
            return str(o)
        if dataclasses and dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return _json.JSONEncoder.default(self, o)


# todo
class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, db.Model):
            dic = o.__dict__
            if "_sa_instance_state" in dic:
                del dic["_sa_instance_state"]
            return dic
        if isinstance(o, datetime):
            return o.strftime(DATE_TIME_FORMAT)
        if isinstance(o, date):
            return o.strftime(DATE_FORMAT)
        elif isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        else:
            return super().default(o)
