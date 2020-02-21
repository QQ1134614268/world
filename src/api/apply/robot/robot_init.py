# -*- coding:utf-8 -*-
from .action import register
from .data import wg, zero, ran, test


def register_init():
    register(wg)
    register(zero)
    register(ran)
    register(test)
