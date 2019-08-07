# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 16:05
# @Author  : huangran
"""
from db.db import db


class AreaVO(db.Model):
    __tablename__ = 'area'  # 起表名
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment="主键")
    name = db.Column(db.String(150), default='123456')
    level = db.Column(db.String(70), default='default.jpg')
    position = db.Column(db.String(70), default='default.jpg')
    createTime = db.Column(db.DateTime)


class AreaMemberRelationVO(db.Model):
    __tablename__ = 'area_member_relation'  # 起表名
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment="主键")
    areaId = db.Column(db.String(150), default='123456')
    userId = db.Column(db.String(70), default='default.jpg')
    createTime = db.Column(db.DateTime)
