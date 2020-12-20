# -*- coding:utf-8 -*-
"""
@Time: 2020/12/20
@Description: 
"""
from flask import Blueprint, request

from service import user_service
from util import res_util

attention_api = Blueprint("attention", __name__, url_prefix='/api/attention_api')


@attention_api.route('/addAttention', methods=['POST'])
def addAttention():
    data = request.get_json()
    userId = data.get('userId')
    group = data.get('group')
    return user_service.addAttention(userId, group)


@attention_api.route('/getAttentionList', methods=['GET'])
def getAttentionList():
    return res_util.success(user_service.getAttentionList())


@attention_api.route('/updateAttention', methods=['POST'])
def updateAttention():
    data = request.get_json()
    userId = data.get('userId')
    group = data.get('group')
    user_service.updateAttention(userId, group)
    return res_util.success("账号密码不匹配")


@attention_api.route('/deleteAttention', methods=['POST'])
def deleteAttention():
    data = request.get_json()
    userId = data.get('userId')
    user_service.deleteAttention(userId)
    return res_util.success("账号密码不匹配")
