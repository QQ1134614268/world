import datetime
import time

from config.conf import DATE_TIME_FORMAT


def getUtcTimeStr():
    return datetime.datetime.utcnow().strftime(DATE_TIME_FORMAT)


def getDatetimeByStr(time_str):
    return datetime.datetime.strptime(time_str, DATE_TIME_FORMAT)


def utc_to_local():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=8)


def getLocalTimeStr():
    return datetime.datetime.now().strftime(DATE_TIME_FORMAT)


def get_utc_now():
    return datetime.datetime.utcnow()


if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S_%f"))
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.now())
