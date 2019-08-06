# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/6 18:50
# @Author  : huangran
"""

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from datetime import datetime
from db.db import db


class BaseModel(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime)
    status = Column(Integer, default=1)

    # 初始化构造函数
    def __init__(self):
        self.addtime = datetime.now()
