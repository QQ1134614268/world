# -*- coding:utf-8 -*-
"""
@Time: 2022/1/4
@Description:
"""
from util.excel_util import StrConvert, Field, FloatConvert, DateConvert


class WorkerExcelVO:
    name = Field(StrConvert, nullable=False, max_length=20, comment="姓名*", index=1)
    id_card_number = Field(StrConvert, nullable=False, max_length=20, comment="身份证", index=2)
    phone = Field(StrConvert, nullable=False, max_length=20, comment="电话", index=3)
    sex = Field(StrConvert, nullable=False, max_length=20, comment="性别", index=4)
    birthday = Field(DateConvert, nullable=False, max_length=20, comment="生日", index=5)
    start_time = Field(DateConvert, nullable=False, max_length=20, comment="入职日期", index=6)
    pay = Field(FloatConvert, nullable=False, comment="薪资*", index=7, default=0)
