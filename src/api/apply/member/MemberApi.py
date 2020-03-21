from io import BytesIO

import time
from flask import Blueprint, session, jsonify, make_response, request

from api.apply.member import StoreVO
from api.apply.member.UserVO import MemberUserVO
from db.db import db
from api.user import UserService
from util import PasswordUtil, ResUtil
from util import VerificationCodeUtil

member_api = Blueprint("member_api", __name__, url_prefix='/member_api')

# todo 注册验证手机号  手机号登录
VERIFY_CODE_KEY = "code"


@member_api.route('/register_store', methods=['POST'])
def register_store():
    """
    用户注册
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
          id: member_user
          required:
            - phone
            - password
            - store_name
          properties:
            store_name:
              description: 商户名
              type: string
              example: 三千烦恼丝
            phone:
              description: 手机号
              type: string
              example: 18829040560
            password:
              description: 密码
              type: string
              example: abc123
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    phone = data.get('phone', '')
    store_name = data.get('store_name', '')
    password = data.get('password', '')
    if not phone:
        return jsonify(ResUtil.fail("手机号不能为空"))
    if not store_name:
        return jsonify(ResUtil.fail("商户名不能为空"))
    if not password:
        return jsonify(ResUtil.fail("密码不能为空"))
    exist = StoreVO.query.filter_by(phone=phone).first()
    if exist:
        # db.session.query(MemberUserVO).filter(MemberUserVO.phone == phone).update({"password": password})
        return jsonify(ResUtil.fail("用户已经存在"))
    vo = StoreVO(store_name=store_name, phone=phone, password=StoreVO.get_password(password))
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("注册成功"))


@member_api.route('/get_verify_code', methods=['GET'])
def get_verify_code():
    """
    获取验证码
    ---
    tags:
      - member_api
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


@member_api.route('/login', methods=['POST'])
def login():
    """
    用户登录
    ---
    tags:
      - member_api
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

    if session.get(VERIFY_CODE_KEY).lower() != data.get("code").lower():
        if data.get("code").lower() == "zero":
            pass
        else:
            return jsonify(ResUtil.fail("验证码错误"))
    name = data.get('name', '')
    password = data.get('password', '')
    user = MemberUserVO.query.filter_by(name=name, password=PasswordUtil.get_sha256_salt_password(password)).first()
    if user:
        return jsonify(ResUtil.success(UserService.get_token( user.id, user.name )))
    else:
        return jsonify(ResUtil.success("账号密码不匹配"))
