import os
from os import path

DEBUG = True

ROOT_DIR = path.abspath(path.dirname(__file__))
RESOURCE_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "resource")
DATA_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "data")
LOG_DIR = path.join(DATA_DIR, "log")

UPLOAD_FILE_PATH = path.join(DATA_DIR, "upload")
UPLOAD_FILE_PATH2 = path.join(DATA_DIR, "upload_file")
VIDEO_FILE_PATH = path.join(DATA_DIR, "video")

UPLOAD_FILE_DIR_NAME = "/upload_file/"
JPG = ".jpg"
DEFAULT_TIME_STR = '%Y-%m-%d %H:%M:%S.%f'
# dev  不发邮件的主机
MAIL_HOST_BLOCK_LIST = ["DESKTOP-4JJG0QE", "WGCOMPUTER", "DESKTOP-58DSV1D"]
DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
PUBLIC_KEY = "world"

DEVELOPER_MAIL = "1134614268@qq.com"
DI = "2440024344@qq.com"
ZERO_MAIL = "1134614268@qq.com"

SERVER_MAIL = "1134614268@qq.com"
SERVER_MAIL_HOST = "smtp.qq.com"
SERVER_MAIL_PORT = 465
SERVER_MAIL_PASS = "ijivowrottpbjfci"

VERSION = "3.0.0"

SECRET = "secret"
DIALECT = "mysql"
DRIVER = "mysqlconnector"
USERNAME = "wg"
PASSWORD = "123456"
HOST = "127.0.0.1"  # 本地 dev
# HOST = "ggok.top"  # 生产 ggok.top
PORT = 3306
WORLD_DB = "world"
INFORMATION_SCHEMA_DB = 'information_schema'
CODE_DB = 'information_schema'

SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{WORLD_DB}?charset=utf8mb4'
INFORMATION_SCHEMA_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{INFORMATION_SCHEMA_DB}?charset=utf8mb4'
CODE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{CODE_DB}?charset=utf8mb4'
SQLALCHEMY_BINDS = {
    'information_schema': INFORMATION_SCHEMA_URI,
    'code': CODE_URI,
}

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 1234567890


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret"

    SECRET = "secret"
    DIALECT = "mysql"
    DRIVER = "mysqlconnector"
    USERNAME = "wg"
    PASSWORD = "123456"
    HOST = "127.0.0.1"  # 本地 dev
    #
    PORT = 3306
    WORLD_DB = "world"
    INFORMATION_SCHEMA_DB = 'information_schema'
    CODE_DB = 'information_schema'

    SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{WORLD_DB}?charset=utf8mb4'
    INFORMATION_SCHEMA_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{INFORMATION_SCHEMA_DB}?charset=utf8mb4'
    CODE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{CODE_DB}?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        'information_schema': INFORMATION_SCHEMA_URI,
        'code': CODE_URI,
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    HOST = "ggok.top"  # 生产 ggok.top
    SQLALCHEMY_BINDS = {

    }


# todo 多环境
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
