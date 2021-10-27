# -*- coding:utf-8 -*-
"""
@Time: 2021/3/6
@Description:
"""
import os
import random
import shutil
import string
from enum import Enum

from flask import jsonify, send_file
from flask import request
from flask_restful import Resource
from flask_restful import marshal
from sqlalchemy import or_

from config.conf import DATA_DIR, UPLOAD_FILE_PATH2
from config.mysql_db import db
from service.common_service import set_model_user_id
from service.token_service import get_id_by_token
from util import res_util
from util import token_util
from util.file_util import get_file_name_by_uuid
from util.log_util import logger
from util.video_util import get_first_frame_loc
from vo.table_model import VideoUserVO, WorksVO, TargetVO, InvitationCodeVO


class VideoUserLoginApi(Resource):

    def get(self):
        username = request.args.get("username")
        password = request.args.get("password")
        user = VideoUserVO.query.filter(VideoUserVO.username == username, VideoUserVO.password == password, ).first()
        if not user:
            return res_util.fail("密码不正确")
        return res_util.success(token_util.get_token(user.id, user.username, ))


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

        return jsonify(res_util.page_success(page_item))


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


class FileApi2(Resource):

    def get(self):
        path = request.args.get("path", "")
        full_path = os.path.join(DATA_DIR, path)
        if os.path.isfile(full_path):
            return send_file(full_path, as_attachment=True,
                             attachment_filename=full_path.split('/')[-1],
                             mimetype='application/octet-stream')
        logger.info("文件不存在: " + full_path)

    def post(self):
        file = request.files["file"]
        # file     print()    # 打印文件名
        f_name = get_file_name_by_uuid() + "_" + file.filename
        full_path = os.path.join(UPLOAD_FILE_PATH2, f_name)
        file.save(full_path)
        return res_util.success("upload_file/" + f_name)

    def delete(self):
        path = request.get_json("path")
        shutil.rmtree(path)
        return res_util.success()


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
        return jsonify(res_util.page_success(page_item))


class TargetRankListApi(Resource):

    def get(self, _id):
        obj_filter = []
        results = TargetVO.query.filter(*obj_filter).order_by(TargetVO.create_time.desc()).limit(10).all()
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


class Role(Enum):
    ADMIN = "ADMIN"
    SYS_ADMIN = "SYS_ADMIN"


class InvitationCodeApi(Resource):
    """
    邀请码
    """

    def post(self, _id):
        user_id = get_id_by_token()
        data = {
            "user_id": get_id_by_token()
        }
        user = VideoUserVO.query.filter(VideoUserVO.id == get_id_by_token()).first()
        if user.role not in ["ADMIN", "SYS_ADMIN", ]:
            return res_util.fail("权限不足!")
        vo = InvitationCodeVO.query.filter(InvitationCodeVO.user_id == user_id).first()
        if vo:
            self.put(vo.id)
            return res_util.success(vo.id)
        vo = InvitationCodeVO(**data)
        db.session.add(vo)
        db.session.commit()
        vo.code = self.activation_code(vo.id)
        db.session.commit()
        return res_util.success(vo.id)

    def put(self, _id):
        user_id = get_id_by_token()
        vo = InvitationCodeVO.query.filter(InvitationCodeVO.user_id == user_id).first()
        vo.code = self.activation_code(vo.id)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        user_id = get_id_by_token()
        vo = InvitationCodeVO.query.filter(InvitationCodeVO.user_id == user_id).first()
        return res_util.json_success(vo)

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
