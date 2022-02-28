from flask import request
from flask_restful import Resource

import service.user_service
from config.mysql_db import db
from util import res_util
from vo.table_model import SystemLevelVO


class SystemLevelApi(Resource):

    def get(self, _id):
        parent_code = request.args.get("parent_code", '-1')
        vos = SystemLevelVO.query.filter(
            SystemLevelVO.parent_code == parent_code,
        ).all()
        return res_util.success(vos)

    def post(self, _id):
        data = request.get_json()
        vo = SystemLevelVO(**data)
        vo.create_by = service.user_service.get_id_by_token()
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def put(self, _id):
        data = request.get_json()
        SystemLevelVO.query.filter(SystemLevelVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        SystemLevelVO.query.filter(SystemLevelVO.id == _id).delete()
        db.session.commit()
        return res_util.success(_id)

