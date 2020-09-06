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


class ModelApi(Resource):
    def get(self):
        ret = ["zero", "", "", ]
        return jsonify(res_util.success(ret))

    def post(self):
        file = request.files["file"]
        enum_type = request.form.get("type")
        ret = []
        if enum_type == "zero":
            with open(file) as f:
                lines = f.readline()
                for line in lines:
                    ret.append(line)
        return jsonify(res_util.success("success"))
