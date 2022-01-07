from flask import jsonify

from config.enum_conf import ExceptionCode
from util.db_util import row_to_dic


def success(data="success"):
    return jsonify({
        "code": ExceptionCode.SUCCESS.value,
        "data": data,
    })


def page_success(data="success"):
    return jsonify({
        "code": ExceptionCode.SUCCESS.value,
        "data": data.items,
        "total": data.total,
        "page": data.page,
        "page_size": data.per_page,
    })


def page_success_row(data="success"):
    return jsonify({
        "code": ExceptionCode.SUCCESS.value,
        "data": row_to_dic(data.items),
        "total": data.total,
        "page": data.page,
        "page_size": data.per_page,
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
