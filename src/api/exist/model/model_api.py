from flask import jsonify, request
from flask_restful import Resource
from flask_restful import marshal, fields

import service.token_service
from api.exist.model.Util import Res
from api.exist.model.model import ModelVO, ProveVO, StoryVO
from config.mysql_db import db
from util import res_util
from util.tree_util import get_tree

model_fields = {
    'id': fields.Integer,
    'path': fields.String,
    'value': fields.String,
}


class ModelApi(Resource):
    def get(self):
        if request.args.get("id"):
            vo = ModelVO.query.filter_by(ModelVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, model_fields))

        if request.args.get("model_id"):
            vo = ModelVO.query.filter_by(ModelVO.id == request.args.get("model_id")).first()
            vos = ModelVO.query.filter_by(ModelVO.path == vo.path + str(vo.id) + "/").order_by(
                ModelVO.path.desc()).all()
            vos = list(marshal(vos, model_fields))
            vos = get_tree(vos)
            return res_util.success(vos)

        vos = ModelVO.query.order_by(ModelVO.path.desc()).all()
        vos = list(marshal(vos, model_fields))
        vos = get_tree(vos)
        return res_util.success(vos)

    def post(self):
        data = request.get_json()
        value = data.get("value", "")
        data["userId"] = service.token_service.get_id_by_token()
        vo = ModelVO(userId=service.token_service.get_id_by_token(), value=value)
        db.session.add(vo)
        db.session.commit()
        return jsonify(res_util.success("success"))

    def put(self):
        data = request.get_json()
        if data["model_id"] and data["target_id"]:
            vo = ModelVO.query.filter(ModelVO.id == data["model_id"]).first()
            target_vo = ModelVO.query.filter(ModelVO.id == data["target_id"]).first()
            old_path = vo.path + str(vo.id) + "/"
            new_path = target_vo.path + str(target_vo.id) + "/"
            sql = 'UPDATE model_t SET path = REPLACE(path,"%s","%s") WHERE path like "%s" '.format(
                old_path, new_path, old_path + "%")
            db.session.execute(sql)
            vo.path = new_path
            db.session.commit()
        ModelVO.query.filter(ModelVO.id == data["model_id"]).update(dict(value=data["value"]))
        db.session.commit()
        return res_util.success("操作成功")

    def delete(self):
        data = request.get_json()
        modelId = data.get('id')
        vo = ModelVO.query.filter(ModelVO.id == modelId).first()
        vos = ModelVO.query.filter(ModelVO.path.like(vo.path + str(modelId) + "%")).all()
        db.session.delete(vos)
        db.session.commit()
        return res_util.success("操作成功")


class ProveApi(Resource):
    @staticmethod
    def get(_id):
        return Res.get(_id, ProveVO)

    @staticmethod
    def post(_id):
        return Res.add(ProveVO, request.get_json())

    @staticmethod
    def put(_id):
        return Res.update(_id, ProveVO, request.get_json())

    @staticmethod
    def delete(_id):
        return Res.delete(_id, ProveVO)


class StoryApi(Resource):
    def get(self, _id):
        return Res.get(_id, StoryVO)

    def post(self, _id):
        return Res.add(StoryVO, request.get_json())

    def put(self, _id):
        return Res.update(_id, StoryVO, request.get_json())

    def delete(self, _id):
        return Res.delete(_id, StoryVO)


class UploadDataApi:
    @staticmethod
    def post(_id):
        file = request.files["file"]
        lines = file.readlines()
        for index, line in enumerate(lines):
            lines[index] = str(line, encoding="utf-8").replace("\r\n", "").replace("\t", " " * 4)
        for index, parent_line in enumerate(lines):
            if UploadDataApi.get_level(parent_line) == 0:
                p_vo = ProveVO(parent_id=1, value=parent_line)
                db.session.add(p_vo)
                db.session.flush()
                UploadDataApi.digui(p_vo, 0, lines[index:])
        return res_util.success()

    @staticmethod
    def digui(p_vo, level, lines):
        for index, parent_line in enumerate(lines):
            if level + 1 == UploadDataApi.get_level(parent_line):
                c_vo = ProveVO(parent_id=p_vo.id, value=parent_line)
                db.session.add(c_vo)
                UploadDataApi.digui(c_vo, UploadDataApi.get_level(parent_line), lines[index:])
            elif level < UploadDataApi.get_level(parent_line) + 1:
                break

    @staticmethod
    def get_level(line: str):
        new = line.lstrip()
        len_space = len(line) - len(new)
        return bool(len_space % 4) + len_space // 4

    @staticmethod
    def get(_id):
        pass
