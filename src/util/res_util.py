from flask import jsonify
from flask_sqlalchemy import Pagination

from config.enum_conf import ExceptionCode


def success(data="success"):
    return jsonify({
        "code": ExceptionCode.SUCCESS.value,
        "data": _handle(data),
    })


def fail(data="", code=ExceptionCode.FAIL.value):
    return jsonify({
        "code": code,
        "data": data,
    })


def exception(data=""):
    return jsonify({
        "code": ExceptionCode.EXCEPTION.value,
        "data": data,
    })


def _handle(data):
    if isinstance(data, Pagination):
        if isinstance(data.items, list) and data.items:
            tmp = []
            for item in data.items:
                if str(type(item)) == 'sqlalchemy.util._collections.result':
                    tmp.append(item._asdict())
                else:
                    tmp.append(item)
            data.items = tmp
    if str(type(data)) == 'sqlalchemy.util._collections.result':
        return data._asdict()

    return data


# todo
@DeprecationWarning
def page_success(data="success"):
    return jsonify({
        "code": ExceptionCode.SUCCESS.value,
        "data": data.items,
        "total": data.total,
        "page": data.page,
        "page_size": data.per_page,
    })
