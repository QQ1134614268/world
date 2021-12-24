# encoding: utf-8
# todo 公告, 反馈
import importlib
import random

import time
from flask import Blueprint, jsonify, make_response, request
from flask_restful import fields, marshal, Resource

import service.token_service
from config.conf import UPLOAD_FILE_PATH
from config.mysql_db import db
from config.redis_db import redisDB
from service import log_table_service, token_service
from util import res_util
from util import token_util
from util import verification_code_util
from vo.table_model import UserVO, AnnouncementVO, MessageVO

sys_api = Blueprint("sys", __name__, url_prefix='/api/sys_api')

announcement_fields = {
    'id': fields.Integer,
    'userid': fields.Integer,
    'content': fields.String,
    'images': fields.String
}


@sys_api.route('/get_verify_code', methods=['GET'])
def get_verify_code():
    code, img_bytes = verification_code_util.get_verify_code()
    response = make_response(img_bytes)
    response.headers['Content-Type'] = 'image/gif'
    redisDB.set(code, code, ex=60)
    return response


@sys_api.route('/login', methods=['POST'])
def login():
    """

    :return:
    """
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    user = UserVO.query.filter_by(username=username).first()
    if user and user.check_password(password):
        log_table_service.log_table(user.id, "登录系统", "登录")
        return jsonify(res_util.success(token_util.get_token(user.id, user.username, )))
    else:
        return jsonify(res_util.fail("账号密码不匹配"))


@sys_api.route('/logout', methods=['GET'])
def logout():
    # 单点登录, redis 删除
    log_table_service.log_table(token_service.get_id_by_token(), "退出", "退出")
    return jsonify(res_util.success("退出"))


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
    return jsonify(res_util.success("注册成功"))


@sys_api.route('/add_announcement', methods=['POST'])
def add_announcement():
    title = request.form.get('title')
    content = request.form.get('content')
    image = request.files['image']
    time_str = time.strftime('%Y%m%d_%H%M%S_') + str(random.randint(1000, 9999))
    image_path = UPLOAD_FILE_PATH + '/images/' + time_str + "-" + image.filename
    image.save(image_path)  # 保存文件到指定路径
    user_id = service.token_service.get_id_by_token()
    vo = AnnouncementVO(userid=user_id, title=title, content=content, images=image_path)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))


@sys_api.route('/get_announcement_list', methods=['GET'])
def get_announcement_list():
    message_list = list(AnnouncementVO.query.order_by(AnnouncementVO.create_time).all())
    message_list = [marshal(vo, announcement_fields) for vo in message_list]
    return jsonify(res_util.success(message_list))


@sys_api.route('/get_announcement_by_id', methods=['GET'])
def get_announcement_by_id():
    announcement_id = request.args.get('id')
    vo = AnnouncementVO.query.filter_by(id=announcement_id).first()
    return jsonify(res_util.success(marshal(vo, announcement_fields)))


@sys_api.route('/add_suggest', methods=['POST'])
def add_suggest():
    announcement_id = request.form.get("id")
    content = request.form.get('content')
    image = request.files.get("image")
    vo = MessageVO(announcement_id=announcement_id, content=content, image=image)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))


@sys_api.route('/get_suggest', methods=['GET'])
def get_suggest():
    announcement_id = request.args.get("id")
    message_list = MessageVO.query.filter_by(id=announcement_id).order_by(MessageVO.create_time).all()
    return jsonify(res_util.success(message_list))


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
