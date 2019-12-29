# -- coding:UTF-8 --
import time
from flask import request

from util.TokenUtil import get_payload, get_token


def get_name_by_token():
    jwt_token = request.headers.get("token")
    if not jwt_token:
        jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidyZnIiwiaWQiOjEsInRpbWVzdGFtcCI6MTU3Njc2Mzk3MH0.dnXajP3v7vetcGnTE-cQAnmYgpqHzxLuwuAVv2XZYF4"
    return get_payload(jwt_token)["name"]  # dict的缺点,直接取值,且需要明白之前存的数据


def get_id_by_token():
    jwt_token = request.headers.get("token")
    if not jwt_token:
        jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidyZnIiwiaWQiOjEsInRpbWVzdGFtcCI6MTU3Njc2Mzk3MH0.dnXajP3v7vetcGnTE-cQAnmYgpqHzxLuwuAVv2XZYF4"
    return get_payload(jwt_token)["id"]


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

    temp_user = {"name": "w&g", "id": 1, "timestamp": int(time.time())}
    str_token = get_token(temp_user)
    print()
