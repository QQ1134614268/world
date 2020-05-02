# -*- coding:utf-8 -*-
from flask_restful import Resource
from flask_restful import fields

model_fields = {
    'id': fields.Integer,
    'path': fields.String,
    'value': fields.String,
}


# todo
# 分析工人能力-工时接口
class WorkerApi(Resource):
    def get(self):
        pass
