# -*- coding:utf-8 -*-
import json

from api.apply.robot import action
from api.apply.robot import user_data
from api.apply.robot.BuildData import create_data
from api.apply.robot.action import register


def robot1():
    # 注册(各种类别)-登录 -加好友 -发个人信息
    data = {
        "email": create_data("string", 10),
        "password": "123456",
        "username": create_data("string", 6),
    }
    res = register(data)
    print("1. 注册 -- ", json.loads(res.text))
    res = action.login({"password": "123456", "username": data["username"], "code": "zero"})
    print("2. 登陆 --", json.loads(res.text))
    res = json.loads(res.text)
    headers = {"token": res["data"]}
    res = action.getUserByName({"username": "wg"}, headers)
    print("3. 查找用户 --", json.loads(res.text))
    res = action.addAttention({"userId": json.loads(res.text).get("id"), "group": ""})
    print("4. 添加关注", json.loads(res.text))
    res = action.add_speech({"content": "I'm " + data["username"] + ",wg is my attention", "group": ""})
    print("5. 发表言论 --", json.loads(res.text))


def robot1_wg():
    res = action.login({"username": "wg", "password": "123456", "code": "zero"})
    print("1. 用户wg登陆 -- ", json.loads(res.text))
    headers = {"token": json.loads(res.text)["data"]}
    res = action.getUserByName({"username": "test"}, headers)
    print("2. wg查找test", json.loads(res.text))
    userId = json.loads(res.text).get("id")
    res = action.addAttention({"userId": userId, "group": ""}, headers)
    print("3. wg关注test", json.loads(res.text))
    res = action.add_speech({"content": "I'm " + user_data.wg["username"] + ",wg is my attention", "group": ""},
                            headers)
    print("4. wg发表言论", json.loads(res.text))
    mySpeechList = action.get_my_speech(headers)
    print("5. wg获取自己的言论", json.loads(mySpeechList.text))


if __name__ == '__main__':
    robot1()
    robot1_wg()
