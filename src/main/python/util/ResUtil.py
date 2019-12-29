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
