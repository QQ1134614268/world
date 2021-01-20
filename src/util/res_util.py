def success(data="success"):
    return {
        "code": 1,
        "data": data,
    }


def fail(data=""):
    return {
        "code": 2,
        "data": data,
    }


def err(data=""):
    return {
        "code": 4,
        "data": data,
    }
