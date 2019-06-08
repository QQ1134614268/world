"""
@author:huangran
"""


class WorldException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return "code: %(code)d      message: %(message)s " % {'code': self.code, 'message': self.message}


if __name__ == '__main__':
    e = WorldException(1, "ok")
    print(e)
    print(e.code)
