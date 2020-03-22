# -*- coding:utf-8 -*-
import socket


def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except ConnectionError:
        host_ip = "unknown ip"
    return host_ip
