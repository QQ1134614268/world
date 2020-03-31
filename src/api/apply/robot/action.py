# -*- coding:utf-8 -*-
import requests
from global_variable import ROBOT_HOST
host = ROBOT_HOST


def register(data):
    url = '/api/user_api/register'
    return requests.post(host + url, json=data)
    # return res.json()


def login(data):
    url = '/api/user_api/login'
    return requests.post(host + url, json=data)


headers_default = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoicm9vdCIsImlkIjoxLCJ0aW1lc3RhbXAiOjE1NzcxMTc1NDJ9.-FKeKaMO9RIyAramv5HgGHAxxVfOEIiBSvpcSLfRp_w"}


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
