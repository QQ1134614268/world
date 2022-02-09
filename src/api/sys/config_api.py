# -*- coding:utf-8 -*-
"""
@Time: 2021/12/5
@Description:
"""
from flask import request
from flask_restful import Resource

import service.user_service
from config.mysql_db import db
from util import res_util
from vo.table_model import EnumConfig


class ConfigApi(Resource):

    def get(self, _id):
        parent_code = request.args.get("parent_code", '-1')
        group_code = request.args.get("group_code", None)
        create_by = request.args.get("create_by", service.user_service.get_id_by_token())
        vos = EnumConfig.query.filter(
            EnumConfig.create_by == create_by,
            EnumConfig.parent_code == parent_code,
            EnumConfig.group_code == group_code
        ).all()
        return res_util.success(vos)

    def post(self, _id):
        data = request.get_json()
        vo = EnumConfig(**data)
        vo.create_by = service.user_service.get_id_by_token()
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def put(self, _id):
        data = request.get_json()
        EnumConfig.query.filter(EnumConfig.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        EnumConfig.query.filter(EnumConfig.id == _id).delete()
        db.session.commit()
        return res_util.success(_id)


class EnumApi(Resource):

    def get(self, _id):
        parent_code = request.args.get("parent_code", '-1')
        group_code = request.args.get("group_code", None)
        vos = EnumConfig.query.filter(
            EnumConfig.parent_code == parent_code,
            EnumConfig.group_code == group_code
        ).all()
        return res_util.success(vos)
