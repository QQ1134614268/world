import datetime

import jwt
from flask import request

from config.conf import SECRET
from config.exception import WorldNoLoginException
from util import time_util
from util.time_util import get_now_str


def get_token(user_id, user_name):
    payload = {"start_time": get_now_str(), "id": user_id, "name": user_name}
    return str(jwt.encode(payload, SECRET, algorithm='HS256'), "utf_8")


def get_payload():
    jwt_token = request.headers.get("token")
    try:
        return jwt.decode(bytes(jwt_token, "utf_8"), SECRET, algorithms=['HS256'])
    except:
        raise WorldNoLoginException("请重新登录")


def check_token():
    token = request.headers.get("token")
    if token:
        start_time = get_payload().get("start_time")
        time = time_util.get_datetime_by_str(start_time)
        if time + datetime.timedelta(days=1) < time_util.get_now():
            return True
    return False


if __name__ == '__main__':
    print(get_token(1, 'wg'))
