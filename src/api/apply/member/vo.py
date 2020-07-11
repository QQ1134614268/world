# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, JSON

from vo.BaseModel import BaseTable


class ExistVO(BaseTable):
    __tablename__ = 'exist_t'
    path = Column(String(255))
    name = Column(String(255))
    data = Column(JSON)
    # userId = Column(Integer)
    # amount = Column(Float, default=0)
