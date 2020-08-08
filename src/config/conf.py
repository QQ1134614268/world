from os import path

ROOT_DIR = path.abspath(path.dirname(__file__))
RESOURCE_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "resource")
DATA_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "data")
DEFAULT_TIME_STR = '%Y_%m_%d_%H_%M_%S_%f'

MAIL_HOST_BLOCK_LIST = ["DESKTOP-4JJG0QE"]

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
PUBLIC_KEY = "world"

LOG_PATH = "/web_data/world/log"
UPLOAD_FILE_PATH = "/web_data/world/file"

MAIL_TO = "1134614268@qq.com"
SERVER_MAIL = "1134614268@qq.com"
SERVER_MAIL_HOST = "smtp.qq.com"
SERVER_MAIL_PASS = "ragrmyytlnsuibih"

APPID = "2019082466418136"
ALI_PAY_AES_KEY = "U2LU6HVqOHkv7w7w5rZ2Ew=="

DEBUG = True

VERSION = "1.0.4"
ROBOT_HOST = "http://127.0.0.1"

SECRET = "secret"
DIALCT = "mysql"
DRIVER = "mysqlconnector"
USERNAME = "wg"
PASSWORD = 123456
HOST = "127.0.0.1"  # 生产 ggok.top
PORT = 3306
DBNAME = "world"

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 1234567890
