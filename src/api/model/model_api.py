from flask import Blueprint, jsonify, request
from flask_restful import Resource

from api.user import UserService
from db.mongodb import mongoDB
from util import ResUtil

model_api = Blueprint("model_api", __name__, url_prefix='/api/model_api')


class Model(Resource):
    def get(self):
        fullPath = request.args.get("path")
        if not fullPath:
            fullPath = '/'
        return btree_service.getAllNodesService(fullPath)
        # nodeId = request.args.get("id")
        # fullPath = request.args.get("path")
        # return btree_service.getChildNodesById(nodeId, fullPath)

    def post(self):
        # return '', 204
        data = request.get_json()
        data["userId"] = UserService.get_id_by_token()
        collection = mongoDB.models
        collection.insert_one(data)
        return jsonify(ResUtil.success("success"))

    def put(self):
        # data = request.get_json()
        # nodeId = data.get('id')
        # targetId = data.get('targetId')
        # dropType = data.get('dropType')
        # targetVO = BTreeVO.query.filter(BTreeVO.id == targetId).first()
        # vo = BTreeVO.query.filter(BTreeVO.id == nodeId).first()
        # if dropType == "inner":
        #     BTreeVO.query.filter(BTreeVO.fullPath == vo.fullPath, BTreeVO.sort > vo.sort).update(
        #         {BTreeVO.sort: BTreeVO.sort - 1})
        #     tempVO = BTreeVO.query.filter(BTreeVO.fullPath == targetVO.fullPath + str(targetVO.id) + "/").order_by(
        #         desc(BTreeVO.sort)).first()
        #     vo.sort = tempVO.sort + 1 if tempVO else 1
        # if dropType == "before":
        #     BTreeVO.query.filter(BTreeVO.fullPath == vo.fullPath, BTreeVO.sort > vo.sort).update(
        #         {BTreeVO.sort: BTreeVO.sort - 1})
        #     vo.sort = targetVO.sort
        #     BTreeVO.query.filter(BTreeVO.fullPath == targetVO.fullPath, BTreeVO.sort >= targetVO.sort).update(
        #         {BTreeVO.sort: BTreeVO.sort + 1})
        # if dropType == "after":
        #     BTreeVO.query.filter(BTreeVO.fullPath == vo.fullPath, BTreeVO.sort > vo.sort).update(
        #         {BTreeVO.sort: BTreeVO.sort - 1})
        #     vo.sort = targetVO.sort + 1
        #     BTreeVO.query.filter(BTreeVO.fullPath == targetVO.fullPath, BTreeVO.sort > targetVO.sort).update(
        #         {BTreeVO.sort: BTreeVO.sort + 1})
        # fullPath = targetVO.fullPath + str(targetVO.id) + "/" if dropType == "inner" else targetVO.fullPath
        # if fullPath != vo.fullPath:
        #     sql = 'UPDATE btree_t SET fullPath = REPLACE(fullPath,"%s","%s") WHERE fullPath like "%s" ' % (
        #         vo.fullPath, fullPath, vo.fullPath + str(vo.id) + "/" + "%")
        #     db.session.execute(sql)
        #     vo.fullPath = fullPath
        # db.session.commit()
        # # # TODO 移动到顶级节点 禁止移动到子级节点
        # # BTreeVO.query.filter(BTreeVO.fullPath.like(vo.fullPath)).update(
        # #     {BTreeVO.fullPath: str().replace(vo.fullPath, fullPath)})
        # # db.session.commit()
        # return btree_service.getAllNodesService(fullPath)

        data = request.get_json()
        nodeId = data.get('id')
        value = data.get('value')
        vo = BTreeVO.query.filter(BTreeVO.id == nodeId).first()
        vo.value = value
        db.session.add(vo)
        db.session.commit()
        return jsonify(ResUtil.success("操作成功"))
    def delete(self):
        data = request.get_json()
        nodeId = data.get('id')
        fullPath = data.get('fullPath')
        voList = BTreeVO.query.filter(BTreeVO.fullPath.like(fullPath + str(nodeId) + "%")).all()
        db.session.delete(voList)
        db.session.commit()
        return jsonify(ResUtil.success("操作成功"))
