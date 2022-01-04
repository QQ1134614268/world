# -*- coding:utf-8 -*-
"""
@Time: 2021/3/6
@Description:
"""
import random
import string

from flask import jsonify
from flask import request
from flask_restful import Resource
from flask_restful import marshal
from sqlalchemy import or_

import service.user_service
from config.mysql_db import db
from service.auth_service import set_model_user_id
from util import res_util
from util.video_util import get_first_frame_loc
from vo.table_model import VideoUserVO, WorksVO, TargetVO


class VideoUserLoginApi(Resource):

    def get(self):
        username = request.args.get("username")
        password = request.args.get("password")
        user = VideoUserVO.query.filter(VideoUserVO.username == username, VideoUserVO.password == password, ).first()
        if not user:
            return res_util.fail("密码不正确")
        return res_util.success(service.user_service.get_token(user))


class VideoUserApi(Resource):

    def post(self, _id):
        data = request.get_json()
        code = data.pop("code")
        code_vo = InvitationCodeVO.query.filter(InvitationCodeVO.code == code).first()
        if not code_vo:
            return res_util.fail("邀请码不正确!")
        vo = VideoUserVO(**data)
        db.session.add(vo)
        code_vo.code = ""
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = VideoUserVO.query.filter(VideoUserVO.id == _id).first()
        return res_util.success(marshal(vo, VideoUserVO.get_video_user_field()))

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
        if not data.get("thumbnail"):
            data["thumbnail"] = get_first_frame_loc(data["file"])
        vo = WorksVO(**data)
        set_model_user_id(vo)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = WorksVO.query.filter(WorksVO.id == _id).first()
        return res_util.json_success(vo)

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
        page_item = WorksVO.query.filter(*obj_filter).order_by(WorksVO.create_time.desc()).paginate(
            page=page, per_page=page_size)

        return res_util.page_success(page_item)


class WorksRankListApi(Resource):
    def get(self, _id):
        obj_filter = []
        results = WorksVO.query.filter(*obj_filter).order_by(WorksVO.create_time.desc()).limit(10).all()
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
            WorksVO.file,
            WorksVO.user_id,
            WorksVO.create_time,
            WorksVO.start,
            WorksVO.thumbnail,
            VideoUserVO.avatar,
            VideoUserVO.username,
        ).paginate(page=page, per_page=page_size)
        page_item.items = [dict(zip(item.keys(), item)) for item in page_item.items]
        return res_util.page_success(page_item)


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
            obj_filter.append(TargetVO.user_id == user_id)
        page_item = TargetVO.query.filter(*obj_filter).paginate(page=page, per_page=page_size)
        return res_util.page_success(page_item)


class TargetRankListApi(Resource):

    def get(self, _id):
        obj_filter = []
        results = TargetVO.query.filter(*obj_filter).order_by(TargetVO.create_time.desc()).limit(10).all()
        return jsonify(res_util.success(results))


class MarketTargetListApi(Resource):

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
        return res_util.page_success(page_item)
