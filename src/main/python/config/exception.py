"""
@author:huangran
"""
from flask import request, json
from werkzeug.exceptions import HTTPException


class WorldException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return "code: %(code)d      message: %(message)s " % {'code': self.code, 'message': self.message}


# 重写HTTPException异常中的get_body和get_headers方法,返回异常json格式
class APIException(HTTPException):

    # 重写父类的方法
    def get_body(self, environ=None):
        """Get the HTML body."""
        return json.dumps(dict(
            code=self.code,
            name=self.name,
            requert=request.method + ">>" + request.url,
            description=self.get_description(environ)
        ))

    # 重写父类的方法
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]


if __name__ == '__main__':
    e = WorldException(1, "ok")
    print(e)
    print(e.code)

# from werkzeug.exceptions import HTTPException
# from flask import json
# from flask import request
#
# from flask import current_app
#
# app=current_app
# @app.errorhandler(Exception)
# def flask_global_exception_handler(e):
#     # 判断异常是不是APIException
#     if isinstance(e, APIException):
#         return e
#     # 判断异常是不是HTTPException
#     elif isinstance(e, HTTPException):
#         error = APIException()
#         error.code = e.code
#         error.description = e.description
#         return error
#     # 异常肯定是Exception
#     else:
#         from flask import current_app
#         # 如果是调试模式,则返回e的具体异常信息。否则返回json格式的ServerException对象！
#         if current_app.config["DEBUG"]:
#             return e
#         else:
#                 return ServerException()
# #重写HTTPException异常中的get_body和get_headers方法,返回异常json格式
# class APIException(HTTPException):
#
#     # 重写父类的方法
#     def get_body(self, environ=None):
#         """Get the HTML body."""
#         return json.dumps(dict(
#             code= self.code,
#             name= self.name,
#             requert = request.method+">>"+request.url,
#             description= self.get_description(environ)
#         ))
#
#     #重写父类的方法
#     def get_headers(self, environ=None):
#         """Get a list of headers."""
#         return [('Content-Type', 'application/json')]
#
# class ServerException(APIException):
#     # 重写父类的属性
#     code = None
#     description = "server unknown error..."
