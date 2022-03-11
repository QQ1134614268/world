# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, Integer, Text

from vo.table_model import BaseTable


class ProveVO(BaseTable):
    __tablename__ = 'prove_vo'
    userId = Column(Integer, index=True, comment='用户id')
    parent_id = Column(Integer, default=0, comment='父级id')
    value = Column(Text, default='', comment='内容')
    sort = Column(Integer, comment='排序顺序')
    wight = Column(Integer, default=1, comment='权重')


class StoryVO(BaseTable):
    __tablename__ = 'story_vo'
    userId = Column(Integer, index=True, comment='用户id')
    parent_id = Column(Integer, comment='父级id')
    value = Column(Text, default='', comment='内容')
    sort = Column(Integer, comment='排序顺序')
    wight = Column(Integer, default=1, comment='权重')
