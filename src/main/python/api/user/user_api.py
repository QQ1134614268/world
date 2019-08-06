# -- coding:UTF-8 --
"""
@author:huangran
"""
from flask import Blueprint, session, jsonify, make_response, request
from db.db import db
from vo.user import UserVO
import time
from config import jwt_config
from config import res
from config import verification_code

user_api = Blueprint("user", __name__, url_prefix='/user')

VERIFY_CODE_KEY = "code"


@user_api.route('/register', methods=['POST'])
def register():
    """
    用户注册
    ---
    tags:
      - user
    parameters:
      - name: username
        in: query
        type:
        required: true
        description: 用户名
      - name: password
        in: query
        type: string
        required: true
        description: 密码
      - name: email
        in: query
        type: email
        description: 邮箱
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    username = data.get('username', '')
    exist = UserVO.query.filter_by(username=username).first()
    password = data.get('password', '')
    email = data.get('email', '')
    vo = UserVO(username=username, password=UserVO.get_password(password), email=email)
    if exist:
        return jsonify(res.fail("用户名已经存在"))
    db.session.add(vo)
    db.session.commit()
    return jsonify(res.success("注册成功"))


@user_api.route('/get_verify_code', methods=['GET'])
def get_verify_code():
    from io import BytesIO
    file_io = BytesIO()
    code, image = verification_code.get_verify_code()
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
    parameters:
      - name: username
        in: query
        type:
        required: true
        description: 用户名
      - name: password
        in: query
        type: string
        required: true
        description: 密码
      - name: email
        in: query
        type: email
        description: 邮箱
    responses:
      500:
        description: server error
      200:
        description: success
    """
    # """ todo
    # 用户名 密码  手机号/邮箱/身份证
    #    微信等 联合登陆
    #    依赖 微信"""
    data = request.get_json()
    if session.get(VERIFY_CODE_KEY).lower() != data.get("verify_code").lower():
        if session.get(VERIFY_CODE_KEY).lower() == "zero":
            pass
        else:
            return jsonify(res.fail("验证码错误"))
    username = data.get('username', '')
    password = data.get('password', '')
    user = UserVO.query.filter_by(username=username, password=UserVO.get_password(password)).first()
    if user:
        payload = {
            "username": user.username,
            "userid": user.id,
            "timestamp": int(time.time()),
            # "exp": 1448333419,
        }
        return jsonify(res.success(jwt_config.get_token(payload)))
    else:
        return jsonify(res.success("账号密码不匹配"))


def logout():
    pass


def get_user():
    pass


def get_auth():
    pass
