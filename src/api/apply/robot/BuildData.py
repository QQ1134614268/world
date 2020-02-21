# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/7 18:44

"""
import random
import string

import time

from util.time_util import getTimeStr


def create_data(datatype, length):
    if datatype == "timestamp":
        value = time.time() * 1000
    else:
        value = random.randint(10 ** (length - 1), 10 ** length - 1)
        if datatype == "string":
            value = str(value)
        elif datatype == "float":
            value = float(value / 100)
    return value


def create_data2(datatype, length):
    if datatype == "String" or datatype == "string":
        return ''.join(random.sample(string.ascii_letters + string.digits, length))
    if datatype == "Time" or datatype == "time":
        return getTimeStr()
    if datatype == "Int" or datatype == "int":
        return random.randint(10 ** (length - 1), 10 ** length - 1)
    if datatype == "Float" or datatype == "float":
        return float(random.randint(10 ** (length - 1), 10 ** length - 1) / 100)


if __name__ == '__main__':
    for i in range(1, 10):
        print(create_data2("string", 10))
        print(create_data2("time", 10))
        print(create_data2("int", 10))
        print(create_data2("float", 10))
