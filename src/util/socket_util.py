# -*- coding:utf-8 -*-
import socket


def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except ConnectionError:
        host_ip = "unknown ip"
    return host_ip


def get_host_name():
    try:
        host_name = socket.gethostname()
    except ConnectionError:
        host_name = host_name
    return host_name


if __name__ == '__main__':
    print(get_host_name())
