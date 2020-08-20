# -*- coding:utf-8 -*-
"""
@Time: 2020/8/19
@Description: 
"""

from sqlalchemy import Column, String, Integer, Text, JSON, Boolean, Float

from config.mysql_db import BaseTable


class ClassVO(BaseTable):
    __tablename__ = 'class_t'
    name = Column(Text, default='')
    describe = Column(String(255), default='')
    data = Column(JSON)
    public = Column(Integer)

    sort = Column(Integer)
    wight = Column(Float)

    deleted = Column(Boolean, default=False)

    parent_id = Column(Integer, default=0)
    user_id = Column(Integer)
