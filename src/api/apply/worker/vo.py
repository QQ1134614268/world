# -*- coding:utf-8 -*-
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text

from vo.BaseModel import BaseTable
from vo.UserVO import UserVO


class WokerVO(BaseTable):
    __tablename__ = 'model_t'
    userId = Column(Integer, ForeignKey(UserVO.id), index=True)

