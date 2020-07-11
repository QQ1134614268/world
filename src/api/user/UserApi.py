# -- coding:UTF-8 --
import json

from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal

from api.user import UserService
from util import ResUtil
from vo.UserVO import UserVO

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
    return jsonify(ResUtil.success(marshal(user, user_fields)))


@user_api.route('/getUserById', methods=['GET'])
def getUserById():
    userId = request.args.get("userId")
    user = UserVO.query.filter_by(id=userId).first()
    return jsonify(ResUtil.success(marshal(user, user_fields)))


@user_api.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    userId = UserService.get_id_by_token()
    user = UserVO.query.filter_by(id=userId).first()
    return jsonify(ResUtil.success(marshal(user, user_fields)))


@user_api.route('/getUserByDict', methods=['GET'])
def getUserByDict():
    kw = request.args.get("kw")
    # data={"xxx":"xxx"} 自行组装
    data = json.loads(kw)
    user = UserVO.query.filter_by(**data).first()
    # user不存在 返回{"id": 0,"userType": 0, "username": null} 不好
    return jsonify(ResUtil.success(marshal(user, user_fields)))


@user_api.route('/getUserAll', methods=['GET'])
def getUserAll():
    user = list(UserVO.query.limit(10))
    return jsonify(ResUtil.success(marshal(user, user_fields)))


def get_auth():
    pass


@user_api.route('/addAttention', methods=['POST'])
def addAttention():
    data = request.get_json()
    userId = data.get('userId')
    group = data.get('group')
    return UserService.addAttention(userId, group)


@user_api.route('/getAttentionList', methods=['GET'])
def getAttentionList():
    return jsonify(ResUtil.success(UserService.getAttentionList()))


@user_api.route('/updateAttention', methods=['POST'])
def updateAttention():
    data = request.get_json()
    userId = data.get('userId')
    group = data.get('group')
    UserService.updateAttention(userId, group)
    return jsonify(ResUtil.success("账号密码不匹配"))


@user_api.route('/deleteAttention', methods=['POST'])
def deleteAttention():
    data = request.get_json()
    userId = data.get('userId')
    UserService.deleteAttention(userId)
    return jsonify(ResUtil.success("账号密码不匹配"))
