# -- coding:UTF-8 --

from config.enum_conf import ExceptionCode


class WorldException(Exception):

    def __init__(self, message="Exception", code=ExceptionCode.FAIL.value):
        self.code = code
        self.message = message

    def __str__(self):
        return "code: %(code)d      message: %(message)s " % {'code': self.code, 'message': self.message}


class WorldNoLoginException(WorldException):

    def __init__(self, message="Exception", code=ExceptionCode.NO_LOGIN_FAIL.value):
        self.code = code
        self.message = message

    def __str__(self):
        return "code: %(code)d      message: %(message)s " % {'code': self.code, 'message': self.message}


if __name__ == '__main__':
    e = WorldException("err", 1)
    print(e)
    print(e.code)
