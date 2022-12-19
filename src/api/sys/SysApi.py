# encoding: utf-8
import importlib

from flask import Blueprint, request
from flask_restful import Resource

import service.user_service
from config.mysql_db import db
from util import res_util
from vo.table_model import AnnouncementVO, SuggestVO

sys_api = Blueprint("sys", __name__, url_prefix='/api/sys_api')


class AnnouncementApi(Resource):
    def post(self, _id):
        data = request.get_json()
        user_id = service.user_service.get_id_by_token()
        vo = AnnouncementVO(userid=user_id, **data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success()

    def get(self, _id):
        query_filter = []

        announcement_id = request.args.get('id')
        if announcement_id:
            query_filter.append(AnnouncementVO.id == announcement_id)
        message_list = AnnouncementVO.query.filter(query_filter).order_by(AnnouncementVO.create_time).all()
        return res_util.success(message_list)


class SuggestApi(Resource):

    def post(self, _id):
        data = request.get_json()

        vo = SuggestVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success()

    def get(self, _id):
        message_list = SuggestVO.query.filter_by(id=_id).order_by(SuggestVO.create_time).all()
        return res_util.success(message_list)


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
