import datetime

import time

default_time_str = '%Y_%m_%d_%H_%M_%S_%f'


def getUtcTimeStr():
    return datetime.datetime.utcnow().strftime(default_time_str)


def getDatetimeByStr(time_str):
    return datetime.datetime.strptime(time_str, default_time_str)


def utc_to_local():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=8)


def getLocalTimeStr():
    return datetime.datetime.now().strftime(default_time_str)


def get_utc_now():
    return datetime.datetime.utcnow()


if __name__ == '__main__':
    print(datetime.datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f'))
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.now())
