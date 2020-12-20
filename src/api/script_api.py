# -*- coding:utf-8 -*-
"""
@Time: 2020/9/6
@Description: 
"""
from flask import jsonify, request
from flask_restful import Resource
from flask_restful import fields
from sqlalchemy.sql import func

from vo.table_model import ClassVO
from config.mysql_db import db
from util import res_util

model_fields = {
    'id': fields.Integer,
}


class ScriptApi(Resource):
    def get(self):
        ret = ["zero", "", "", ]
        return jsonify(res_util.success(ret))

    def post(self):
        file = request.files["file"]
        lines = file.readlines()
        root = {"children": [], "id": 0}
        level = {-1: root}
        id_max = ClassVO.query.with_entities(func.max(ClassVO.id)).scalar() or 0
        vo_id = id_max + 1
        vos = []
        for line in lines:
            curr = str(line, encoding="utf-8").replace("\r\n", "")
            if not curr.lstrip():
                continue
            space = len(curr) - len(curr.lstrip())
            data = {"value": curr.lstrip(), "children": [], "id": vo_id}
            vo_id += 1
            level[space // 4 - 1]["children"].append(data)
            level[space // 4] = data
            vos.append(ClassVO(id=data["id"], name=data["value"], parent_id=level[space // 4 - 1]["id"]))
        db.session.add_all(vos)
        db.session.commit()
        return res_util.success(root)
