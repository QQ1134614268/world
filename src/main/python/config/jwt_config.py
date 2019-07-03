# -- coding:UTF-8 --
"""
@author:huangran
"""
import jwt
from flask import request
import time

secret = 'secret'  # 配置文件


def get_token(payload):
    return jwt.encode(payload, secret, algorithm='HS256')


def get_payload(token):
    return jwt.decode(token, secret, algorithms=['HS256'])


def get_current_username():
    token = request.headers.get("token")
    # 临时token
    if not token:
        token = get_payload({"username": "w&g", "userid": 1, "timestamp": int(time.time())})
    token=bytes(token, encoding="utf8")
    # token=
    # bytes 字符串,字典
    return get_payload(token)["username"]


def check_token(token):
    payload = get_payload(token)
    # 校验 token TODO

    return True

if __name__ == '__main__':
    info={"username": "w&g", "userid": 1, "timestamp": int(time.time())}
    token= jwt.encode(info, secret, algorithm='HS256')
    info2=jwt.decode(token, secret, algorithms=['HS256'])
    print( token,info2,type(token))