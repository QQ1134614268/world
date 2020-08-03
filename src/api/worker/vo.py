# -*- coding:utf-8 -*-
"""
@Time: 2020/8/2
@Description: 
"""
from sqlalchemy import Column, String, DateTime, Integer, Enum

from config.mysql_db import BaseTable


class WorkerVO(BaseTable):
    __tablename__ = 'worker_t'
    name = Column(String(255))
    birthday = Column(DateTime)
    id_card_number = Column(String(255))
    sex = Column(Enum('男', '女'))
    pay = Column(String(255))
    start_time = Column(DateTime)


class WorkerTimeVO(BaseTable):
    __tablename__ = 'worker_time_t'
    hours = Column(Integer)
