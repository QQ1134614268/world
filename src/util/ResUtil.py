# from util.LogUtil import logger
# from api.user.UserService import get_id_by_token


def success(data):
    return {
        "code": 1,
        "data": data,
        "message": ""
    }


def fail(message):
    return {
        "code": 2,
        "data": "",
        "message": message
    }
