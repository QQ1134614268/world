# -*- coding:utf-8 -*-
"""
@Time: 2020/8/19
@Description: 
"""
from flask import jsonify, request
from flask_restful import Resource
from flask_restful import marshal, fields

from config.mysql_db import db
from service import user_service
from util import res_util
from .vo import ExistVO

model_fields = {
    'id': fields.Integer,
    'describe': fields.String,
    'name': fields.String,
    'wight': fields.Float,
    'data': fields.String,
}


class ExistApi(Resource):
    def get(self):
        if request.args.get("parent_id"):
            vos = ExistVO.query.filter_by(ExistVO.parent_id == request.args.get("parent_id")).all()
            return res_util.success([marshal(vo, model_fields) for vo in vos])

        if request.args.get("id"):
            vo = ExistVO.query.filter_by(ExistVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, model_fields))

    def post(self):
        data = request.get_json()
        parent_id = data.get("parent_id", "")
        describe = data.get("describe", "")
        name = data.get("name", "")
        vo = ExistVO(name=name, describe=describe, parent_id=parent_id, user_id=user_service.get_id_by_token(), )
        db.session.add(vo)
        db.session.commit()
        return jsonify(res_util.success())

    def delete(self):
        data = request.get_json()
        ExistVO.query.filter(ExistVO.id == data.get("id", "")).delete()
        db.session.commit()
        return jsonify(res_util.success())

    def put(self):
        # todo
        data = request.get_json()
        ExistVO.query.filter(ExistVO.id == data.get("id", "")).update(data)
        db.session.commit()
        return jsonify(res_util.success())
