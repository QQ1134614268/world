import configparser
from os import path

ROOT_DIR = path.abspath(__file__)
RESOURCE_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "resource")
# def get_config_file_path():
#     parser = argparse.ArgumentParser(description='manual to this script')
#     parser.add_argument('--mode', type=str, default=None)
#     args = parser.parse_args()
#     if args.mode:
#         file_path = RESOURCE_DIR + "/config-{}.ini".format(args.mode)
#     else:
#         file_path = RESOURCE_DIR + "/config.ini"
#     return file_path


def get_config_file_path():
    # parser = argparse.ArgumentParser(description='manual to this script')
    # parser.add_argument('--mode', type=str, default=None)
    # args = parser.parse_args()
    # if args.mode:
    #     file_path = RESOURCE_DIR + "/config-{}.ini".format(args.mode)
    # else:
    #     file_path = RESOURCE_DIR + "/config.ini"
    # return file_path
    # todo 参数与python manage.py db upgrade 产生冲突,,why?????
    #      python manage.py db upgrade 命令中的命令  怎么实现的?

    return path.join(RESOURCE_DIR, "config.ini")


config = configparser.ConfigParser()
config.read(get_config_file_path(), encoding="utf-8")

DEBUG = config.getboolean("world", "DEBUG")

LOG_PATH = config.get("world", "LOG_PATH")
UPLOAD_FILE_PATH = config.get("world", "UPLOAD_FILE_PATH")

MAIL_TO = config.get("world", "MAIL_TO")
SERVER_MAIL = config.get("world", "SERVER_MAIL")
SERVER_MAIL_HOST = config.get("world", "SERVER_MAIL_HOST")
SERVER_MAIL_PASS = config.get("world", "SERVER_MAIL_PASS")

APPID = config.get("world", "APPID")
ALI_PAY_AES_KEY = config.get("world", "ALI_PAY_AES_KEY")

VERSION = config.get("world", "VERSION")
ROBOT_HOST = config.get("world", "ROBOT_HOST")

SECRET = config.get("world", "SECRET")

DIALCT = config.get("mysql", "DIALCT")
DRIVER = config.get("mysql", "DRIVER")
USERNAME = config.get("mysql", "USERNAME")
PASSWORD = config.get("mysql", "PASSWORD")
HOST = config.get("mysql", "HOST")
PORT = config.get("mysql", "PORT")
DBNAME = config.get("mysql", "DBNAME")

MONGO_HOST = config.get("mongodb", "HOST")
MONGO_PORT = config.get("mongodb", "PORT")

REDIS_HOST = config.get("redis", "HOST")
REDIS_PORT = config.get("redis", "PORT")
REDIS_DB = config.get("redis", "REDIS_DB")
REDIS_PASSWORD = config.get("redis", "PASSWORD")
