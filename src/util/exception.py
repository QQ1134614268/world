# -- coding:UTF-8 --
from flask import request, json
from werkzeug.exceptions import HTTPException


class WorldException(Exception):

    def __init__(self, message="Exception", code=0):
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
    e = WorldException("err", 1)
    print(e)
    print(e.code)
