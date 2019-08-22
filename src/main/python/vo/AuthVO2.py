# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/23 2:47
"""
from sqlalchemy import Column, String, Integer

from vo.BaseModel import BaseTable


class AuthVO(BaseTable):
    __tablename__ = 'auth'
    user_id = Column(Integer)
    path = Column(String(150), default='/')
