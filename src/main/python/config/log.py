# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/30 21:29
# @Author  : huangran
"""
import logging
from logging.handlers import RotatingFileHandler


def crate():
    # formatter = '[%(asctime)s][%(filename)s] -- %(message)s'  # 日志格式
    # formatter_str = logging.Formatter('%(asctime)s -%(levelname)s -%(filename)s %(lineno)d -  %(message)s')
    formatter_str = '%(asctime)s -%(levelname)s -%(filename)s %(lineno)d -  %(message)s'  # 日志格式
    formatter = logging.Formatter(formatter_str)

    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
    rHandler = RotatingFileHandler("log3.txt", maxBytes=1 * 1024, backupCount=3)
    rHandler.setLevel(logging.INFO)
    rHandler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(rHandler)
    logger.addHandler(console)

    return logger


logger = crate()


def info(message):
    logger.info(message)


def error(message):
    logger.error(message)


def warning(message):
    logger.warning(message)


if __name__ == '__main__':
    info("Start print log")
    error("Do something")
    warning("Something maybe fail.")
