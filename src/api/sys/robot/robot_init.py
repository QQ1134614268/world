# -*- coding:utf-8 -*-
import json

from api.sys.robot.action import register
from api.sys.robot.user_data import wg, zero, ran, test


def register_init():
    res = register(wg)
    print(json.loads(res.text))
    res = register(zero)
    print(json.loads(res.text))
    res = register(ran)
    print(json.loads(res.text))
    res = register(test)
    print(json.loads(res.text))


if __name__ == '__main__':
    register_init()
