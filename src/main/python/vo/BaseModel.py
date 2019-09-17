# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/6 18:50
# @Author  : huangran
"""
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey,Sequence
from sqlalchemy.orm import relationship  # 创建关系

from db.db import db
from util.DateUtils import get_utc_now

# gmt_modify = Column(TIMESTAMP(True), nullable=False, server_default=func.now(), onupdate=func.now())


class BaseTable(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=get_utc_now())
    status = Column(Integer)


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


class InnerVO(BaseTable):
    __tablename__ = 'inner'
    inner = Column(String(150), default='123456')


class ComplexVO(BaseTable):
    __tablename__ = 'complex'
    content = Column(String(150), default='123456')
    images = Column(String(70), default='default.jpg')
    inner_id = Column(Integer, ForeignKey("inner.id", ondelete='CASCADE'))
    inner_name = relationship("InnerVO", backref="inner_of_complex")
