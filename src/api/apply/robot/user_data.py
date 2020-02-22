# -*- coding:utf-8 -*-
from api.apply.robot.BuildData import create_data

wg = {
    "email": create_data("string", 10),
    "password": "123456",
    "username": "wg"
}
test = {
    "email": create_data("string", 10),
    "password": "123456",
    "username": "test"
}

zero = {
    "email": create_data("string", 10),
    "password": "123456",
    "username": "zero"
}

ran = {
    "email": create_data("string", 10),
    "password": "123456",
    "username": "ran"
}