# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/28 0:35
"""

from flask import Blueprint, jsonify, request

from api.root.btree_service import getAllNodesService
from api.root.btree_service import getChildNodesById
from api.root.vo import BTreeVO
from api.user import UserService
from db.db import db
from util import ResUtil

btree_api = Blueprint("btree_api", __name__, url_prefix='/btree_api')


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
    fullPath = data.get('fullPath')
    # 根??
    value = data.get('value')
    # sort = data.get('sort')
    user_id = UserService.get_id_by_token()
    vo = BTreeVO(value=value, user_id=user_id, fullPath=fullPath)
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("操作成功"))


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


@btree_api.route('/moveNodes', methods=['POST'])
def moveNodes():
    data = request.get_json()
    nodeId = data.get('id')
    vo = BTreeVO.query.filter(BTreeVO.id == nodeId).first()

    parentId = data.get('parentId')
    parentVO = BTreeVO.query.filter(BTreeVO.id == parentId).first()
    fullPath = parentVO.fullPath + str(parentVO.id)
    # sql = 'UPDATE btree_t SET fullPath = REPLACE(fullPath,"%s","%s") WHERE fullPath like "%s" ' % (vo.fullPath,fullPath, vo.fullPath)
    # db.session.execute(sql)
    # db.session.commit()
    # TODO 移动到顶级节点 禁止移动到子级节点
    BTreeVO.query.filter(BTreeVO.fullPath.like(vo.fullPath)).repalce(BTreeVO.vo.fullPath, fullPath)
    db.session.commit()
    return getAllNodesService(fullPath)


@btree_api.route('/getChildNodesById', methods=['GET'])
def getChildNodesById():
    nodeId = request.args.get("nodeId")
    fullPath = request.args.get("fullPath")
    return getChildNodesById(nodeId, fullPath)

# TODO 多个顶级节点
@btree_api.route('/getAllNodes', methods=['GET'])
def getAllNodes():
    fullPath = request.args.get("fullPath")
    return getAllNodesService(fullPath)
