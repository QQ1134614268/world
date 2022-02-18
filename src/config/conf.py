from os import path

# app.config.from_pyfile(config_name)

CONFIG_NAME_MAPPER = {
    'dev': 'dev_config.py',
    'prod': 'prod_config.py',
    'test': 'test_config.py'
}
DEBUG = True

DI = "2440024344@qq.com"

ROOT_DIR = path.abspath(path.dirname(__file__))
RESOURCE_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "resource")
DATA_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "data")
LOG_DIR = path.join(DATA_DIR, "log")

UPLOAD_FILE_PATH = path.join(DATA_DIR, "upload")
UPLOAD_FILE_PATH2 = path.join(DATA_DIR, "upload_file")
VIDEO_FILE_PATH = path.join(DATA_DIR, "video")

DEFAULT_TIME_STR = '%Y-%m-%d %H:%M:%S.%f'
# dev  不发邮件的主机
MAIL_HOST_BLOCK_LIST = ["DESKTOP-4JJG0QE", "WGCOMPUTER"]
DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
PUBLIC_KEY = "world"

MAIL_TO = "1134614268@qq.com"
SERVER_MAIL = "1134614268@qq.com"
SERVER_MAIL_HOST = "smtp.qq.com"
SERVER_MAIL_PORT = 465
SERVER_MAIL_PASS = "ragrmyytlnsuibih"

APPID = "2019082466418136"
ALI_PAY_AES_KEY = "U2LU6HVqOHkv7w7w5rZ2Ew=="

VERSION = "3.0.0"
ROBOT_HOST = "http://127.0.0.1"

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
