# encoding: utf-8
"""
@author:huangran
"""
from flask import Blueprint, Response
hello_api = Blueprint("hello", __name__, url_prefix='/hello')


@hello_api.route('/hello')
def hello():
    return 'hello world!'
