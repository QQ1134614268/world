"""
@author:huangran
"""
from flask import Blueprint, Response
from flask import jsonify, make_response, request, json
from db.db import db
from vo.user import UserVO
import time
from config import jwt_config
from config import res
user_api = Blueprint("user", __name__, url_prefix='/user')


@user_api.route('/register', methods=['POST'])
def register():  # 用户注册
    """
        管理员添加新用户: add user
        :return:
        """
    data = request.get_json()
    username = data.get('username', '')
    exist = UserVO.query.filter_by(username=username).first()
    password = data.get('password', '')
    email = data.get('email', '')
    vo = UserVO(username=username, password=UserVO.get_password(password), email=email)
    if exist:
        return make_response(jsonify(res.fail("用户名已经存在")))
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("注册成功")))


@user_api.route('/login', methods=['POST'])
def login():
    """ todo
    用户名 密码  手机号/邮箱/身份证
       微信等 联合登陆
       依赖 微信"""
    data = request.get_json()
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
        return make_response(jsonify(res.success(jwt_config.get_token(payload))))
    else:
        return make_response(jsonify(res.success("账号密码不匹配")))


def logout():
    pass


def get_user():
    pass


def get_auth():
    pass
