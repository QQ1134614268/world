# -*- coding:utf-8 -*-
"""
@Time: 2021/3/14
@Description:
"""
import dataclasses
import uuid
from datetime import date, datetime

from flask.json import JSONEncoder as _JSONEncoder
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import json as _json


# 类变量是不会存储到 dict中，只有实例变量才可以
class JSONEncoder(_JSONEncoder):

    def default(self, o):
        if isinstance(o, SQLAlchemy().Model):

            dict2 = o.__dict__
            if "_sa_instance_state" in dict2:
                del dict2["_sa_instance_state"]
            return dict2
            #     todo  直接获取列名
            o.table.cl

        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, uuid.UUID):
            return str(o)
        if dataclasses and dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return _json.JSONEncoder.default(self, o)
