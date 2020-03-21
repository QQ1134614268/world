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
        jwt_token = get_token(1, "wg")
    return jwt.decode(bytes(jwt_token, "utf_8"), SECRET, algorithms=['HS256'])
