# -*- coding:utf-8 -*-
"""
@Time: 2022/2/8
@Description:
"""
import argparse
import os
import os.path
from os import path
from urllib.parse import quote

import yaml

from config.conf import RESOURCE_DIR


class WorldEnv:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--config', '-c', help='配置文件位置')
        parser.add_argument('--active', '-m', help='运行模式')
        parser.add_argument('--worldData', '-d', help='数据文件位置')
        cmd_args, _ = parser.parse_known_args()

        if cmd_args.config:
            env_file_path = cmd_args.worldConfig  # 运行时指定
        elif cmd_args.active:
            env_file_path = os.path.join(RESOURCE_DIR, f"env.{cmd_args.active}.yaml")  # 运行时指定
        else:
            env_file_path = os.path.join(RESOURCE_DIR, "env.yaml")

        if not os.path.isfile(env_file_path):
            raise Exception(f"配置文件{env_file_path}不存在")

        with open(env_file_path, encoding="utf-8") as file:
            dict_value: dict = yaml.load(file, Loader=yaml.FullLoader)

        self.data_dir = dict_value.get("data_dir")
        self.debug = dict_value.get("debug")
        self.secret = dict_value.get("secret")

        self.public_key = dict_value.get("public_key")

        self.mail_host_block_list = dict_value.get("mail_host_block_list")

        # 邮件配置
        self.developer_mail = dict_value.get("developer_mail")
        self.zero_mail = dict_value.get("zero_mail")
        self.server_mail = dict_value.get("server_mail")
        self.server_mail_host = dict_value.get("server_mail_host")
        self.server_mail_port = dict_value.get("server_mail_port")
        self.server_mail_pass = dict_value.get("server_mail_pass")

        # mysql配置
        self.username = dict_value.get("username")
        self.password = dict_value.get("password")
        self.host = dict_value.get("host")
        self.port = dict_value.get("port")
        self.world_db = dict_value.get("world_db")
        # mongo 配置
        self.mongo_host = dict_value.get("mongo_host")
        self.mongo_port = dict_value.get("mongo_port")
        # redis配置
        self.redis_host = dict_value.get("redis_host")
        self.redis_port = dict_value.get("redis_port")
        self.redis_db = dict_value.get("redis_db")
        self.redis_password = dict_value.get("redis_password")

    @property
    def sqlalchemy_database_uri(self):
        """获取用户名"""
        return f'mysql+mysqlconnector://{quote(self.username)}:{quote(self.password)}@{self.host}:{self.port}/{self.world_db}?charset=utf8mb4'

    @property
    def log_dir(self):
        """获取用户名"""
        return path.join(self.data_dir, "log")

    @property
    def upload_file_path(self):
        """获取用户名"""
        return path.join(self.data_dir, "user_cloud_space")

    @property
    def upload_file_path2(self):
        """获取用户名"""
        return path.join(self.data_dir, "upload_file")

    @property
    def upload_file_dir_name(self):  # todo 待删除
        """获取用户名"""
        return "/upload_file/"


world_env = WorldEnv()
