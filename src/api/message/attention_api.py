# -*- coding:utf-8 -*-
"""
@Time: 2020/12/20
@Description: 
"""
from flask import Blueprint, request

import service.attention_service
from util import res_util

attention_api = Blueprint("attention", __name__, url_prefix='/api/attention_api')


@attention_api.route('/addAttention', methods=['POST'])
def addAttention():
    data = request.get_json()
    userId = data.get('userId')
    group = data.get('group')
    return service.attention_service.addAttention(userId, group)


@attention_api.route('/getAttentionList', methods=['GET'])
def getAttentionList():
    return res_util.success(service.attention_service.getAttentionList())
