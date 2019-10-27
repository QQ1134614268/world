"""
@author:huangran
"""
import datetime

import time

# time.time()
# time.localtime()
# time.localtime(time.time())
DEFALUT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_defalut_time_str():
    return time.strftime(DEFALUT_TIME_FORMAT)


def get_file_time_str():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')


def utc_to_local():
    timenow = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    return timenow


def get_utc_now():
    return datetime.datetime.utcnow()


def get_timestamp():
    return int(time.time())


def get_timestamp_():
    return int(round(time.time() * 1000))


def get_datetime():
    # TODO
    import datetime
    "2018-09-21 02:10:31"
    st = "2018-09-21 02:10:31"
    start_time = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
