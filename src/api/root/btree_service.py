# -*- coding:utf-8 -*-
from flask import jsonify
from flask_restful import fields, marshal

from api.root.vo import BTreeVO
from api.user import UserService
from db.db import db
from util import ResUtil
from util.TreeUtil import getTreeFromList

btreeFields = {
    'id': fields.Integer,
    'fullPath': fields.String,
    'value': fields.String,
    'sort': fields.Integer,
}


def getAllNodesService(fullPath):
    voList = BTreeVO.query.filter(BTreeVO.fullPath.like(fullPath + "%")).order_by(BTreeVO.fullPath, BTreeVO.sort).all()
    data_list = [marshal(i, btreeFields) for i in voList]
    data_list = getTreeFromList(data_list)
    return jsonify(ResUtil.success(data_list))


def getChildNodesById(nodeId, fullPath):
    voList = BTreeVO.query.filter(BTreeVO.fullPath == fullPath + str(nodeId)).all()
    data_list = [marshal(i, btreeFields) for i in voList]
    return jsonify(ResUtil.success(data_list))


def addNode(nodeId, value):
    vo = BTreeVO.query.filter_by(id=nodeId).first()
    fullPath = vo.fullPath + str(vo.id) + "/"
    # sort = data.get('sort')
    userId = UserService.get_id_by_token()
    vo = BTreeVO(value=value, userId=userId, fullPath=fullPath)
    db.session.add(vo)
    db.session.commit()

    return jsonify(ResUtil.success(marshal(vo, btreeFields)))
