# -*- coding:utf-8 -*-
"""
@Time: 2022/12/8
@Description:
"""
import argparse
import os.path
from dataclasses import dataclass
from os import path
from urllib.parse import quote

import yaml

env = {}
world_env = None


# 类属性 todo
# @property  @dataclass name-tuple
@dataclass()
class WorldEnv:
    def __init__(self):
        self.data_dir = 1

    @staticmethod
    def init_env(args):
        # WorldEnv.__dict__.update(args)
        return WorldEnv().__dict__.update(args)

    data_dir: str
    debug: bool
    secret: str

    public_key: str

    sqlalchemy_database_uri: str
    log_dir: str
    upload_file_path: str
    upload_file_path2: str
    upload_file_dir_name: str
    mail_host_block_list: list

    # 邮件配置
    developer_mail: str
    zero_mail: str
    server_mail: str
    server_mail_host: str
    server_mail_port: str
    server_mail_pass: str

    # mysql配置
    username: str
    password: str
    host: str
    port: str
    world_db: str

    # mongo 配置
    mongo_host: str
    mongo_port: str

    # redis配置
    redis_host: str
    redis_port: str
    redis_db: str
    redis_password: str

    @property
    def sqlalchemy_database_uri(self):
        """获取用户名"""
        return f'mysql+mysqlconnector://{quote(USERNAME)}:{quote(PASSWORD)}@{HOST}:{PORT}/{WORLD_DB}?charset=utf8mb4'

    @property
    def log_dir(self):
        """获取用户名"""
        return path.join(DATA_DIR, "log")

    @property
    def upload_file_path(self):
        """获取用户名"""
        return path.join(DATA_DIR, "upload")

    @property
    def upload_file_path2(self):
        """获取用户名"""
        return path.join(DATA_DIR, "upload_file")

    @property
    def upload_file_dir_name(self):
        """获取用户名"""
        return "/upload_file/"


def get_config() -> dict:  # 转类

    parser = argparse.ArgumentParser()
    parser.add_argument('--worldConfig', '-c', help='配置文件位置')
    parser.add_argument('--worldMode', '-m', help='运行模式')
    parser.add_argument('--worldData', '-d', help='数据文件位置')
    cmd_args = parser.parse_args()

    env_file_path = cmd_args.worldConfig or "config/env.yaml"  # 运行时指定

    print(f"配置文件路径: {env_file_path}")

    if not os.path.isfile(env_file_path):
        raise Exception("配置文件不存在")
    with open(env_file_path, encoding="utf-8") as file:
        dict_value = yaml.load(file, Loader=yaml.FullLoader)
        env.update(dict_value)
    # if cmd_args.worldMode:
    #     env[debug] = cmd_args.worldMode
    if cmd_args.worldData:
        env["data_dir"] = cmd_args.worldData

    print("激活配置:", env)
    world_env = WorldEnv.init_env(env)


get_config()
DEBUG = world_env.debug
DATA_DIR = world_env.data_dir
MAIL_HOST_BLOCK_LIST = world_env.mail_host_block_list
PUBLIC_KEY = world_env.public_key
DEVELOPER_MAIL = world_env.developer_mail
ZERO_MAIL = world_env.zero_mail
SERVER_MAIL = world_env.server_mail
SERVER_MAIL_HOST = world_env.MAIL_HOST
SERVER_MAIL_PORT = world_env.MAIL_PORT
SERVER_MAIL_PASS = world_env.MAIL_PASS
SECRET = world_env.SECRET1
USERNAME = world_env.USERNAME1

PASSWORD = world_env.PASSWORD1
HOST = world_env.HOST1
PORT = world_env.PORT1
WORLD_DB = world_env.DB
MONGO_HOST = world_env.MONGO_HOST1
MONGO_PORT = world_env.MONGO_PORT1
REDIS_HOST = world_env.REDIS_HOST1
REDIS_PORT = world_env.REDIS_PORT1
REDIS_DB = world_env.REDIS_DB1
REDIS_PASSWORD = world_env.REDIS_PASSWORD1

SQLALCHEMY_DATABASE_URI = world_env.sqlalchemy_database_uri
LOG_DIR = world_env.log_dir
UPLOAD_FILE_PATH = world_env.upload_file_path
UPLOAD_FILE_PATH2 = world_env.upload_file_path2
UPLOAD_FILE_DIR_NAME = world_env.upload_file_dir_name
