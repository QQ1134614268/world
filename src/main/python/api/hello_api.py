# encoding: utf-8
"""
@author:huangran
"""
from flask import Blueprint, Response
import time
from utity import date_utity

hello_api = Blueprint("hello", __name__, url_prefix='/hello')


@hello_api.route('/hello')
def hello():
    return 'hello world!'


@hello_api.route('/sleep')
def sleep():
    start = date_utity.get_datetime()
    time.sleep(30)
    end = date_utity.get_datetime()
    return 'thread test;I slept from ' + start + " to " + end
