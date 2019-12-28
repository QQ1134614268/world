# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/6 18:50
# @Author  : huangran
"""
import datetime

from sqlalchemy import Column, String, BIGINT, Integer, DateTime, Sequence

from db.db import db


# gmt_modify = Column(TIMESTAMP(True), nullable=False, server_default=func.now(), onupdate=func.now())


class BaseTable(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(BIGINT, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.datetime.now)


class ProjectConfig(BaseTable):
    __tablename__ = 'project_config'
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))


class EnumConfig(BaseTable):
    __tablename__ = 'enum_config'
    name = Column(String(50), nullable=False, index=True)
    identity = Column(String(50), unique=True)
    value = Column(String(50))
    sort = Column(Integer, Sequence('sort_seq'))
    note = Column(String(50))
