# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, Integer, String, Date, Enum, Float, UniqueConstraint

from vo.table_model import BaseTable


class WorkerVO(BaseTable):
    __tablename__ = 'worker_t'

    __table_args__ = {
        'mysql_engine': "InnoDB",
        'mysql_collate': 'utf8mb4_general_ci',
        'mysql_charset': 'utf8mb4',
        'comment': '工人详情',
    }
    belong = Column(Integer)
    name = Column(String(255))
    birthday = Column(Date)
    id_card_number = Column(String(255))  # , unique=True
    sex = Column(Enum('男', '女'))
    pay = Column(Float, default=0)
    start_time = Column(Date)
    phone = Column(String(11))

    UniqueConstraint(belong, id_card_number)


class WorkerTimeVO(BaseTable):
    __tablename__ = 'worker_time_t'
    __table_args__ = (UniqueConstraint('worker_id', 'date'),)
    date = Column(Date)
    worker_id = Column(Integer, index=True)
    morning = Column(Float, default=0)
    morning_area = Column(String(255))
    morning_content = Column(String(255))
    noon = Column(Float, default=0)
    noon_area = Column(String(255))
    noon_content = Column(String(255))
    afternoon = Column(Float, default=0)
    afternoon_area = Column(String(255))
    afternoon_content = Column(String(255))
    night = Column(Float, default=0)
    night_area = Column(String(255))
    night_content = Column(String(255))


class WorkerTimeVO2(BaseTable):
    # todo 上午 下午 晚上
    __tablename__ = 'worker_time_t2'
    __table_args__ = (UniqueConstraint('worker_id', 'date'),)
    date = Column(Date)
    time_type = Column(Enum('morning', 'noon', 'afternoon', 'night'))
    worker_id = Column(Integer, index=True)
    area = Column(String(255))
    content = Column(String(255))