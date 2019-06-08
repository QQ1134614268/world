"""
@author:huangran
"""


def success(data):
    return {
        "code": 1,
        "data": data,
        "message": ""
    }


def fail(message):
    return {
        "code": 1,
        "data": "",
        "message": message
    }
