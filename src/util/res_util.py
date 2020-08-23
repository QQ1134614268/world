def success(data="success"):
    return {
        "code": 1,
        "data": data,
        "message": ""
    }


def fail(message=""):
    return {
        "code": 2,
        "data": "",
        "message": message
    }


def err(message=""):
    return {
        "code": 4,
        "data": "",
        "message": message
    }
