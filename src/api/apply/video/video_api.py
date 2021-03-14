# -*- coding:utf-8 -*-
"""
@Time: 2021/3/6
@Description:
"""

from flask import request
from flask_restful import Resource

from config.mysql_db import db
from util import res_util
from util import token_util
from vo.table_model import VideoUserVO, WorksVO, TargetVO


class VideoUserApi(Resource):

    def post(self, _id):
        data = request.get_json()
        vo = VideoUserVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        if _id:
            vo = VideoUserVO.query.filter(VideoUserVO.id == request.args.get("id")).first()
            return res_util.success(vo)
        obj_filter = []
        username = request.args.get("username")
        password = request.args.get("password")
        if username:
            user = VideoUserVO.query.filter(VideoUserVO.username == username,
                                            VideoUserVO.password == password, ).first()
            return res_util.success(token_util.get_token(user.id, user.username, ))

    def put(self, _id):
        data = request.get_json()
        VideoUserVO.query.filter(VideoUserVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        model = VideoUserVO.query.filter(VideoUserVO.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)


class WorksApi(Resource):

    def post(self, _id):
        data = request.get_json()
        vo = WorksVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = WorksVO.query.filter(WorksVO.id == request.args.get("id")).first()
        return res_util.success(vo.to_json())

    def put(self, _id):
        data = request.get_json()
        WorksVO.query.filter(WorksVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        model = WorksVO.query.filter(WorksVO.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)


class TargetApi(Resource):

    def post(self, ):
        data = request.get_json()
        vo = TargetVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = TargetVO.query.filter(TargetVO.id == request.args.get("id")).first()
        return res_util.success(vo.to_json())

    def put(self, _id):
        data = request.get_json()
        TargetVO.query.filter(TargetVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        model = TargetVO.query.filter(TargetVO.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)


class AllApi(Resource):
    # todo

    def post(self, model, _id):
        obj = self.__init_obj__(model)
        data = request.get_json()
        vo = WorksVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, model, _id):
        obj = self.__init_obj__(model)
        vo = obj.query.filter(obj.id == request.args.get("id")).first()
        return res_util.success(vo.to_json())

    def put(self, model, _id):
        obj = self.__init_obj__(model)
        data = request.get_json()
        obj.query.filter(obj.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, model, _id):
        obj = self.__init_obj__(model)
        model = obj.query.filter(obj.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)

    def __init_obj__(self, model):
        model_path = "vo.table_model"
        import importlib
        class_name = model
        module = importlib.import_module(model_path)  # 根据"auth.my_auth"导入my_auth模块
        obj_i = getattr(module, class_name)()  # 反射并实例化
        return obj_i

    def __init__(self, model):
        # todo
        return
        request.args.get_path = ""
        model_path = "vo.table_model"
        import importlib
        class_name = model
        module = importlib.import_module(model_path)  # 根据"auth.my_auth"导入my_auth模块
        obj_i = getattr(module, class_name)()  # 反射并实例化
        return obj_i
