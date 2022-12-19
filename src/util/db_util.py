# -*- coding:utf-8 -*-
"""
@Time: 2021/11/26
@Description:
"""


def row_to_dic(res):
    return [dict(zip(item.keys(), item)) for item in res]
