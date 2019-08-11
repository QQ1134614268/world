# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 16:05
# @Author  : huangran
"""

from db import db
from vo.BaseModel import BaseTable


class AuthVO(BaseTable):
    __tablename__ = 'Auth'  # 起表名
    auth_path = db.Column(db.String(150), default='123456')
    user_id = db.Column(db.INT, default='123456')
