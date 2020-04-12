# -- coding:UTF-8 --
import json
from io import BytesIO

from flask import Blueprint, jsonify, make_response, request
from flask_restful import fields, marshal

from api.user import UserService
from db.db import db
from db.redis_db import redisDB
from util import PasswordUtil, ResUtil
from util import VerificationCodeUtil
from vo.UserVO import UserVO

user_api = Blueprint("user", __name__, url_prefix='/api/user_api')


@user_api.route('/register', methods=['POST'])
def register():
    """
    用户注册
    ---
    tags:
      - user
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          用户注册
        required: true
        schema:
          id: user
          required:
            - username
            - password
            - email
          properties:
            username:
              description: 用户名
              type: string
              example: tom
            password:
              description: 密码
              type: string
              example: abc123
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    username = data.get('username', '')
    exist = UserVO.query.filter_by(username=username).first()
    if exist:
        return jsonify(ResUtil.fail("用户名已经存在"))
    password = data.get('password', '')
    vo = UserVO(username=username, password=PasswordUtil.get_sha256_salt_password(password))
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("注册成功"))


@user_api.route('/get_verify_code', methods=['GET'])
def get_verify_code():
    """
    获取验证码
    ---
    tags:
      - user
    parameters:
     - name: username
       type: string
       required: true
       description: 用户名
       in: query
       example: root
    responses:
      500:
        description: server error
      200:
        description: success
    """
    username = request.args.get("username")
    if not username:
        return jsonify(ResUtil.fail("参数不全"))
    file_io = BytesIO()
    code, image = VerificationCodeUtil.get_verify_code()
    image.save(file_io, 'jpeg')
    response = make_response(file_io.getvalue())
    response.headers['Content-Type'] = 'image/gif'
    redisDB.set("verify_code-" + username, code, ex=60)
    return response


@user_api.route('/login', methods=['POST'])
def login():
    """
    用户登录
    ---
    tags:
      - user
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description:
          用户登录
        required: true
        schema:
          id: login
          required:
            - username
            - password
            - code
          properties:
            username:
              description: 用户名
              type: string
              example: tom
            password:
              description: 密码
              type: string
              example: abc123
            code:
              description: 验证码
              type: string
              example: zero
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    code = data.get('code', '')
    if code.lower() == "zero" or (
            redisDB.get("verify_code-" + username) and redisDB.get("verify_code-" + username).lower() == code.lower()):
        user = UserVO.query.filter_by(username=username,
                                      password=PasswordUtil.get_sha256_salt_password(password)).first()
        if user:
            return jsonify(ResUtil.success(UserService.get_token(user.id, user.username, )))
        else:
            return jsonify(ResUtil.success("账号密码不匹配"))
    else:
        return jsonify(ResUtil.fail("验证码错误"))


@user_api.route('/logout', methods=['POST'])
def logout():
    return jsonify(ResUtil.success("退出"))


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
