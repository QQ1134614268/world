import random
import uuid

import time


def get_file_name():
    file_name = time.strftime('%Y%m%d_%H%M%S_') + str(random.randint(1000, 9999))
    return file_name


def get_file_name_by_uuid():
    return uuid.uuid1()


if __name__ == '__main__':
    name = 'test_name'
    namespace = uuid.NAMESPACE_URL

    print(uuid.uuid1())
    print(uuid.uuid3(namespace, name))
    print(uuid.uuid4())
    print(uuid.uuid5(namespace, name))
