from flask import jsonify


def success(data="success"):
    return {
        "code": 1,
        "data": data,
    }


def page_success(data="success"):
    return {
        "code": 1,
        "data": data.items,
        "total": data.total,
        "page": data.page,
        "page_size": data.per_page,
    }


def json_success(data="success"):
    return jsonify({
        "code": 1,
        "data": data,
    })


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
