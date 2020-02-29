# -*- coding:utf-8 -*-
from flask import jsonify
from flask_restful import fields, marshal

from api.root.vo import BTreeVO
from util import ResUtil

btreeFields = {
    'id': fields.Integer,
    'fullPath': fields.String,
    'value': fields.Integer,
    'sort': fields.Integer,
}


def getAllNodesService(fullPath):
    voList = BTreeVO.query.filter(BTreeVO.fullPath.like(fullPath)).order_by(BTreeVO.fullPath).all()
    data_list = [marshal(i, btreeFields) for i in voList]
    return jsonify(ResUtil.success(data_list))


def getChildNodesById(nodeId, fullPath):
    voList = BTreeVO.query.filter(BTreeVO.fullPath == fullPath + str(nodeId)).all()
    data_list = [marshal(i, btreeFields) for i in voList]
    return jsonify(ResUtil.success(data_list))
