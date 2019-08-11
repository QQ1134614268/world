# -- coding:UTF-8 --
"""
@author:huangran
"""
import time

import jwt
from flask import request

secret = 'secret'  # 配置文件


def get_token(payload):
    return str(jwt.encode(payload, secret, algorithm='HS256'), "utf_8")


def get_payload(jwt_token):
    return jwt.decode(bytes(jwt_token, "utf_8"), secret, algorithms=['HS256'])


def get_payload_form_request():
    jwt_token = request.headers.get("token")
    return jwt.decode(bytes(jwt_token, "utf_8"), secret, algorithms=['HS256'])


def get_current_username():
    jwt_token = request.headers.get("token")
    if not jwt_token:
        temp_user = {"username": "w&g", "userid": 1, "timestamp": int(time.time())}
        jwt_token = get_token(temp_user)
    return get_payload(jwt_token)["username"]  # dict的缺点,直接取值,且需要明白之前存的数据


def get_current_userid():
    jwt_token = request.headers.get("token")
    # todo 临时的id
    if not jwt_token:
        temp_user = {"username": "w&g", "userid": 1, "timestamp": int(time.time())}
        jwt_token = get_token(temp_user)
    return get_payload(jwt_token)["userid"]


def check_token(jwt_token):
    payload = get_payload(jwt_token)
    # 校验 token TODO

    return True


if __name__ == '__main__':
    # info = {"username": "w&g", "userid": 1, "timestamp": int(time.time())}
    # token = jwt.encode(info, secret, algorithm='HS256')
    # print(type(token))
    # str_token = str(token, "utf_8")
    # print(str_token)
    # b_token = bytes(str_token, "utf_8")
    # print(b_token)
    # info2 = jwt.decode(b_token, secret, algorithms=['HS256'])
    # print(info2, type(info2))
    #
    # temp_user = {"username": "w&g", "userid": 1, "timestamp": int(time.time())}
    # jwt_token = str(get_payload(get_token(temp_user)))
    # print(jwt_token)

    # base64.b64encode( )
    # base64.b64decode( )
    # base64.encodestring()
    # base64.decodestring()
    # base64.decode()
    # base64.encode()

    temp_user = {"username": "w&g", "userid": 1, "timestamp": int(time.time())}
    str_token = get_token(temp_user)
    print()