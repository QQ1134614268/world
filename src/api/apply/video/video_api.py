# -*- coding:utf-8 -*-
"""
@Time: 2021/3/6
@Description:
"""

from flask import jsonify
from flask import request
from flask_restful import Resource
from sqlalchemy import or_

from config.mysql_db import db
from service.common_service import set_model_user_id
from util import res_util
from util import token_util
from util.video_util import get_first_frame_loc
from vo.table_model import VideoUserVO, WorksVO, TargetVO, InvitationCodeVO


class VideoUserApi(Resource):

    def post(self, _id):
        data = request.get_json()
        # UserVO
        vo = VideoUserVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        if _id:
            vo = VideoUserVO.query.filter(VideoUserVO.id == _id).first()
            return res_util.json_success(vo)
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
        data["thumbnail"] = get_first_frame_loc(data["file"])
        vo = WorksVO(**data)
        set_model_user_id(vo)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        if _id:
            vo = WorksVO.query.filter(WorksVO.id == _id).first()
            return res_util.json_success(vo)
        obj_filter = []
        vos = WorksVO.query.all()
        return jsonify(res_util.success(vos))

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


class WorksListApi(Resource):
    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        search = request.args.get("search")
        user_id = request.args.get("user_id")
        obj_filter = []
        if search:
            obj_filter.append(WorksVO.describe.contains(search))
        if user_id:
            obj_filter.append(WorksVO.user_id == user_id)
        page_item = WorksVO.query.filter(*obj_filter).paginate(page=page, per_page=page_size)

        return jsonify(res_util.page_success(page_item))


class WorksRankListApi(Resource):
    def get(self, _id):
        obj_filter = []
        results = WorksVO.query.filter(*obj_filter).limit(10).all()
        return jsonify(res_util.success(results))


class MarketWorksListApi(Resource):
    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        search = request.args.get("search")
        obj_filter = []
        if search:
            obj_filter.append(WorksVO.describe.contains(search))
        page_item = WorksVO.query.join(
            VideoUserVO, WorksVO.user_id == VideoUserVO.id
        ).filter(
            *obj_filter
        ).with_entities(
            WorksVO.id,
            WorksVO.describe,
            WorksVO.outer_chain,
            WorksVO.file,
            WorksVO.user_id,
            WorksVO.create_time,
            WorksVO.start,
            WorksVO.thumbnail,
            VideoUserVO.avatar,
            VideoUserVO.username,
        ).paginate(page=page, per_page=page_size)
        page_item.items = [dict(zip(item.keys(), item)) for item in page_item.items]
        return jsonify(res_util.page_success(page_item))


class TargetApi(Resource):

    def post(self, _id):
        data = request.get_json()
        vo = TargetVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = TargetVO.query.filter(TargetVO.id == _id).first()
        return res_util.json_success(vo)

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


class TargetListApi(Resource):

    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        search = request.args.get("search")
        user_id = request.args.get("user_id")
        obj_filter = []
        if search:
            obj_filter.append(or_(TargetVO.title.contains(search), TargetVO.content.contains(search)))
        if user_id:
            obj_filter.append(WorksVO.user_id == user_id)
        page_item = TargetVO.query.filter(*obj_filter).paginate(page=page, per_page=page_size)
        return jsonify(res_util.page_success(page_item))


class TargetRankListApi(Resource):

    def get(self, _id):
        obj_filter = []
        results = TargetVO.query.filter(*obj_filter).limit(10).all()
        return jsonify(res_util.success(results))


class MarketTargetListApi(Resource):
    """

    """

    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        search = request.args.get("search")
        user_id = request.args.get("user_id")
        obj_filter = []
        if user_id:
            obj_filter.append(TargetVO.user_id == user_id)

        if search:
            obj_filter.append(or_(TargetVO.title.contains(search), TargetVO.content.contains(search)))

        page_item = TargetVO.query.join(
            VideoUserVO, TargetVO.user_id == VideoUserVO.id
        ).filter(
            *obj_filter
        ).with_entities(
            TargetVO.id,
            TargetVO.title,
            TargetVO.content,
            TargetVO.price,
            TargetVO.user_id,
            TargetVO.create_time,
            VideoUserVO.avatar,
            VideoUserVO.username,
        ).paginate(page=page, per_page=page_size)
        page_item.items = [dict(zip(item.keys(), item)) for item in page_item.items]
        return jsonify(res_util.page_success(page_item))


class InvitationCodeApi(Resource):
    """
    邀请码
    """

    def post(self, _id):
        data = request.get_json()
        vo = InvitationCodeVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)


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
