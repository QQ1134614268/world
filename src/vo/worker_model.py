# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, Integer, String, Date, Enum, Float, UniqueConstraint

from config.enum_conf import SexEnum
from util.dev_util import get_comment
from vo.table_model import BaseTable


class WorkerVO(BaseTable):
    __tablename__ = 'worker_t'

    __table_args__ = {
        'mysql_engine': "InnoDB",
        'mysql_collate': 'utf8mb4_general_ci',
        'mysql_charset': 'utf8mb4',
        'comment': '工人详情',
    }
    belong = Column(Integer, )
    name = Column(String(255))
    birthday = Column(Date)
    id_card_number = Column(String(255))  # , unique=True
    # todo 优化 枚举 导入导出,vue 工人列表 表格
    sex = Column(Enum('男', '女'), comment=get_comment(SexEnum))
    pay = Column(Float(precision="10,2"), default=0, comment="日薪资(元)")

    # 10 总长度为10  2 小数点后保留2位
    start_time = Column(Date)
    phone = Column(String(11))

    UniqueConstraint(belong, id_card_number)


class WorkerTimeVO(BaseTable):
    __tablename__ = 'worker_time_t'
    __table_args__ = (UniqueConstraint('worker_id', 'date'),)
    date = Column(Date)
    worker_id = Column(Integer, index=True)
    morning = Column(Float(precision="10,2"), default=0, comment="上午工时(小时)")
    morning_area = Column(String(255))
    morning_content = Column(String(255))
    noon = Column(Float(precision="10,2"), default=0, comment="中午工时(小时)")
    noon_area = Column(String(255))
    noon_content = Column(String(255))
    afternoon = Column(Float(precision="10,2"), default=0, comment="下午工时(小时)")
    afternoon_area = Column(String(255))
    afternoon_content = Column(String(255))
    night = Column(Float(precision="10,2"), default=0, comment="晚上工时(小时)")
    night_area = Column(String(255))
    night_content = Column(String(255))
