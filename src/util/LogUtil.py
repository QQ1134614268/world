# -*- coding: utf-8 -*-
import datetime
import json
import logging
import socket

from concurrent_log_handler import ConcurrentRotatingFileHandler

from config.conf import LOG_PATH
from util import file_util


def create_logger(file_path=LOG_PATH + "/log.json"):
    file_util.prepare_path(file_path)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # write log to file
    # handler = logging.FileHandler(file_path)
    handler = ConcurrentRotatingFileHandler(file_path, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf_8")
    handler.setLevel(logging.INFO)
    handler.setFormatter(JSONFormatter())
    # write log to console
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    handler_console.setFormatter(JSONFormatter())

    logger.addHandler(handler)
    logger.addHandler(handler_console)
    return logger


class JSONFormatter(logging.Formatter):
    REMOVE_ATTR = ["filename", "module", "exc_text", "created", "stack_info", "msecs", "relativeCreated", "exc_info",
                   "msg", "args", "levelno"]

    def format(self, record):
        extra = self.build_record(record)
        if record.args:
            extra['msg'] = "'" + record.msg + "'," + str(record.args).strip('()')
        else:
            extra['msg'] = record.msg
        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)
        if self._fmt == 'pretty':
            return json.dumps(extra, indent=2, ensure_ascii=False)
        else:
            return json.dumps(extra, ensure_ascii=False)

    @classmethod
    def build_record(cls, record):
        extra = {
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in cls.REMOVE_ATTR
        }
        extra['time'] = datetime.datetime.fromtimestamp(record.__dict__["created"]).strftime("%Y_%m_%d_%H_%M_%S_%f")
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
        except ConnectionError:
            host_name = "unknown hostname"
            host_ip = "unknown ip"
        extra['host_name'] = host_name
        extra['host_ip'] = host_ip
        return extra


logger = create_logger()

if __name__ == '__main__':
    logger.info({"a": 1})
    logger.error("Do something")
    logger.warning("Something maybe fail.")
