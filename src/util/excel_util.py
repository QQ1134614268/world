# -*- coding:utf-8 -*-
"""
@Time: 2021/12/26
@Description:
"""
import os
from datetime import datetime

from openpyxl import load_workbook, Workbook

from config.conf import DATE_FORMAT, RESOURCE_DIR, world_env
from config.exception import WorldException
from config.mysql_db import db


# todo 优化整体


class Convert:
    # 读取excel类型 empty string number date boolean Error
    def __init__(self, nullable=False, max_length=20, comment="姓名", index=None, default=None):
        self.nullable = nullable
        self.max_length = max_length
        self.comment = comment
        self.index = index
        self.default = default

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
        return datetime.strptime(value, DATE_FORMAT)


class FloatConvert(Convert):

    @staticmethod
    def convert(value, **kwargs):
        if value is None:
            if not kwargs.get("nullable"):
                raise WorldException("转换类型异常")
            return kwargs.get("default")
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


class Field:
    def __init__(self, convert_handle: Convert, nullable=False, min_length=0, max_length=20, comment=None, index=None,
                 default=None):
        self.convert_handle = convert_handle
        self.comment = comment
        self.nullable = nullable
        self.min_length = min_length
        self.max_length = max_length
        self.index = index
        self.default = default

    def convert(self, value):
        return self.convert_handle.convert(value, nullable=self.nullable, max_length=self.max_length,
                                           default=self.default)


class ExcelExceptionMsg:
    pass


def check_excel_type(file_name):
    arr = file_name.split(".")
    file_type = arr and arr[-1]
    if file_type not in ["xlsx", "xls"]:
        raise WorldException("上传文件格式不正确!")


class ExcelHandler:

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
    def to_file(cls, data=[], cla_type=None, ):
        wb = Workbook()
        ws = wb.active
        attr_map = cls.get_attr_map(cla_type)
        for index, attr in enumerate(attr_map.items()):
            ws.cell(row=1, column=(index + 1)).value = attr[1].comment
        for row_index, item in enumerate(data):
            for col_index, attr in enumerate(attr_map.items()):
                if isinstance(item, dict):
                    ws.cell(row=(row_index + 2), column=(col_index + 1)).value = item.get(attr[0])
                if isinstance(item, db.Model):
                    ws.cell(row=(row_index + 2), column=(col_index + 1)).value = getattr(item, attr[0])
        return wb


if __name__ == '__main__':
    class User:
        name = Field(StrConvert, nullable=False, max_length=20, comment="姓名", index=1)
        sex = Field(StrConvert, nullable=False, max_length=20, comment="性别", index=2)
        birthday = Field(DateConvert, nullable=False, max_length=20, comment="生日", index=3)
        # pay = Field(FloatConvert, nullable=False, max_length=20, comment="薪资", index=3)


    path = os.path.join(RESOURCE_DIR, "excel_download_test.xlsx")
    dic_list = ExcelHandler.from_file(fp=path, cla_type=User)
    print(dic_list)
    # vos2 = [User(**dic) for dic in dic_list]
    wb2 = ExcelHandler.to_file(data=dic_list, cla_type=User)
    wb2.save(os.path.join(world_env.log_dir, "test_excel_output.xlsx"))
