# -*- coding: utf-8 -*-
"""
# @Time    : 2019/7/14 23:37
# @Author  : huangran
"""
import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf
