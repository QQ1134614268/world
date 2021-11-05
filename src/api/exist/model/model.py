# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""

from sqlalchemy import Column, Text, Integer, ForeignKey

from vo.table_model import BaseTable


class ProveVO(BaseTable):
    __tablename__ = 'prove_vo'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    parent_id = Column(Integer, default=0)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)
    #     name = Column(Text, default='')
    #     describe = Column(String(255), default='')
    #     data = Column(JSON)
    #     public = Column(Integer)
    #
    #     sort = Column(Integer)
    #     wight = Column(Float)
    #
    #     deleted = Column(Boolean, default=False)
    #
    #     parent_id = Column(Integer, default=0)
    #     user_id = Column(Integer)


class StoryVO(BaseTable):
    __tablename__ = 'story_vo'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    parent_id = Column(Integer)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)
