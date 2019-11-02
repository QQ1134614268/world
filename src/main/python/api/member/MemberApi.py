from io import BytesIO

import time
from flask import Blueprint, session, jsonify, make_response, request

from config import res
from db.db import db
from service import UserService
from vo.UserVO import UserVO
from api.member.WalletVO import WalletVO
member_api = Blueprint("member_api", __name__, url_prefix='/member_api')


@member_api.route('/consume', methods=['POST'])
def consume():
    """
    消费
    ---
    tags:
      - member_api
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          用户注册
        required: true
        schema:
          id: user
          required:
            - username
            - password
            - email
          properties:
            username:
              description: 用户名
              type: string
              example: tom
            password:
              description: 密码
              type: string
              example: abc123
            email:
              description: 邮箱
              type: string
              example: xxx@xx.com
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    user_id = UserService.get_current_userid()
    amount = data.get('amount', '')
    wallet_id = data.get('wallet_id')

    vo = WalletVO.query.filter_by(id=wallet_id).first() # todo  id=  id是内置的,修改这个

    vo = UserVO(username=username, password=UserVO.get_password(password), email=email)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res.success("注册成功"))


@member_api.route('/invest', methods=['POST'])
def invest():
    """
    充值
    ---
    tags:
      - member_api
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          用户注册
        required: true
        schema:
          id: user
          required:
            - username
            - password
            - email
          properties:
            username:
              description: 用户名
              type: string
              example: tom
            password:
              description: 密码
              type: string
              example: abc123
            email:
              description: 邮箱
              type: string
              example: xxx@xx.com
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    user_id = UserService.get_current_userid()
    amount = data.get('amount', '')
    wallet_id = data.get('wallet_id')

    vo = WalletVO.query.filter_by(id=wallet_id).first() # todo  id=  id是内置的,修改这个

    vo = UserVO(username=username, password=UserVO.get_password(password), email=email)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res.success("注册成功"))

# 充值