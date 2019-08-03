# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 15:41
# @Author  : huangran
"""
from db.db import db


class OrganizationVO(db.Model):
    __tablename__ = 'Organization'  # 起表名
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment="主键")
    name = db.Column(db.String(150), default='123456')
    level = db.Column(db.String(70), default='default.jpg')
    full_name = db.Column(db.BLOB(70), default='default.jpg')
    full_path = db.Column(db.BLOB(70), default='default.jpg')
    code = db.Column(db.String(150), default='123456')
    leader = db.Column(db.INT, default='default.jpg')
    createTime = db.Column(db.DateTime)


class OrganizationMemberRelationVO(db.Model):
    __tablename__ = 'OrganizationMemberRelation'  # 起表名
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment="主键")
    name = db.Column(db.String(150), default='123456')
    level = db.Column(db.String(70), default='default.jpg')
    full_name = db.Column(db.BLOB(70), default='default.jpg')
    full_path = db.Column(db.BLOB(70), default='default.jpg')
    createTime = db.Column(db.DateTime)
