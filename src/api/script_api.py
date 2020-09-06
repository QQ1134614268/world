# -*- coding:utf-8 -*-
"""
@Time: 2020/9/6
@Description: 
"""
from flask import jsonify, request
from flask_restful import Resource
from flask_restful import fields

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
        enum_type = request.form.get("type")
        ret = []
        # from io import BytesIO
        # f = BytesIO(file.readline())
        lines = file.read()
        for line in lines:
            ret.append(line)
        # if enum_type == "zero" or 1:
        #     with open(file.read(), "rb") as f:
        #         lines = f.readline()
        #         for line in lines:
        #             ret.append(line)
        return res_util.success(ret)
