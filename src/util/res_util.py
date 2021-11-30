from flask import jsonify

from config.enum_conf import ExceptionCode


def success(data="success"):
    return {
        "code": ExceptionCode.SUCCESS.value,
        "data": data,
    }


def page_success(data="success"):
    return {
        "code": ExceptionCode.SUCCESS.value,
        "data": data.items,
        "total": data.total,
        "page": data.page,
        "page_size": data.per_page,
    }


def json_success(data="success"):
    return jsonify({
        "code": ExceptionCode.SUCCESS.value,
        "data": data,
    })


def fail(data=""):
    return {
        "code": ExceptionCode.FAIL.value,
        "data": data,
    }


def exception(data=""):
    return {
        "code": ExceptionCode.EXCEPTION.value,
        "data": data,
    }
