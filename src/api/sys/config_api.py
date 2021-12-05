# -*- coding:utf-8 -*-
"""
@Time: 2021/12/5
@Description:
"""
from flask import request
from flask_restful import Resource

from config.mysql_db import db
from service import token_service
from util import res_util
from vo.table_model import EnumConfig


class ConfigApi(Resource):
    """工时"""

    def get(self, _id):
        parent_id = request.args.get("parent_id", -1)
        vos = EnumConfig.query.filter(
            EnumConfig.create_by == token_service.get_id_by_token(),
            EnumConfig.parent_id == parent_id
        ).all()
        return res_util.json_success(vos)

    def post(self, _id):
        data = request.get_json()
        vo = EnumConfig(**data)
        vo.create_by = token_service.get_id_by_token()
        db.session.add(vo)
        db.session.commit()
        return res_util.json_success(vo.id)

    def put(self, _id):
        data = request.get_json()
        EnumConfig.query.filter(EnumConfig.id == _id).update(data)
        db.session.commit()
        return res_util.json_success(_id)

    def delete(self, _id):
        EnumConfig.query.filter(EnumConfig.id == _id).delete()
        db.session.commit()
        return res_util.json_success(_id)
