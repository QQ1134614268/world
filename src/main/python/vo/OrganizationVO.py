# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 15:41
# @Author  : huangran
"""
from sqlalchemy import Column, String, Integer

from vo.BaseModel import BaseTable


class OrganizationVO(BaseTable):
    __tablename__ = 'organization'
    parent_id = Column(Integer)
    name = Column(String(150), default='123456')
    level = Column(Integer, default=1)
    full_name = Column(String(70), default='default.jpg')
    full_path_code = Column(String(70), default='default.jpg')
    full_path_id = Column(String(70), default='default.jpg')
    code = Column(String(150), default='123456')
    leader = Column(Integer, default=1)


class OrganizationMemberRelationVO(BaseTable):
    __tablename__ = 'organization_member_relation'
    name = Column(String(150), default='123456')
    level = Column(String(70), default='default.jpg')
    full_name = Column(String(70), default='default.jpg')
    full_path = Column(String(70), default='default.jpg')
