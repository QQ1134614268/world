# -- coding:UTF-8 --

from flask import Blueprint, request, jsonify, make_response
from flask_restful import marshal, Resource

import service.user_service
from config.mysql_db import db
from config.redis_db import redisDB
from service import log_table_service
from util import res_util, verification_code_util
from vo.table_model import UserVO

user_api = Blueprint("user", __name__, url_prefix='/api/user_api')


@user_api.route('/getUserByName', methods=['GET'])
def getUserByName():
    username = request.args.get("username")
    user = UserVO.query.filter_by(username=username).first()
    if user:
        return res_util.json_success(user)
    return res_util.fail("找不到用户")


@user_api.route('/getUserById', methods=['GET'])
def getUserById():
    userId = request.args.get("userId")
    user = UserVO.query.filter_by(id=userId).first()
    return res_util.json_success(user)


@user_api.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    userId = service.user_service.get_id_by_token()
    user = UserVO.query.filter_by(id=userId).first()
    return res_util.json_success(user)


@user_api.route('/getUserByDict', methods=['GET'])
def getUserByDict():
    data = request.get_json()
    user = UserVO.query.filter_by(**data).all()
    return res_util.json_success(user)


@user_api.route('/getUserAll', methods=['GET'])
def getUserAll():
    user = list(UserVO.query.limit(10))
    return res_util.json_success(user)


class UserApi(Resource):

    def post(self, _id):
        data = request.get_json()
        vo = UserVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = UserVO.query.filter(UserVO.id == _id).first()
        return res_util.success(marshal(vo, UserVO.get_video_user_field()))

    def put(self, _id):
        data = request.get_json()
        UserVO.query.filter(UserVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        model = UserVO.query.filter(UserVO.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)


@user_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    user = UserVO.query.filter_by(username=username).first()
    if user and user.check_password(password):
        log_table_service.log_table(user.id, "登录系统", "登录")
        return res_util.json_success(service.user_service.get_token(user))
    else:
        return res_util.fail("账号密码不匹配")


@user_api.route('/logout', methods=['GET'])
def logout():
    # 单点登录, redis 删除
    log_table_service.log_table(service.user_service.get_id_by_token(), "退出", "退出")
    return res_util.json_success()


@user_api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username', '')
    code = data.get('code')
    if not code:
        return res_util.fail("验证码错误")
    cache_code = redisDB.get(code)
    if not (code and cache_code and code.upper() == cache_code.upper()):
        return res_util.fail("验证码错误")
    exist = UserVO.query.filter_by(username=username).first()
    if exist:
        return jsonify(res_util.fail("用户名已经存在"))
    password = data.get('password', '')
    vo = UserVO(username=username, password=password)
    db.session.add(vo)
    db.session.commit()
    return res_util.json_success()


@user_api.route('/get_verify_code', methods=['GET'])
def get_verify_code():
    code, img_bytes = verification_code_util.get_verify_code()
    response = make_response(img_bytes)
    response.headers['Content-Type'] = 'image/gif'
    redisDB.set(code, code, ex=60)
    return response
