"""
@author:huangran
"""
import jwt
from flask import request

secret = 'secret'  # 配置文件


def get_token(payload):
    return jwt.encode(payload, secret, algorithm='HS256')


def get_payload(token):
    return jwt.decode(token, secret, algorithms=['HS256'])


def get_current_username():
    token = request.headers.get("token")
    return get_payload(token)["username"]


def check_token(token):
    payload = get_payload(token)
    # 校验 token TODO

    return True
