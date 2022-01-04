# -- coding:UTF-8 --

from flask import Blueprint, request
from flask_restful import fields, marshal

import service.user_service
from util import res_util
from vo.table_model import UserVO

user_api = Blueprint("user", __name__, url_prefix='/api/user_api')
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'userType': fields.Integer,
}


@user_api.route('/getUserByName', methods=['GET'])
def getUserByName():
    username = request.args.get("username")
    user = UserVO.query.filter_by(username=username).first()
    if user:
        return res_util.success(marshal(user, user_fields))
    return res_util.fail("找不到用户")


@user_api.route('/getUserById', methods=['GET'])
def getUserById():
    userId = request.args.get("userId")
    user = UserVO.query.filter_by(id=userId).first()
    return res_util.success(marshal(user, user_fields))


@user_api.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    userId = service.user_service.get_id_by_token()
    user = UserVO.query.filter_by(id=userId).first()
    return res_util.success(marshal(user, user_fields))


@user_api.route('/getUserByDict', methods=['GET'])
def getUserByDict():
    data = request.get_json()
    user = UserVO.query.filter_by(**data).all()
    return res_util.success(marshal(user, user_fields))


@user_api.route('/getUserAll', methods=['GET'])
def getUserAll():
    user = list(UserVO.query.limit(10))
    return res_util.success(marshal(user, user_fields))
