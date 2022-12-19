# -*- coding:utf-8 -*-
import uuid


def get_uuid():
    return uuid.uuid1().hex


if __name__ == '__main__':
    name = 'test_name'
    namespace = uuid.NAMESPACE_URL

    print(uuid.uuid1())
    print(uuid.uuid3(namespace, name))
    print(uuid.uuid4())
    print(uuid.uuid5(namespace, name))
