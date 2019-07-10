# encoding: utf-8
"""
@author:huangran
"""
from flask import Blueprint, jsonify, make_response
import time
from utity import date_utity
from config import res
from config import log

hello_api = Blueprint("hello", __name__, url_prefix='/hello')


@hello_api.route('/hello', methods=["GET"])
def hello():
    log.info("hello")
    return make_response(jsonify(res.success("hello world!")), 200)


@hello_api.route('/sleep', methods=["GET"])
def sleep():
    start = date_utity.get_defalut_time_str()
    time.sleep(30)
    end = date_utity.get_defalut_time_str()
    return make_response(jsonify(res.success('thread test;I slept from ' + start + " to " + end)), 200)


@hello_api.route('/exception', methods=["GET"])
def exception():
    result = 1 / 0
    return make_response(jsonify(res.success(result)), 200)
