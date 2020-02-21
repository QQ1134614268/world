# -*- coding:utf-8 -*-
from .data import wg
from .action import register

def robot1():
    # 注册(各种类别)-登录 -加好友 -发个人信息
    register()

def robot1_wg():
    import requests
    data = {"name": "张三", "age": 12}
    res = requests.post("http://127.0.0.1/hello_api/json_post", json=data)
    print(res.json())  # 转为字典格式
    headers = {"Content-Type": "application/json"}
    headers = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoicm9vdCIsImlkIjoxLCJ0aW1lc3RhbXAiOjE1NzcxMTc1NDJ9.-FKeKaMO9RIyAramv5HgGHAxxVfOEIiBSvpcSLfRp_w"}
    url = "/wb_api/add_blog"
