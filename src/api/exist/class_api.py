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
from vo.table_model import ClassVO

class_fields = {
    'id': fields.Integer,
    'describe': fields.String,
    'name': fields.String,
    'wight': fields.Float,
    'data': fields.String,
}


class ClassApi(Resource):
    def get(self):
        if request.args.get("parent_id"):
            vos = ClassVO.query.filter(ClassVO.parent_id == request.args.get("parent_id")).all()
            return res_util.success([marshal(vo, class_fields) for vo in vos])
        if request.args.get("id"):
            vo = ClassVO.query.filter(ClassVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, class_fields))
        if request.args.get("all"):
            # 查找全部 todo
            vo = ClassVO.query.filter(ClassVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, class_fields))

        vos = ClassVO.query.filter(ClassVO.parent_id == 0).all()
        return res_util.success([marshal(vo, class_fields) for vo in vos])

    def post(self):
        data = request.get_json()
        parent_id = data.get("parent_id", "")
        describe = data.get("describe", "")
        name = data.get("name", "")
        vo = ClassVO(name=name, describe=describe, parent_id=parent_id, user_id=user_service.get_id_by_token(), )
        db.session.add(vo)
        db.session.commit()
        return jsonify(res_util.success())

    def delete(self):
        data = request.get_json()
        ClassVO.query.filter(ClassVO.id == data.get("id", "")).delete()
        db.session.commit()
        return jsonify(res_util.success())

    def put(self):
        # todo
        data = request.get_json()
        ClassVO.query.filter(ClassVO.id == data.get("id", "")).update(data)
        db.session.commit()
        # if data 拖拽功能
        return jsonify(res_util.success())
