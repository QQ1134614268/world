# -*- coding:utf-8 -*-
import requests


host = "http://ggok.top:9090"


def register(data):
    url = '/api/sys_api/register'
    return requests.post(host + url, json=data)
    # return res.json()


def login(data):
    url = '/api/sys_api/login'
    return requests.post(host + url, json=data)


headers_default = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dGNfdGltZV9zdHIiOiIyMDIwXzA1XzA0XzA1XzEyXzAxXzc1MjQxOSIsImlkIjozMTU3LCJuYW1lIjoibnFJTGRYIn0.iUwljJxvmvBV6L6IlnqIzZnhuvz4KWFgYKjmuWung8A"}


def addAttention(data, headers=headers_default):
    url = '/api/user_api/addAttention'
    return requests.post(host + url, json=data, headers=headers)


def getUserByName(data, headers=headers_default):
    url = '/api/user_api/getUserByName'
    return requests.get(host + url, params=data, headers=headers)


def add_speech(data, headers=headers_default):
    url = '/api/message_api/add_speech'
    return requests.post(host + url, json=data, headers=headers)


def get_my_speech(headers=headers_default):
    url = '/api/message_api/get_my_speech'
    return requests.get(host + url, headers=headers)


if __name__ == '__main__':
    getUserByName({"username": "wg"})
