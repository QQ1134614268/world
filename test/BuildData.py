# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/7 18:44

"""
import random

import time


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
