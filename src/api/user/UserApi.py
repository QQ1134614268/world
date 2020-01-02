# -- coding:UTF-8 --
from io import BytesIO

import time
from flask import Blueprint, session, jsonify, make_response, request

from db.db import db
from service import UserService
from util import PasswordUtil, ResUtil
from util import VerificationCodeUtil
from vo.UserVO import UserVO

user_api = Blueprint("user", __name__, url_prefix='/user')

VERIFY_CODE_KEY = "code"


@user_api.route('/register', methods=['POST'])
def register():
    """
    用户注册
    ---
    tags:
      - user
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
    username = data.get('username', '')
    exist = UserVO.query.filter_by(username=username).first()
    if exist:
        return jsonify(ResUtil.fail("用户名已经存在"))
    password = data.get('password', '')
    email = data.get('email', '')
    vo = UserVO(username=username, password=PasswordUtil.get_sha256_salt_password(password), email=email)
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("注册成功"))
if __name__ == '__main__':
    UserVO.query.filter_by(username="111")

@user_api.route('/get_verify_code', methods=['GET'])
def get_verify_code():
    """
    获取验证码
    ---
    tags:
      - user
    responses:
      500:
        description: server error
      200:
        description: success
    """
    file_io = BytesIO()
    code, image = VerificationCodeUtil.get_verify_code()
    image.save(file_io, 'jpeg')
    response = make_response(file_io.getvalue())
    response.headers['Content-Type'] = 'image/gif'
    session[VERIFY_CODE_KEY] = code
    return response


@user_api.route('/login', methods=['POST'])
def login():
    """
    用户登录
    ---
    tags:
      - user
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description:
          用户登录
        required: true
        schema:
          id: login
          required:
            - username
            - password
            - code
          properties:
            username:
              description: 用户名
              type: string
              example: tom
            password:
              description: 密码
              type: string
              example: abc123
            code:
              description: 验证码
              type: string
              example: zero
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    if data.get("code").lower() == "zero":
        pass
    # todo  session.get(VERIFY_CODE_KEY)  None 问题
    elif session.get(VERIFY_CODE_KEY).lower() != data.get("code").lower():
        return jsonify(ResUtil.fail("验证码错误"))
    username = data.get('username', '')
    password = data.get('password', '')
    user = UserVO.query.filter_by(username=username, password=PasswordUtil.get_sha256_salt_password(password)).first()
    if user:
        payload = {
            "name": user.username,
            "id": user.id,
            "timestamp": int(time.time()),
            # "exp": 1448333419,
        }
        return jsonify(ResUtil.success(UserService.get_token(payload)))
    else:
        return jsonify(ResUtil.success("账号密码不匹配"))


def logout():
    pass


def get_user():
    pass


def get_auth():
    pass
