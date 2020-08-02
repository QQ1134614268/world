# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, Integer, Text

from config.mysql_db import BaseTable


class BTreeVO(BaseTable):
    __tablename__ = 'btree_t'
    fullPath = Column(String(70), default='/')
    value = Column(Text, default='')
    userId = Column(Integer)
    sort = Column(Integer)


class BTreeVO2(BaseTable):
    __tablename__ = 'btree2_t'
    parentId = Column(Integer)
    fullPath = Column(String(70), default='/')
    value = Column(Text, default='')
    userId = Column(Integer)
    sort = Column(Integer)
