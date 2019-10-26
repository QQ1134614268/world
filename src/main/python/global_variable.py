import argparse
import configparser
from os import path

ROOT_DIR = path.abspath(__file__)
RESOURCE_DIR = path.dirname(path.dirname(ROOT_DIR)) + "/resource"


def get_parser_args_mode():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--mode', type=str, default=None)
    args = parser.parse_args()
    return args.mode


MODE = get_parser_args_mode()


def get_config_values(section, option):
    config = configparser.ConfigParser()
    config.read(RESOURCE_DIR + "/config.ini", encoding="utf-8")
    return config.get(section=section, option=option)


LOG_PATH = get_config_values("world", "LOG_PATH")
UPLOAD_FILE_PATH = get_config_values("world", "UPLOAD_FILE_PATH")
MAIL_TO = get_config_values("world", "MAIL_TO")
SERVER_MAIL = get_config_values("world", "SERVER_MAIL")
SERVER_MAIL_HOST = get_config_values("world", "SERVER_MAIL_HOST")
SERVER_MAIL_PASS = get_config_values("world", "SERVER_MAIL_PASS")
APPID = get_config_values("world", "APPID")
ALI_PAY_AES_KEY = get_config_values("world", "ALI_PAY_AES_KEY")
