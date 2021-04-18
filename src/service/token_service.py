# -*- coding:utf-8 -*-
"""
@Time: 2021/4/18
@Description:
"""
from util.token_util import get_payload


def get_name_by_token():
    return get_payload()["name"]  # dict的缺点,直接取值,且需要明白之前存的数据


def get_id_by_token():
    return get_payload()["id"]