# -*- coding:utf-8 -*-
"""
@Time: 2022/12/8
@Description:
"""
import os

import sys

from config.dir_conf import RESOURCE_DIR
from util import file_util

DIR = "DATA_DIR"

env_file_path = len(sys.argv) and sys.argv[0] or os.path.join(RESOURCE_DIR, "yaml_env_default.yaml")

env = file_util.FileUtil.from_yaml(env_file_path)

REDIS_PASSWORD1 = "REDIS_PASSWORD"

REDIS_DB1 = "REDIS_DB"

REDIS_PORT1 = "REDIS_PORT"

REDIS_HOST1 = "REDIS_HOST"

MONGO_PORT1 = "MONGO_PORT"

MONGO_HOST1 = "MONGO_HOST"

DB = "WORLD_DB"

PORT1 = "PORT"

HOST1 = "HOST"

PASSWORD1 = "PASSWORD"

USERNAME1 = "USERNAME"

SECRET1 = "SECRET"

MAIL_PASS = "SERVER_MAIL_PASS"

MAIL_PORT = "SERVER_MAIL_PORT"

MAIL_HOST = "SERVER_MAIL_HOST"

SERVER_MAIL1 = "SERVER_MAIL"

MAIL = "ZERO_MAIL"

S = "DEVELOPER_MAIL"

KEY = "PUBLIC_KEY"

HOST_BLOCK_LIST = "MAIL_HOST_BLOCK_LIST"

debug = "DEBUG"

DEBUG = env.get(debug, True)
DATA_DIR = env.get(DIR, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
MAIL_HOST_BLOCK_LIST = env.get(HOST_BLOCK_LIST, ["DESKTOP-4JJG0QE", "WGCOMPUTER", "DESKTOP-58DSV1D"])
PUBLIC_KEY = env.get(KEY, "world")
DEVELOPER_MAIL = env.get(S, "1134614268@qq.com")
ZERO_MAIL = env.get(MAIL, "1134614268@qq.com")
SERVER_MAIL = env.get(SERVER_MAIL1, "1134614268@qq.com")
SERVER_MAIL_HOST = env.get(MAIL_HOST, "smtp.qq.com")
SERVER_MAIL_PORT = env.get(MAIL_PORT, 465)
SERVER_MAIL_PASS = env.get(MAIL_PASS, "ijivowrottpbjfci")
SECRET = env.get(SECRET1, "secret")
USERNAME = env.get(USERNAME1, "wg")
PASSWORD = env.get(PASSWORD1, "123456")
HOST = env.get(HOST1, "127.0.0.1")  # 本地 dev
PORT = env.get(PORT1, 3306)
WORLD_DB = env.get(DB, "world")
MONGO_HOST = env.get(MONGO_HOST1, "127.0.0.1")
MONGO_PORT = env.get(MONGO_PORT1, 27017)
REDIS_HOST = env.get(REDIS_HOST1, "127.0.0.1")
REDIS_PORT = env.get(REDIS_PORT1, 6379)
REDIS_DB = env.get(REDIS_DB1, 0)
REDIS_PASSWORD = env.get(REDIS_PASSWORD1, 1234567890)
