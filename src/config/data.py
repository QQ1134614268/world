# -*- coding:utf-8 -*-
"""
@Time: 2020/12/14
@Description: 
"""
from util.data_util import create_data

user_data = [
    {"email": create_data("string", 10), "password": "123456", "username": "wg"},
    {"email": create_data("string", 10), "password": "123456", "username": "test"},
    {"email": create_data("string", 10), "password": "123456", "username": "zero"},
    {"email": create_data("string", 10), "password": "123456", "username": "ran"}
]
user_data2 = [
    ["email", "password", "username"],
    [create_data("string", 10), "123456", "wg"],
    [create_data("string", 10), "123456", "test"],
    [create_data("string", 10), "123456", "zero"],
    [create_data("string", 10), "123456", "ran"],
]
store_data = [
    ["name", "password", ],
    ["发如雪", "123456", ],
]

