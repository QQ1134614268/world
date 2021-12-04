import datetime

import jwt
from flask import request

from config.conf import SECRET
from config.exception import WorldException
from util import time_util
from util.time_util import getUtcTimeStr


def get_token(userId, userName):
    payload = {"utc_time_str": getUtcTimeStr(), "id": userId, "name": userName}
    return str(jwt.encode(payload, SECRET, algorithm='HS256'), "utf_8")


def get_payload():
    jwt_token = request.headers.get("token")
    try:
        return jwt.decode(bytes(jwt_token, "utf_8"), SECRET, algorithms=['HS256'])
    except:
        raise WorldException("请重新登录")
        # jwt_token = get_token(1, "wg")
        # return jwt.decode(bytes(jwt_token, "utf_8"), SECRET, algorithms=['HS256'])


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


if __name__ == '__main__':
    print(get_token(1, 'wg'))
