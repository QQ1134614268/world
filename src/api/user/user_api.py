# -- coding:UTF-8 --
import json

from flask import Blueprint, request
from flask_restful import fields, marshal

from service import user_service
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
    userId = user_service.get_id_by_token()
    user = UserVO.query.filter_by(id=userId).first()
    return res_util.success(marshal(user, user_fields))


@user_api.route('/getUserByDict', methods=['GET'])
def getUserByDict():
    kw = request.args.get("kw")
    # todo2
    # data={"xxx":"xxx"} 自行组装
    data = json.loads(kw)
    user = UserVO.query.filter_by(**data).first()
    # user不存在 返回{"id": 0,"userType": 0, "username": null} 不好
    return res_util.success(marshal(user, user_fields))


@user_api.route('/getUserAll', methods=['GET'])
def getUserAll():
    user = list(UserVO.query.limit(10))
    return res_util.success(marshal(user, user_fields))
