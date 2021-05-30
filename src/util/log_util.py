# -*- coding: utf-8 -*-
import collections
import datetime
import json
import logging

from concurrent_log_handler import ConcurrentRotatingFileHandler

from config.conf import DEFAULT_TIME_STR
from config.conf import LOG_PATH
from util import file_util


def create_logger(file_path=LOG_PATH + "/log.json"):
    file_util.prepare_path(file_path)

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    # write log to file
    # handler = logging.FileHandler(file_path)
    handler = ConcurrentRotatingFileHandler(file_path, maxBytes=1 * 1024 * 1024, backupCount=10, encoding="utf_8")
    handler.setLevel(logging.INFO)
    handler.setFormatter(JSONFormatter())
    # write log to console
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    handler_console.setFormatter(JSONFormatter())

    log.addHandler(handler)
    log.addHandler(handler_console)
    return log


class JSONFormatter(logging.Formatter):

    def format(self, record):
        extra = collections.OrderedDict()
        extra['time'] = datetime.datetime.fromtimestamp(record.created).strftime(DEFAULT_TIME_STR)
        extra['level'] = record.levelname
        extra['pathname'] = record.pathname
        extra['lineno'] = record.lineno
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


logger = create_logger()

if __name__ == '__main__':
    logger.info({"a": 1})
    logger.error("Do something")
    logger.warning("Something maybe fail.")
