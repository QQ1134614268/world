# encoding: utf-8
"""
@author:huangran
"""
import random
import time

from flask import Blueprint, jsonify, make_response, request
from flask_restful import fields, marshal

from config import res
from service import UserService
from db.db import db
from vo.UserVO import AnnouncementVO, MessageVO

sys_api = Blueprint("sys", __name__, url_prefix='/sys')

announcement_fields = {
    'id': fields.Integer,
    'userid': fields.Integer,
    'content': fields.String,
    'images': fields.String
}


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
    from app import PROJECT_DIR
    # todo 路径表达式与平台
    image_path = PROJECT_DIR + '/data/upload/images/' + time_str + "-" + image.filename
    image.save(image_path)  # 保存文件到指定路径
    user_id = UserService.get_current_userid()
    vo = AnnouncementVO(userid=user_id, title=title, content=content, images=image_path)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res.success("操作成功"))


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
    message_list = list(AnnouncementVO.query.order_by(AnnouncementVO.createTime).all())
    message_list = [marshal(vo, announcement_fields) for vo in message_list]
    return jsonify(res.success(message_list))


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
    return jsonify(res.success(marshal(vo, announcement_fields)))


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
    # todo file单独传输
    try:
        image = request.files('image')
    except:
        image = ""
    vo = MessageVO(announcement_id=announcement_id, content=content, image=image)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res.success("操作成功"))


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
    message_list = MessageVO.query.filter_by(id=announcement_id).order_by(MessageVO.createTime).all()
    return jsonify(res.success(message_list))
