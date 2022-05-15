# -- coding:UTF-8 --
from flask import Blueprint, request, send_file, make_response
from flask_restful import Resource

import service.user_service
from config.mysql_db import db
from config.redis_db import redisDB
from service import log_table_service, user_service
from service.user_service import get_id_by_token
from util import res_util, verification_code_util
from vo.table_model import UserVO

user_api = Blueprint("user", __name__, url_prefix='/api/user_api')


class UserApi(Resource):

    def post(self, _id):
        data = request.get_json()
        username = data.get('username', '')
        code = data.get('code')
        if not code:
            return res_util.fail("验证码错误")
        cache_code = redisDB.get(code.upper())
        if not (code and cache_code and code.upper() == cache_code.upper()):
            return res_util.fail("验证码错误")
        exist = UserVO.query.filter_by(username=username).first()
        if exist:
            return res_util.fail("用户名已经存在")
        password = data.get('password', '')
        vo = UserVO(username=username, password=password)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = UserVO.query.filter(UserVO.id == _id).with_entities(
            UserVO.id,
            UserVO.username,
            UserVO.phone,
            UserVO.avatar,
            UserVO.email,
            UserVO.userType,
            UserVO.describe,
            UserVO.id_card,
            UserVO.tiktok_number,
            UserVO.video_number,
            UserVO.wechat_number,
            UserVO.role
        ).first()
        return res_util.success(vo)

    def put(self, _id):
        user_id = user_service.get_id_by_token()
        data = request.get_json()
        UserVO.query.filter(UserVO.id == user_id).update(data)
        db.session.commit()
        return res_util.success(_id)


class UserBlueprintApi(Resource):
    """工时统计"""

    @staticmethod
    @user_api.route('/login/<int:_id>', methods=['GET'])
    def login(_id):
        username = request.args.get('username', '')
        password = request.args.get('password', '')
        user = UserVO.query.filter_by(username=username).first()
        if user and user.check_password(password):
            log_table_service.log_table(user.id, "登录系统", "登录")
            return res_util.success(service.user_service.get_token(user))
        else:
            return res_util.fail("账号密码不匹配")

    @staticmethod
    @user_api.route('/logout/<int:_id>', methods=['GET'])
    def logout(_id):
        # 单点登录, redis 删除
        log_table_service.log_table(service.user_service.get_id_by_token(), "退出", "退出")
        return res_util.success()

    @staticmethod
    @user_api.route('/get_verify_code', methods=['GET'])
    def get_verify_code():
        code, bytes_io = verification_code_util.get_verify_code()
        redisDB.set(code.upper(), code, ex=60)
        response = make_response(send_file(bytes_io, mimetype="image/png"))
        response.headers.add("Cache-Control", "no-store")
        return response

    @staticmethod
    @user_api.route('/update_token/<int:_id>', methods=['GET'])
    def update_token(_id):
        user = UserVO.query.filter(UserVO.id == get_id_by_token()).first()
        return res_util.success(service.user_service.get_token(user))
