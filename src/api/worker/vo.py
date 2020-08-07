# -*- coding:utf-8 -*-
"""
@Time: 2020/8/2
@Description: 
"""
from sqlalchemy import Column, String, DateTime, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

from config.mysql_db import BaseTable


class WorkerVO(BaseTable):
    __tablename__ = 'worker_t'
    belong = Column(Integer)
    name = Column(String(255))
    birthday = Column(DateTime)
    id_card_number = Column(String(255), unique=True)
    sex = Column(Enum('男', '女'))
    pay = Column(String(255))
    start_time = Column(DateTime)
    phone = Column(String(11))


class WorkerTimeVO(BaseTable):
    __tablename__ = 'worker_time_t'
    worker_id = Column(Integer, ForeignKey(WorkerVO.id), index=True)
    morning = Column(Integer, default=0)
    noon = Column(Integer, default=0)
    afternoon = Column(Integer, default=0)
    night = Column(Integer, default=0)
    hours = Column(Integer)
    date = Column(DateTime)
    worker = relationship(WorkerVO, backref='time', foreign_keys=[worker_id])
