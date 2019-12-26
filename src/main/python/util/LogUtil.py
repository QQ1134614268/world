# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/30 21:29
# @Author  : huangran
"""
import logging
import os

from concurrent_log_handler import ConcurrentRotatingFileHandler

from global_variable import LOG_PATH


def crate():
    # formatter = '[%(asctime)s][%(filename)s] -- %(message)s'  # 日志格式
    # formatter_str = logging.Formatter('%(asctime)s -%(levelname)s -%(filename)s %(lineno)d -  %(message)s')
    formatter_str = '%(asctime)s -%(levelname)s -%(filename)s %(lineno)d -  %(message)s'  # 日志格式
    formatter = logging.Formatter(formatter_str)

    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
    # rHandler = RotatingFileHandler("log3.txt", maxBytes=1 * 1024, backupCount=3)
    log_filename = os.path.join(LOG_PATH, "log.txt")

    rHandler = ConcurrentRotatingFileHandler(log_filename, maxBytes=5 * 1024 * 1024, backupCount=3,
                                             encoding="utf_8")
    rHandler.setLevel(logging.INFO)
    rHandler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(rHandler)
    logger.addHandler(console)

    return logger


logger = crate()

if __name__ == '__main__':
    logger.info({"a": 1})
    logger.error("Do something")
    logger.warning("Something maybe fail.")
