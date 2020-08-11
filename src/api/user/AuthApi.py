# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:33

"""
from flask import Blueprint, jsonify, request

from util import res_util
from config.mysql_db import db
from service import user_service
from vo import AuthVO

auth_api = Blueprint("auth_api", __name__, url_prefix='/api/auth_api')


# 权限视图,组织,地区等
# 特殊权限视图
# 数据权限


@auth_api.route('/add_auth', methods=['POST'])
def add_auth():
    """
    配置权限
    分组织权限,地区权限,特殊权限eg: 接收email...
    ---
    tags:
     - auth_api
    parameters:
      - in: body
        name: body
        description:
          配置权限
        required: true
        schema:
          required:
            - path
            - user_id
          properties:
            path:
              description: 权限字符
              type: string
              example: /email/
            user_id:
              description: 用户id
              type: string
              example: 1
    responses:
      200:
        description: Successful operation
      400:
        description: Invalid input
     """
    data = request.get_json()
    path = data.get('path')
    user_id = data.get('user_id')
    # 检查当前用户权限  组织,地区,授予权限,特殊权限,子级权限
    current_user_id = user_service.get_id_by_token()
    vo = AuthVO(user_id=user_id, path=path)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))
