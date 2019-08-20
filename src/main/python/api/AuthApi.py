# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:33
# @Author  : huangran
"""
from flask import Blueprint, jsonify, make_response

from config import res

auth_api = Blueprint("auth_api", __name__, url_prefix='/auth_api')


@auth_api.route('/add_origin', methods=['POST'])
def add_auth():
    """
    配置权限
    分组织权限,地区权限,特殊权限,接收email
    ---
    tags:
     - auth_api
    parameters:
     - name: content
       in: path
       type: string
       required: true
       description: content
     - name: images
       in: query
       type: file
       description: a image
     - name: video
       in: query
       type: file
       description: video
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # data = request.get_json()
    # name = data.get('name')
    # level = 0
    # vo = AreaVO(name=name, level=level, video=1)
    # db.session.add(vo)
    # db.session.commit()
    return make_response(jsonify(res.success("操作成功")))
