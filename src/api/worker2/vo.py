# -*- coding:utf-8 -*-
"""
@Time: 2020/8/2
@Description: 
"""
from sqlalchemy import *

from config.mysql_db import BaseTable


class WorkerTime(BaseTable):
    __tablename__ = 'worker_time_t2'
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(32))

    morning_start = Column(Time)
    morning_end = Column(Time)
    noon_start = Column(Time)
    noon_end = Column(Time)
    afternoon_start = Column(Time)
    afternoon_end = Column(Time)
    evening_start = Column(Time)
    evening_end = Column(Time)

    date = Column(Date)

    json_data = Column(JSON)
    json_data2 = Column(JSON)

    note = Column(String(255), server_default="123")
