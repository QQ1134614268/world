# encoding: utf-8
import random
import time

from flask import Blueprint, jsonify, make_response, request
from flask_restful import fields, marshal

from config.conf import UPLOAD_FILE_PATH
from config.mysql_db import db
from config.redis_db import redisDB
from service import user_service
from util import password_util, res_util
from util import token_util
from util import verification_code_util
from vo.UserVO import AnnouncementVO, MessageVO
from vo.UserVO import UserVO

sys_api = Blueprint("sys", __name__, url_prefix='/api/sys_api')

announcement_fields = {
    'id': fields.Integer,
    'userid': fields.Integer,
    'content': fields.String,
    'images': fields.String
}


@sys_api.route('/get_verify_code', methods=['GET'])
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
    assert username, "用户名不正确"
    code, img_bytes = verification_code_util.get_verify_code()
    response = make_response(img_bytes)
    response.headers['Content-Type'] = 'image/gif'
    redisDB.set("verify_code-" + username, code, ex=60)
    return response


@sys_api.route('/login', methods=['POST'])
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
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    user = UserVO.query.filter_by(username=username,
                                  password=password_util.get_sha256_salt_password(password)).first()
    if user:
        return jsonify(res_util.success(token_util.get_token(user.id, user.username, )))
    else:
        return jsonify(res_util.fail("账号密码不匹配"))


@sys_api.route('/logout', methods=['POST'])
def logout():
    return jsonify(res_util.success("退出"))


@sys_api.route('/register', methods=['POST'])
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
    # user_type = data.get('code', '')
    code = data.get('code', '')
    cache_code = redisDB.get("verify_code-" + username) or ""
    if not (code.lower() == "zero" or cache_code == code.lower()):
        return res_util.fail("验证码错误")
    exist = UserVO.query.filter_by(username=username).first()
    if exist:
        return jsonify(res_util.fail("用户名已经存在"))
    password = data.get('password', '')
    vo = UserVO(username=username, password=password_util.get_sha256_salt_password(password))
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("注册成功"))


@sys_api.route('/add_announcement', methods=['POST'])
def add_announcement():
    """
    添加公告
    ---
    tags:
     - sys
    consumes: ["multipart/form-data"]
    produces: ["application/json"]
    parameters:
      - in: formData
        name: title
        type: string
        required: true
        description: 公告标题
        example: 优化bug...
      - in: formData
        name: content
        type: string
        required: true
        description: 内容
        example: bug是...
      - in: formData
        name: image
        description: 配图
        required: false
        type: file
        example: 选择一个图片
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
    """
    title = request.form.get('title')
    content = request.form.get('content')
    image = request.files['image']
    time_str = time.strftime('%Y%m%d_%H%M%S_') + str(random.randint(1000, 9999))
    image_path = UPLOAD_FILE_PATH + '/images/' + time_str + "-" + image.filename
    image.save(image_path)  # 保存文件到指定路径
    user_id = user_service.get_id_by_token()
    vo = AnnouncementVO(userid=user_id, title=title, content=content, images=image_path)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))


@sys_api.route('/get_announcement_list', methods=['GET'])
def get_announcement_list():
    """
    获取历史公告列表
    ---
    tags:
      - sys
    responses:
      500:
        description: server err
      200:
        description: success
    """
    message_list = list(AnnouncementVO.query.order_by(AnnouncementVO.create_time).all())
    message_list = [marshal(vo, announcement_fields) for vo in message_list]
    return jsonify(res_util.success(message_list))


@sys_api.route('/get_announcement_by_id', methods=['GET'])
def get_announcement_by_id():
    """
    获取历史公告
    ---
    tags:
      - sys
    parameters:
     - name: id
       type: integer
       required: true
       description: 公告的id
       in: query
       example: 1
    responses:
      500:
        description: server err
      200:
        description: success
    """
    announcement_id = request.args.get('id')
    vo = AnnouncementVO.query.filter_by(id=announcement_id).first()
    return jsonify(res_util.success(marshal(vo, announcement_fields)))


@sys_api.route('/add_suggest', methods=['POST'])
def add_suggest():
    """
    添加反馈
    ---
    tags:
      - sys
    parameters:
       - in: formData
         name: content
         type: string
         required: true
         description: 建议内容
         example: 建议...
       - in: formData
         name: image
         type: file
         required: false
         description: 配图
       - name: id
         type: integer
         in: formData
         required: true
         description: 公告的id
         example: 1
    responses:
       500:
         description: server err
       200:
         description: success
    """
    announcement_id = request.form.get("id")
    content = request.form.get('content')
    try:
        image = request.files('image')
    except:
        image = ""
    vo = MessageVO(announcement_id=announcement_id, content=content, image=image)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))


@sys_api.route('/get_suggest', methods=['GET'])
def get_suggest():
    """
    获取反馈
    ---
    tags:
      - sys
    parameters:
      - name: announcement
        type: integer
        in: query
        required: true
        description: 公告的id
        example: 1
    responses:
      500:
        description: server err
      200:
         description: success
    """
    announcement_id = request.args.get("id")
    message_list = MessageVO.query.filter_by(id=announcement_id).order_by(MessageVO.create_time).all()
    return jsonify(res_util.success(message_list))
