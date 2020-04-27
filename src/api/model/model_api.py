from flask import jsonify, request
from flask_restful import Resource
from flask_restful import marshal, fields

from api.user import UserService
from db.db import db
from util import ResUtil
from .vo import ModelVO

model_fields = {
    'id': fields.Integer,
    'path': fields.String,
    'value': fields.String,
}


class Model(Resource):
    def get(self):
        modelId = request.args.get("id")
        vo = ModelVO.query.filter_by(id=modelId).first()
        return jsonify(ResUtil.success(marshal(vo, model_fields)))

    def post(self):
        # return '', 204
        data = request.get_json()
        value = data.get("value", "")
        data["userId"] = UserService.get_id_by_token()
        vo = ModelVO(userId=UserService.get_id_by_token(), value=value)
        db.session.add(vo)
        db.session.commit()
        return jsonify(ResUtil.success("success"))

    def put(self):
        # todo  移动
        return jsonify(ResUtil.success("操作成功"))
    def delete(self):
        data = request.get_json()
        modelId = data.get('id')
        vo = ModelVO.query.filter_by(id=modelId).first()
        voList = ModelVO.query.filter(ModelVO.path.like(vo.path + str(modelId) + "%")).all()
        db.session.delete(voList)
        db.session.commit()
        return jsonify(ResUtil.success("操作成功"))
