# -*- coding:utf-8 -*-
"""
@Time: 2021/12/26
@Description:
"""
from datetime import datetime

from openpyxl import load_workbook, Workbook

from config.exception import WorldException
from util import time_util


class Convert:
    # 读取excel类型
    # empty
    # string
    # number
    # date
    # boolean
    # Error
    def __init__(self, nullable=False, max_length=20, comment="姓名", index=None):
        self.nullable = nullable
        self.max_length = max_length
        self.comment = comment
        self.index = index

    @staticmethod
    def convert(value):
        return value


class DateConvert(Convert):

    @staticmethod
    def convert(value, **kwargs):
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        return time_util.get_datetime_by_str(value)


class FloatConvert(Convert):

    @staticmethod
    def convert(value, **kwargs):
        if value is None:
            return None
        if isinstance(value, float):
            return value
        return float(value)


class StrConvert(Convert):
    # , nullable = True
    @staticmethod
    def convert(value, **kwargs):
        # nullable = False, max_length = 20, comment = "姓名", index = None
        if value is None:
            return None
        if isinstance(value, str):
            return value
        return str(value)


# todo 重要
class Field:
    def __init__(self, convert_handle: Convert, nullable=False, max_length=20, comment="姓名", index=None):
        self.convert_handle = convert_handle
        self.comment = comment
        self.nullable = nullable
        self.max_length = max_length
        self.index = index

    def convert(self, value):
        return self.convert_handle.convert(value, nullable=self.nullable, max_length=self.max_length)


class User:
    name = Field(StrConvert, nullable=False, max_length=20, comment="姓名", index=1)
    sex = Field(StrConvert, nullable=False, max_length=20, comment="性别", index=2)
    birthday = Field(DateConvert, nullable=False, max_length=20, comment="生日", index=3)
    # pay = Field(FloatConvert, nullable=False, max_length=20, comment="薪资", index=3)


class ExcelExceptionMsg:
    pass


def check_excel_type(file_name):
    arr = file_name.split(".")
    file_type = arr and arr[-1]
    if file_type not in ["xlxs", "xls"]:
        raise WorldException("上传文件格式不正确!")


class ExcelHandler:
    # [姓名,生日]
    # 字段 field
    # convert
    # 赋值

    @staticmethod
    def get_sheet(fp=None):
        return load_workbook(fp).active

    @staticmethod
    def get_cn_en(cla_type=None):
        cn_en = {}
        for attr, field in cla_type.__dict__.items():
            if isinstance(field, Field):
                cn_en[field.comment] = attr
        return cn_en

    @staticmethod
    def get_cn(cla_type=None):
        cn_en = []
        for attr, field in cla_type.__dict__.items():
            if isinstance(field, Field):
                cn_en.insert(field.index, field.comment)
                # cn_en[field.index] = field.comment
        return cn_en

    @staticmethod
    def get_attr_map(cla_type=None):
        attr_map = {}
        for attr, field in cla_type.__dict__.items():
            if isinstance(field, Field):
                attr_map[attr] = field
        return attr_map

    @classmethod
    def get_excel_header(cls, rows):
        headers = []
        for row in rows:
            for cell in row:
                headers.append(cell.value)
            break
        return headers

    @classmethod
    def from_file(cls, fp=None, cla_type=None):
        errmsg = []
        ret = []
        sheet = cls.get_sheet(fp)
        rows = sheet.iter_rows()
        if sheet.max_row < 2:
            raise WorldException("没有数据")
        excel_header = cls.get_excel_header(rows)
        obj_header = cls.get_cn(cla_type)
        if excel_header != obj_header:
            raise WorldException(obj_header)  # todo
        attr_map = cls.get_attr_map(cla_type)
        for row_index, row in enumerate(rows):
            row_data = {}
            for col_index, attr_key in enumerate(attr_map.keys()):
                field = attr_map.get(attr_key)
                col_index = field.index or col_index
                cell = row[col_index - 1]
                try:
                    value = field.convert(cell.value)
                    row_data[attr_key] = value
                except Exception as e:
                    errmsg.append(f"{row_index + 2}行{col_index + 1}列, 值有问题")
            ret.append(row_data)
        if errmsg:
            raise WorldException(errmsg)
        return ret

    @classmethod
    def to_file(cls, vos=[], cla_type=None, ):
        wb = Workbook()
        ws = wb.active
        attr_map = cls.get_attr_map(cla_type)
        for index, attr in enumerate(attr_map.items()):
            ws.cell(row=1, column=(index + 1)).value = attr_map.get(attr).get("comment")

        for row_index, vo in enumerate(vos):
            for col_index, attr in enumerate(attr_map.items()):
                ws.cell(row=(row_index + 2), column=(col_index + 1)).value = getattr(vo, attr)
        return wb


if __name__ == '__main__':
    path = r'E:\world\resource\excel_download_test.xlsx'
    print(ExcelHandler.from_file(fp=path, cla_type=User))
