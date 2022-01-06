# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, Integer, String, Float

from service.user_service import get_id_by_token
from vo.table_model import BaseTable


class WorksVO(BaseTable):
    __tablename__ = 'works_t'
    user_id = Column(Integer, index=True)
    describe = Column(String(255))
    file = Column(String(255))
    start = Column(Integer, default=0)
    thumbnail = Column(String(255))


class TargetVO(BaseTable):
    __tablename__ = 'target_t'
    user_id = Column(Integer, index=True, default=get_id_by_token)
    title = Column(String(255))
    content = Column(String(1000))
    price = Column(Float)