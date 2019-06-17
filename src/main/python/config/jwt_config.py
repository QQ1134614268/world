"""
@author:huangran
"""
import jwt

secret = 'secret'  #配置文件


def get_token(payload):
    return jwt.encode(payload, secret, algorithm='HS256')


def get_payload(token):
    return jwt.decode(token, secret, algorithms=['HS256'])


def check_token(token):
    payload = get_payload(token)
    # 校验 token TODO

    return True
