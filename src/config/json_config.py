# -*- coding:utf-8 -*-
"""
@Time: 2021/3/14
@Description:
"""
import dataclasses
import uuid
from datetime import date, datetime

from flask_sqlalchemy import Pagination
from itsdangerous import json as _json

from config.conf import DATE_FORMAT, DATE_TIME_FORMAT
from config.mysql_db import db
# 类变量是不会存储到 dict中，只有实例变量才可以
from util.log_util import logger


class JSONEncoder(_json.JSONEncoder):

    def default(self, o):
        #     todo  直接获取列名
        # o.table.cl
        if isinstance(o, db.Model):
            dic = o.__dict__
            if "_sa_instance_state" in dic:
                del dic["_sa_instance_state"]
            return dic
        if isinstance(o, Pagination):
            return {
                "page_data2": o.items,
                "page": o.page,
                "page_size": o.per_page,
                "total": o.total,
            }

        # if isinstance(o, ):
        #     return [dict(zip(item.keys(), item)) for item in o]
        # class 'sqlalchemy.util._collections.'>
        if isinstance(o, datetime):
            return o.strftime(DATE_TIME_FORMAT)
        if isinstance(o, date):
            return o.strftime(DATE_FORMAT)
        if isinstance(o, uuid.UUID):
            return str(o)
        if dataclasses and dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return _json.JSONEncoder.default(self, o)
