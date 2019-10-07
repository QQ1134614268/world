# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/31 23:13
"""

from sqlalchemy import Column, Integer, Text

from vo.BaseModel import BaseTable


# 创建User模型
class XmindLikeVO(BaseTable):
    __tablename__ = 'x_mind_like'
    parent_id = Column(Integer)
    user_id = Column(Integer)
    content = Column(Text, default='')
    sort = Column(Integer)
