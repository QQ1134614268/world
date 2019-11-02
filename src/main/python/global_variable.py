import argparse
import configparser
from os import path

ROOT_DIR = path.abspath(__file__)
RESOURCE_DIR = path.dirname(path.dirname(ROOT_DIR)) + "/resource"


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

    return RESOURCE_DIR + "/config.ini"


def get_config_values(section, option):
    config = configparser.ConfigParser()
    config.read(get_config_file_path(), encoding="utf-8")
    return config.get(section=section, option=option)


LOG_PATH = get_config_values("world", "LOG_PATH")
UPLOAD_FILE_PATH = get_config_values("world", "UPLOAD_FILE_PATH")
MAIL_TO = get_config_values("world", "MAIL_TO")
SERVER_MAIL = get_config_values("world", "SERVER_MAIL")
SERVER_MAIL_HOST = get_config_values("world", "SERVER_MAIL_HOST")
SERVER_MAIL_PASS = get_config_values("world", "SERVER_MAIL_PASS")
APPID = get_config_values("world", "APPID")
ALI_PAY_AES_KEY = get_config_values("world", "ALI_PAY_AES_KEY")
DEBUG = get_config_values("world", "DEBUG")
version = get_config_values("world", "version")

DIALCT = get_config_values("mysql", "DIALCT")
DRIVER = get_config_values("mysql", "DRIVER")
USERNAME = get_config_values("mysql", "USERNAME")
PASSWORD = get_config_values("mysql", "PASSWORD")
HOST = get_config_values("mysql", "HOST")
PORT = get_config_values("mysql", "PORT")
DBNAME = get_config_values("mysql", "DBNAME")
