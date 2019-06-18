"""
@author:huangran
"""
from flask import Blueprint, Response
hello = Blueprint("hello", __name__, url_prefix='/hello')


@hello.route('/hello')
def hello2():
    return 'hello world!'
