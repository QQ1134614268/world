# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/7 18:44

"""
import random
import string

from src.util.time_util import getUtcTimeStr


def create_data(datatype, length):
    if datatype == "String" or datatype == "string":
        return ''.join(random.sample(string.ascii_letters + string.digits, length))
    if datatype == "Time" or datatype == "time":
        return getUtcTimeStr()
    if datatype == "Int" or datatype == "int":
        return random.randint(10 ** (length - 1), 10 ** length - 1)
    if datatype == "Float" or datatype == "float":
        return float(random.randint(10 ** (length - 1), 10 ** length - 1) / 100)


if __name__ == '__main__':
    for i in range(1, 10):
        print(create_data("string", 10))
        print(create_data("time", 10))
        print(create_data("int", 10))
        print(create_data("float", 10))
