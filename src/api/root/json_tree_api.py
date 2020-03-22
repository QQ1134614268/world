# -*- coding:utf-8 -*-
from flask import Blueprint, jsonify, request

from db.mongodb import mongoDB
from util import ResUtil

btree_mongo_api = Blueprint("btree_mongo_api", __name__, url_prefix='/api/btree_mongo_api')


@btree_mongo_api.route('/addModel', methods=['POST'])
def addModel():
    data = request.get_json()
    collection = mongoDB.btreeCollection
    collection.insert_one(data)
    return jsonify(ResUtil.success("success"))
