# -*- coding:utf-8 -*-
"""
@Time: 2021/3/6
@Description:
"""
import os.path
import random
import string

import cv2
from flask import request, Blueprint
from flask_restful import Resource
from sqlalchemy import or_, insert
from sqlalchemy.dialects.mysql import insert

from config.enum_conf import Permission, ReviewEnum
from config.env_default import DATA_DIR
from config.mysql_db import db
from service.auth_service import set_model_user_id, permission_required
from service.user_service import get_id_by_token
from util import res_util
from util.log_util import logger
from util.video_util import get_first_frame_loc
from vo.table_model import UserVO
from vo.video_model import WorksVO, TargetVO, InvitationCodeVO

video_blueprint_api = Blueprint("video_blueprint_api", __name__, url_prefix='/api/video_blueprint_api')


class VideoBlueprintApi:

    @staticmethod
    @video_blueprint_api.route('/err_video/<int:_id>', methods=['GET'])
    def get_sum_time(_id):
        vos = WorksVO.query.all()
        for vo in vos:
            path = os.path.join(DATA_DIR, vo.file[1:])

            vo.size = os.path.getsize(path) / 1024 / 1024

            cap = cv2.VideoCapture(path)
            if cap.isOpened():
                rate = cap.get(5)
                frame_num = cap.get(7)
                duration = frame_num / rate
                vo.duration = duration
            else:
                logger.debug("cv2 打开文件失败", "文件路径: {}".format(path))
        return res_util.success(vos)


class InvitationCodeApi(Resource):

    @permission_required(Permission.INVITATION_CODE.name)
    def post(self, _id):
        data = {"user_id": get_id_by_token(), 'code': self.activation_code(get_id_by_token())}
        insert_stmt = insert(InvitationCodeVO).values(data)
        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
            user_id=insert_stmt.inserted.user_id,
            code=insert_stmt.inserted.code,
        )
        db.session.execute(on_duplicate_key_stmt)
        db.session.commit()
        return res_util.success()

    @permission_required(Permission.INVITATION_CODE.name)
    def put(self, _id):
        user_id = get_id_by_token()
        code = self.activation_code(user_id)
        data = {
            "code": code,
            "user_id": user_id
        }
        db.session.add(InvitationCodeVO(**data))
        db.session.commit()
        return res_util.success(code)

    @permission_required(Permission.INVITATION_CODE.name)
    def get(self, _id):
        user_id = get_id_by_token()
        vo = InvitationCodeVO.query.filter(InvitationCodeVO.user_id == user_id).first()
        return res_util.success(vo)

    @staticmethod
    def activation_code(_id, length=10):
        """
        id + L + 随机码
        string模块中的3个函数：string.letters，string.printable，string.printable
        """
        prefix = hex(_id)[2:] + 'L'
        length = length - len(prefix)
        chars = string.ascii_letters + string.digits
        return prefix + ''.join([random.choice(chars) for i in range(length)])


class VideoUserApi(Resource):

    def post(self, _id):
        data = request.get_json()
        code = data.pop("code")
        code_vo = InvitationCodeVO.query.filter(InvitationCodeVO.code == code).first()
        if not code_vo:
            return res_util.fail("邀请码不正确!")
        if UserVO.query.filter(UserVO.username == data.get("username")).first():
            return res_util.fail("用户名已经存在!")
        vo = UserVO(**data)
        db.session.add(vo)
        db.session.delete(code_vo)
        db.session.commit()
        return res_util.success(vo.id)


class WorksApi(Resource):

    def post(self, _id):
        data = request.get_json()
        if not data.get("thumbnail"):
            data["thumbnail"] = get_first_frame_loc(os.path.join(DATA_DIR, data["file"][1:]))
        vo = WorksVO(**data)
        set_model_user_id(vo)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = WorksVO.query.filter(WorksVO.id == _id).first()
        return res_util.success(vo)

    def put(self, _id):
        data = request.get_json()
        if "duration" in data:
            data.pop("duration")
        if "size" in data:
            data.pop("size")
        #  todo work(**data)
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

        return res_util.success(page_item)


class WorksRankListApi(Resource):
    def get(self, _id):
        obj_filter = [WorksVO.state == ReviewEnum.APPROVE.name]
        results = WorksVO.query.filter(*obj_filter).order_by(WorksVO.create_time.desc()).limit(10).all()
        return res_util.success(results)


class MarketWorksListApi(Resource):
    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        search = request.args.get("search")
        obj_filter = [WorksVO.state == ReviewEnum.APPROVE.name]
        if search:
            obj_filter.append(WorksVO.describe.contains(search))
        page_item = WorksVO.query.join(
            UserVO, WorksVO.user_id == UserVO.id
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
            UserVO.avatar,
            UserVO.username,
        ).paginate(page=page, per_page=page_size)
        page_item.items = [dict(zip(item.keys(), item)) for item in page_item.items]
        return res_util.success(page_item)


class TargetApi(Resource):

    def post(self, _id):
        data = request.get_json()
        vo = TargetVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = TargetVO.query.filter(TargetVO.id == _id).first()
        return res_util.success(vo)

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
        return res_util.success(page_item)


class TargetRankListApi(Resource):

    def get(self, _id):
        obj_filter = [TargetVO.state == ReviewEnum.APPROVE.name]
        results = TargetVO.query.filter(*obj_filter).order_by(TargetVO.create_time.desc()).limit(10).all()
        return res_util.success(results)


class MarketTargetListApi(Resource):

    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        search = request.args.get("search")
        user_id = request.args.get("user_id")
        obj_filter = [TargetVO.state == ReviewEnum.APPROVE.name]
        if user_id:
            obj_filter.append(TargetVO.user_id == user_id)

        if search:
            obj_filter.append(or_(TargetVO.title.contains(search), TargetVO.content.contains(search)))

        page_item = TargetVO.query.join(
            UserVO, TargetVO.user_id == UserVO.id
        ).filter(
            *obj_filter
        ).with_entities(
            TargetVO.id,
            TargetVO.title,
            TargetVO.content,
            TargetVO.price,
            TargetVO.user_id,
            TargetVO.create_time,
            UserVO.avatar,
            UserVO.username,
        ).paginate(page=page, per_page=page_size)
        page_item.items = [dict(zip(item.keys(), item)) for item in page_item.items]
        return res_util.success(page_item)


class ReviewTargetApi(Resource):

    @permission_required(Permission.VIDEO_REVIEW.name)
    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        query = TargetVO.query.join(
            UserVO, TargetVO.user_id == UserVO.id
        )
        user_name = request.args.get("user_name")
        if user_name:
            query = query.filter(TargetVO.user_name.contains(user_name))

        state = request.args.get("state", ReviewEnum.NONE.name)
        if state:
            query = query.filter(TargetVO.state == state)
        # 日期
        if request.args.get("startDate"):
            query = query.filter(TargetVO.create_time >= request.args.get("startDate"))
        if request.args.get("endDate"):
            query = query.filter(TargetVO.create_time <= request.args.get("endDate"))

        page_item = query.with_entities(
            TargetVO.id,
            TargetVO.title,
            TargetVO.content,
            TargetVO.price,
            TargetVO.user_id,
            TargetVO.create_time,
            TargetVO.state,
            UserVO.avatar,
            UserVO.username,
        ).paginate(page=page, per_page=page_size)
        page_item.items = [dict(zip(item.keys(), item)) for item in page_item.items]
        return res_util.success(page_item)

    @permission_required(Permission.VIDEO_REVIEW.name)
    def put(self, _id):
        data = request.get_json()
        TargetVO.query.filter(TargetVO.id == _id).update(data)
        db.session.commit()
        return res_util.success()


class ReviewWorksApi(Resource):

    @permission_required(Permission.VIDEO_REVIEW.name)
    def get(self, _id):
        page = request.args.get("page", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        query = WorksVO.query.join(
            UserVO, WorksVO.user_id == UserVO.id
        )
        user_name = request.args.get("user_name")
        if user_name:
            query = query.filter(UserVO.username.contains(user_name))

        state = request.args.get("state", ReviewEnum.NONE.name)
        if state:
            query = query.filter(WorksVO.state == state)
        # 日期
        if request.args.get("startDate"):
            query = query.filter(WorksVO.create_time >= request.args.get("startDate"))
        if request.args.get("endDate"):
            query = query.filter(WorksVO.create_time <= request.args.get("endDate"))

        page_item = query.with_entities(
            WorksVO.id,
            WorksVO.describe,
            WorksVO.thumbnail,
            WorksVO.user_id,
            WorksVO.create_time,
            WorksVO.state,
            UserVO.username,

        ).paginate(page=page, per_page=page_size)
        page_item.items = [dict(zip(item.keys(), item)) for item in page_item.items]
        return res_util.success(page_item)

    @permission_required(Permission.VIDEO_REVIEW.name)
    def put(self, _id):
        data = request.get_json()
        WorksVO.query.filter(WorksVO.id == _id).update(data)
        db.session.commit()
        return res_util.success()
