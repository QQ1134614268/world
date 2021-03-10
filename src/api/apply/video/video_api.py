# -*- coding:utf-8 -*-
"""
@Time: 2021/3/6
@Description:
"""

from flask import request
from flask_restful import Resource

from config.mysql_db import db
from util import res_util
from vo.table_model import VideoUserVO


class VideoUserApi(Resource):

    def post(self):
        data = request.get_json()
        vo = VideoUserVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = VideoUserVO.query.filter(VideoUserVO.id == request.args.get("id")).first()
        return res_util.success(vo.to_json())

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

class VideoUserApi(Resource):

    def post(self):
        data = request.get_json()
        vo = VideoUserVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = VideoUserVO.query.filter(VideoUserVO.id == request.args.get("id")).first()
        return res_util.success(vo.to_json())

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
