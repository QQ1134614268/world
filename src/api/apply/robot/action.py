# -*- coding:utf-8 -*-
import requests

from .BuildData import create_data

host = "ggok.top"


def register(data):
    if not data:
        data = {
            "email": create_data("string", 10),
            "password": "123456",
            "username": "wg"
        }
    url = '/user/register'
    res = requests.post(host + url, json=data)
    print(res.json())  # 转为字典格式


def login(data):
    url = '/user/register'
    headers = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoicm9vdCIsImlkIjoxLCJ0aW1lc3RhbXAiOjE1NzcxMTc1NDJ9.-FKeKaMO9RIyAramv5HgGHAxxVfOEIiBSvpcSLfRp_w"}
    res = requests.post(host + url, json=data, headers=headers)
    print(res.json())  # 转为字典格式
