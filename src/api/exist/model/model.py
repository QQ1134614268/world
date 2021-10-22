# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""

from sqlalchemy import Column, Text, String, Integer, ForeignKey

from vo.table_model import BaseTable


class ObjectVO(BaseTable):  # 定义 概念 对象
    __tablename__ = 'object_vo'
    # create_time = Column(DateTime, default=datetime.datetime.now)
    # update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    # create_user = db.Column(db.Integer,
    id = Column(Integer, default='', primary_key=True, comment="主键")
    content = Column(Text, default='')


class ModelVO(BaseTable):
    __tablename__ = 'model_t'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    path = Column(String(70), default='/')
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)


class ProveVO(BaseTable):
    __tablename__ = 'prove_vo'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    parent_id = Column(Integer)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)


class StoryVO(BaseTable):
    __tablename__ = 'story_vo'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    parent_id = Column(Integer)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)
