"""
@author:huangran
"""
import os
import logging
import json
from logging.handlers import RotatingFileHandler

class Log:

    @staticmethod
    def get_log(path="logging.json", default_level=logging.INFO):
        if os.path.exists(path):
            with open(path, "r") as f:
                config = json.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
        return logging.getLogger()
    @staticmethod
    def get_log2(path="log.txt"):
        logger=logging.getLogger()
        formatter = logging.Formatter('%(asctime)s -%(levelname)s -%(filename)s %(lineno)d -  %(message)s')
        logger.setLevel(level=logging.INFO)
        # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
        file_handler = RotatingFileHandler(path, maxBytes=1 * 1024, backupCount=3)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        return logger

    @staticmethod
    def info(content):
        Log.get_log2().info(content)

    @staticmethod
    def err(position, title, content):
        logging.ERROR()
        pass

    @staticmethod
    def info_args(position, title, content):
        pass
