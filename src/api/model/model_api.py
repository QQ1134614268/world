from flask import jsonify, request
from flask_restful import Resource
from flask_restful import marshal, fields

from api.user import UserService
from db.db import db
from util import ResUtil
from util.TreeUtil import get_tree
from .vo import ModelVO

model_fields = {
    'id': fields.Integer,
    'path': fields.String,
    'value': fields.String,
}


class ModelApi(Resource):
    def get(self):
        if request.args.get("id"):
            vo = ModelVO.query.filter_by(ModelVO.id == request.args.get("id")).first()
            return ResUtil.success(marshal(vo, model_fields))
        if request.args.get("model_id"):
            vo = ModelVO.query.filter_by(ModelVO.id == request.args.get("model_id")).first()
            vos = ModelVO.query.filter_by(ModelVO.path == vo.path + str(vo.id) + "/").order_by(
                ModelVO.path.desc()).all()
            vos = list(marshal(vos, model_fields))
            vos = get_tree(vos)
            return ResUtil.success(vos)

        vos = ModelVO.query.order_by(ModelVO.path.desc()).all()
        vos = list(marshal(vos, model_fields))
        vos = get_tree(vos)
        return ResUtil.success(vos)

    def post(self):
        data = request.get_json()
        value = data.get("value", "")
        data["userId"] = UserService.get_id_by_token()
        vo = ModelVO(userId=UserService.get_id_by_token(), value=value)
        db.session.add(vo)
        db.session.commit()
        return jsonify(ResUtil.success("success"))

    def put(self):
        data = request.get_json()
        if data["model_id"] and data["target_id"]:
            vo = ModelVO.query.filter(ModelVO.id == data["model_id"]).first()
            target_vo = ModelVO.query.filter(ModelVO.id == data["target_id"]).first()
            old_path = vo.path + str(vo.id) + "/"
            new_path = target_vo.path + str(target_vo.id) + "/"
            sql = 'UPDATE model_t SET path = REPLACE(path,"%s","%s") WHERE path like "%s" '.format(old_path,
                                                                                                   new_path,
                                                                                                   old_path + "%")
            db.session.execute(sql)
            vo.path = new_path
            db.session.commit()
        ModelVO.query.filter(ModelVO.id == data["model_id"]).update(dict(value=data["value"]))
        db.session.commit()
        return ResUtil.success("操作成功")

    def delete(self):
        data = request.get_json()
        modelId = data.get('id')
        vo = ModelVO.query.filter(ModelVO.id == modelId).first()
        vos = ModelVO.query.filter(ModelVO.path.like(vo.path + str(modelId) + "%")).all()
        db.session.delete(vos)
        db.session.commit()
        return ResUtil.success("操作成功")
