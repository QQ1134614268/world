import os
from datetime import timedelta
from os import path

CONFIG_NAME_MAPPER = {
    'dev': 'dev_config.py',
    'prod': 'prod_config.py',
    'test': 'test_config.py'
}
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
MAIL_HOST_BLOCK_LIST = ["DESKTOP-4JJG0QE", "WGCOMPUTER"]
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
DIALCT = "mysql"
DRIVER = "mysqlconnector"
USERNAME = "wg"
PASSWORD = "123456"
HOST = "127.0.0.1"  # 本地 dev
# HOST = "ggok.top"  # 生产 ggok.top
PORT = 3306
DBNAME = "world"
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DBNAME)

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 1234567890


class Config:
    # todo 多环境
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # 定时任务配置
    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    # CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERYBEAT_SCHEDULE = {
        # ＃ 定义任务名称：import_data
        # ＃ 执行规则：每10秒运行一次
        'import_data': {
            'task': 'import_data',
            'schedule': timedelta(seconds=10)
        },
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
