# -*- coding:utf-8 -*-
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text

from config.mysql_db import BaseTable


# from vo.UserVO import UserVO
class ModelVO(BaseTable):
    __tablename__ = 'model_t'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    path = Column(String(70), default='/')
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)
