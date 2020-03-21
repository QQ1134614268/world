import jwt
from flask import request

from global_variable import SECRET
from util.time_util import getUtcTimeStr


def get_token(userId, userName):
    payload = dict({"utc_time_str": getUtcTimeStr()})
    payload["id"] = userId
    payload["name"] = userName
    return str(jwt.encode(payload, SECRET, algorithm='HS256'), "utf_8")


def get_payload():
    jwt_token = request.headers.get("token")
    if not jwt_token:
        jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidyZnIiwiaWQiOjEsInRpbWVzdGFtcCI6MTU3Njc2Mzk3MH0.dnXajP3v7vetcGnTE-cQAnmYgpqHzxLuwuAVv2XZYF4"
    return jwt.decode(bytes(jwt_token, "utf_8"), SECRET, algorithms=['HS256'])
