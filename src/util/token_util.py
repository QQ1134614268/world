import datetime

import jwt
from flask import request

from config.conf import SECRET
from util import time_util
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


def check_token():
    # todo jwt 校验
    token = request.headers.get("token")
    if token:
        utc_time_str = get_payload().get("utc_time_str")
        utc_datetime = time_util.getDatetimeByStr(utc_time_str)
        if utc_datetime + datetime.timedelta(days=1) < time_util.get_utc_now():
            return True
    # return False
    return True
