# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/23 2:47
"""
from sqlalchemy import Column, String, Integer

from config.mysql_db import BaseTable


class AuthVO2(BaseTable):
    __tablename__ = 'auth2'
    user_id = Column(Integer)
    path = Column(String(150), default='/')
