# -- coding:UTF-8 --
import datetime

import jwt
from flask import request

from config.env_default import world_env
from config.exception import WorldNoLoginException
from util import time_util
from util.time_util import get_now_str


def get_name_by_token():
    return get_payload().get("name", "Sys")


def get_id_by_token():
    return get_payload().get("id", -1)


def get_token(user_vo):
    payload = {
        "id": user_vo.id,
        "name": user_vo.username,
        "avatar": user_vo.avatar,
        "role": user_vo.role,
        "start_time": get_now_str(),
    }
    return jwt.encode(payload, world_env.secret, algorithm='HS256')


def get_payload():
    token_str = request.headers.get("token")
    if not token_str:
        return dict()
    try:
        return jwt.decode(bytes(token_str, "utf_8"), world_env.secret, algorithms=['HS256'])
    except:
        raise WorldNoLoginException("请重新登录")


def check_token():
    start_time = get_payload().get("start_time")
    if start_time:
        time = time_util.get_datetime_by_str(start_time)
        if time + datetime.timedelta(days=1) < time_util.get_now():
            return True
    return False
