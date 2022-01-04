# encoding: utf-8
import importlib

from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource

import service.user_service
from config.mysql_db import db
from config.redis_db import redisDB
from service import log_table_service
from util import res_util
from util import verification_code_util
from vo.table_model import UserVO, AnnouncementVO, SuggestVO

sys_api = Blueprint("sys", __name__, url_prefix='/api/sys_api')


@sys_api.route('/get_verify_code', methods=['GET'])
def get_verify_code():
    code, img_bytes = verification_code_util.get_verify_code()
    response = make_response(img_bytes)
    response.headers['Content-Type'] = 'image/gif'
    redisDB.set(code, code, ex=60)
    return response


@sys_api.route('/login', methods=['POST'])
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


@sys_api.route('/logout', methods=['GET'])
def logout():
    # 单点登录, redis 删除
    log_table_service.log_table(service.user_service.get_id_by_token(), "退出", "退出")
    return res_util.json_success()


@sys_api.route('/register', methods=['POST'])
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


class AnnouncementApi(Resource):
    def post(self, _id):
        data = request.get_json()
        user_id = service.user_service.get_id_by_token()
        vo = AnnouncementVO(userid=user_id, **data)
        db.session.add(vo)
        db.session.commit()
        return res_util.json_success()

    def get(self, _id):
        query_filter = []

        announcement_id = request.args.get('id')
        if announcement_id:
            query_filter.append(AnnouncementVO.id == announcement_id)
        message_list = AnnouncementVO.query.filter(query_filter).order_by(AnnouncementVO.create_time).all()
        return res_util.json_success(message_list)


class SuggestApi(Resource):

    def post(self, _id):
        data = request.get_json()

        vo = SuggestVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.json_success()

    def get(self, _id):
        message_list = SuggestVO.query.filter_by(id=_id).order_by(SuggestVO.create_time).all()
        return res_util.json_success(message_list)


class AllApi(Resource):

    def post(self, model):
        data = request.get_json()
        obj = self.reflect_obj(model)
        vo = obj(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, model, _id):
        obj = self.reflect_obj(model)
        vo = obj.query.filter(obj.id == request.args.get("id")).first()
        return res_util.success(vo.to_json())

    def put(self, model, _id):
        obj = self.reflect_obj(model)
        data = request.get_json()
        obj.query.filter(obj.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, model, _id):
        obj = self.reflect_obj(model)
        model = obj.query.filter(obj.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)

    @staticmethod
    def reflect_obj(model):
        model_path = "vo.table_model"
        class_name = model
        module = importlib.import_module(model_path)  # 根据"auth.my_auth"导入my_auth模块
        obj = getattr(module, class_name)()  # 反射并实例化
        return obj
