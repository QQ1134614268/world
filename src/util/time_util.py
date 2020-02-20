import datetime

default_time_str = '%Y_%m_%d__%H_%M_%S.%f'


def getTimeStr():
    return datetime.datetime.now().strftime(default_time_str)


def getDatetimeByStr(time_str):
    return datetime.datetime.strptime(time_str, default_time_str)
