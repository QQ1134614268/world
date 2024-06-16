from os import path

VERSION = "3.0.0"
JPG = ".jpg"
DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

SRC_DIR = path.abspath(path.dirname(path.dirname(__file__)))
RESOURCE_DIR = path.join(SRC_DIR, "resource")
