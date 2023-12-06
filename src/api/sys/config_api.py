# -*- coding:utf-8 -*-
"""
@Time: 2021/12/5
@Description:
"""
from flask import request, Blueprint
from flask_restful import Resource

import service.user_service
from config.mysql_db import db
from util import res_util
from vo.table_model import EnumConfig

enum_api = Blueprint("enum", "enum", url_prefix='/api/enum_api')


class ConfigApi(Resource):

    def get(self, _id):
        if _id:
            return res_util.success(EnumConfig.query.filter(EnumConfig.id == _id).first())
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

    @staticmethod
    @enum_api.route('/page', methods=['GET'])
    def page():
        req = request.args
        page = req.get("currentPage", 1, int)
        page_size = req.get("pageSize", 10, int)
        parent_code = req.get("parent_code")
        group_code = req.get("group_code")
        query = EnumConfig.query
        if parent_code:
            query = query.filter(EnumConfig.parent_code == parent_code)
        if group_code:
            query = query.filter(EnumConfig.group_code == group_code)
        page_data = query.order_by(EnumConfig.create_time.desc()).paginate(page=page, per_page=page_size)
        return res_util.success(page_data)
