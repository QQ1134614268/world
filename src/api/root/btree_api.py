# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/28 0:35
"""

from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from api.root import btree_service
from api.root.vo import BTreeVO
from db.db import db
from util import ResUtil

btree_api = Blueprint("btree_api", __name__, url_prefix='/api/btree_api')


# mongo: 有顺序,但是没有明显的数据结构  node  一个大的文档
# mysql
#     字段
#       path  传id,
#             传fullpath
#       parentId
#              优点:
#                   结构简单
#              缺点:
#                   父子关系,移动时不方便
#       组合 path parentId

#  2     需求
#           条件查询
#           查找
#           删除
#           新增
#           移动
# 3 有一个根/ ?? 还是 很多/??
@btree_api.route('/addNode', methods=['POST'])
def addNode():
    data = request.get_json()
    nodeId = data.get('id')
    value = data.get('value')
    return btree_service.addNode(nodeId, value)


@btree_api.route('/updateNode', methods=['POST'])
def updateNode():
    data = request.get_json()
    nodeId = data.get('id')
    value = data.get('value')
    vo = BTreeVO.query.filter(BTreeVO.id == nodeId).first()
    vo.value = value
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("操作成功"))


@btree_api.route('/delNode', methods=['POST'])
def delNode():
    data = request.get_json()
    nodeId = data.get('id')
    fullPath = data.get('fullPath')
    voList = BTreeVO.query.filter(BTreeVO.fullPath.like(fullPath + str(nodeId) + "%")).all()
    db.session.delete(voList)
    db.session.commit()
    return jsonify(ResUtil.success("操作成功"))


@btree_api.route('/moveNode', methods=['POST'])
def moveNode():
    data = request.get_json()
    nodeId = data.get('id')
    targetId = data.get('targetId')
    dropType = data.get('dropType')
    targetVO = BTreeVO.query.filter(BTreeVO.id == targetId).first()
    vo = BTreeVO.query.filter(BTreeVO.id == nodeId).first()
    if dropType == "inner":
        BTreeVO.query.filter(BTreeVO.fullPath == vo.fullPath, BTreeVO.sort > vo.sort).update(
            {BTreeVO.sort: BTreeVO.sort - 1})
        tempVO = BTreeVO.query.filter(BTreeVO.fullPath == targetVO.fullPath + str(targetVO.id) + "/").order_by(
            desc(BTreeVO.sort)).first()
        vo.sort = tempVO.sort + 1 if tempVO else 1
    if dropType == "before":
        BTreeVO.query.filter(BTreeVO.fullPath == vo.fullPath, BTreeVO.sort > vo.sort).update(
            {BTreeVO.sort: BTreeVO.sort - 1})
        vo.sort = targetVO.sort
        BTreeVO.query.filter(BTreeVO.fullPath == targetVO.fullPath, BTreeVO.sort >= targetVO.sort).update(
            {BTreeVO.sort: BTreeVO.sort + 1})
    if dropType == "after":
        BTreeVO.query.filter(BTreeVO.fullPath == vo.fullPath, BTreeVO.sort > vo.sort).update(
            {BTreeVO.sort: BTreeVO.sort - 1})
        vo.sort = targetVO.sort + 1
        BTreeVO.query.filter(BTreeVO.fullPath == targetVO.fullPath, BTreeVO.sort > targetVO.sort).update(
            {BTreeVO.sort: BTreeVO.sort + 1})
    fullPath = targetVO.fullPath + str(targetVO.id) + "/" if dropType == "inner" else targetVO.fullPath
    if fullPath != vo.fullPath:
        sql = 'UPDATE btree_t SET fullPath = REPLACE(fullPath,"%s","%s") WHERE fullPath like "%s" ' % (
            vo.fullPath, fullPath, vo.fullPath + str(vo.id) + "/" + "%")
        db.session.execute(sql)
        vo.fullPath = fullPath
    db.session.commit()
    return btree_service.getAllNodesService(fullPath)


@btree_api.route('/getChildNodesById', methods=['GET'])
def getChildNodesById():
    nodeId = request.args.get("id")
    fullPath = request.args.get("fullPath")
    return btree_service.getChildNodesById(nodeId, fullPath)

# TODO 多个顶级节点
@btree_api.route('/getAllNodes', methods=['GET'])
def getAllNodes():
    fullPath = request.args.get("fullPath")
    if not fullPath:
        fullPath = '/'
    return btree_service.getAllNodesService(fullPath)
