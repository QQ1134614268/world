import os
import shutil

from util.unique_util import get_uuid


def get_file_name_by_uuid(file_name):
    return get_uuid() + "." + file_name.split('.')[-1]


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
