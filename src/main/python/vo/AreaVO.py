# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 16:05
# @Author  : huangran
"""
from sqlalchemy import Column, String, Integer, DateTime

from vo.BaseModel import BaseTable


class AreaVO(BaseTable):
    __tablename__ = 'area'  # 起表名
    name = Column(String(150), default='123456')
    level = Column(String(70), default='default.jpg')
    position = Column(String(70), default='default.jpg')


class AreaMemberRelationVO(BaseTable):
    __tablename__ = 'area_member_relation'  # 起表名
    id = Column(Integer, autoincrement=True, primary_key=True, comment="主键")
    areaId = Column(String(150), default='123456')
    userId = Column(String(70), default='default.jpg')
