# -*- coding:utf-8 -*-
"""
@Time: 2022/9/22
@Description:
"""
from os import path

from env_default import DATA_DIR

ROOT_DIR = path.abspath(path.dirname(__file__))
RESOURCE_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "resource")

LOG_DIR = path.join(DATA_DIR, "log")
UPLOAD_FILE_PATH = path.join(DATA_DIR, "upload")
UPLOAD_FILE_PATH2 = path.join(DATA_DIR, "upload_file")
VIDEO_FILE_PATH = path.join(DATA_DIR, "video")
UPLOAD_FILE_DIR_NAME = "/upload_file/"
