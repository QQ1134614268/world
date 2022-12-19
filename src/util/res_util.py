from flask import jsonify
from flask_sqlalchemy import Pagination

from config.enum_conf import ResponseCode


def success(data="success"):
    if isinstance(data, Pagination):
        if data.items and isinstance(data.items, list) and str(data.items[0]) == 'sqlalchemy.util._collections.result':
            data.items = [item._asdict() for item in data.items]
        return jsonify({
            "code": ResponseCode.SUCCESS.value,
            "data": data.items,
            "total": data.total,
            "page": data.page,
            "page_size": data.per_page,
        })
    if str(type(data)) == 'sqlalchemy.util._collections.result':
        return jsonify({
            "code": ResponseCode.SUCCESS.value,
            "data": data._asdict(),
        })

    return jsonify({
        "code": ResponseCode.SUCCESS.value,
        "data": data,
    })


def fail(data="", code=ResponseCode.FAIL.value):
    return jsonify({
        "code": code,
        "data": data,
    })


def exception(data=""):
    return jsonify({
        "code": ResponseCode.EXCEPTION.value,
        "data": data,
    })
