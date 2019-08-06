# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 16:05
# @Author  : huangran
"""
from db.db import db


class AuthVO(db.Model):
    __tablename__ = 'Auth'  # 起表名
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment="主键")
    auth_path = db.Column(db.String(150), default='123456')
    user_id=db.Column(db.INT, default='123456')
    createTime = db.Column(db.DateTime)
