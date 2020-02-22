# -*- coding:utf-8 -*-
import requests

host = "http://127.0.0.1"


def register(data):
    url = '/user/register'
    return requests.post(host + url, json=data)
    # return res.json()


def login(data):
    url = '/user/login'
    return requests.post(host + url, json=data)


headers_default = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoicm9vdCIsImlkIjoxLCJ0aW1lc3RhbXAiOjE1NzcxMTc1NDJ9.-FKeKaMO9RIyAramv5HgGHAxxVfOEIiBSvpcSLfRp_w"}


def addAttention(data, headers=headers_default):
    url = '/user/addAttention'
    return requests.post(host + url, json=data, headers=headers)


def getUserByName(data, headers=headers_default):
    url = '/user/getUserByName'
    return requests.get(host + url, params=data, headers=headers)


def add_speech(data, headers=headers_default):
    url = '/message_api/add_speech'
    return requests.post(host + url, json=data, headers=headers)


def get_my_speech(headers=headers_default):
    url = '/message_api/get_my_speech'
    return requests.get(host + url, headers=headers)
