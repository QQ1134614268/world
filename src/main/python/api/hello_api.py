"""
@author:huangran
"""
from flask import Blueprint, Response

hello = Blueprint("hello", __name__, url_prefix='')


@hello.route('/hello')
def hello():
    return 'hello world!'
