# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, Integer, Text

from vo.table_model import BaseTable


class ProveVO(BaseTable):
    __tablename__ = 'prove_vo'
    userId = Column(Integer, index=True)
    parent_id = Column(Integer, default=0)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)


class StoryVO(BaseTable):
    __tablename__ = 'story_vo'
    userId = Column(Integer, index=True)
    parent_id = Column(Integer)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)