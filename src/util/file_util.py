import os
import shutil

from util import time_util
from util.unique_util import get_uuid


def get_file_name_by_uuid():
    return get_uuid()


def prepare_path(file_path, remove=False):
    """

    :param file_path:
    :param remove:
    :return:
    """
    dic_path = os.path.dirname(file_path)
    if os.path.exists(dic_path):
        if remove:
            shutil.rmtree(dic_path)
    else:
        os.makedirs(dic_path)


def get_filepath_with_time(file_path):
    dic_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    new_file_name = time_util.getUtcTimeStr() + "_" + file_name
    return os.path.join(dic_path, new_file_name)


def prepare_file(file_path, remove=False):
    prepare_path(file_path, remove)
    return get_filepath_with_time(file_path)


if __name__ == '__main__':
    print(get_filepath_with_time("F:/div/log.log"))
