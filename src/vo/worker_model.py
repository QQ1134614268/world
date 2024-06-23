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
    belong = Column(Integer, comment='所属id')
    name = Column(String(255), comment='姓名')
    birthday = Column(Date, comment='出生日期')
    id_card_number = Column(String(255), comment='身份证id')  # , unique=True
    # todo 优化 枚举 导入导出,vue 工人列表 表格
    sex = Column(Enum('男', '女'), comment=get_comment(SexEnum))
    pay = Column(Float(precision="12,4"), default=0, comment="日薪资(元)")  # 12: 总长度为12;  4: 小数点后保留4位
    start_time = Column(Date, comment='入职日期')
    phone = Column(String(11), comment='手机号')

    UniqueConstraint(belong, id_card_number)


class WorkerTimeVO(BaseTable):
    __tablename__ = 'worker_time_t'
    __table_args__ = (UniqueConstraint('worker_id', 'date'),)
    date = Column(Date, comment='日期')
    worker_id = Column(Integer, index=True, comment='工人id')
    # precision 小数点后精确度由数据库实现; SQL 标准中的 FLOAT 和 DOUBLE PRECISION 类型并不接受精度参数; 可替换为DECIMAL类型
    morning = Column(Float(precision=12), default=0, comment="上午工时(小时)")
    morning_area = Column(String(255), comment='上午工作地点')
    morning_content = Column(String(255), comment='上午工作内容')
    noon = Column(Float(precision=12), default=0, comment="中午工时(小时)")
    noon_area = Column(String(255), comment='中午工作地点')
    noon_content = Column(String(255), comment='中午工作内容')
    afternoon = Column(Float(precision=12), default=0, comment="下午工时(小时)")
    afternoon_area = Column(String(255), comment='下午工作地点')
    afternoon_content = Column(String(255), comment='下午工作内容')
    night = Column(Float(precision=12), default=0, comment="晚上工时(小时)")
    night_area = Column(String(255), comment='晚上工作地点')
    night_content = Column(String(255), comment='晚上工作内容')
