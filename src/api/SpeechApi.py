# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/30 23:13

"""
from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal

from util import ResUtil
from db.db import db
from vo.UserVO import RecordVO, CommentVO

speech_api = Blueprint("speech", __name__, url_prefix='/speech')
record_fields = {
    'user_id': fields.Integer,
    'content': fields.String,
    'image': fields.String,
    'video': fields.String
}
comment_fields = {
    'record_id': fields.Integer,
    'content': fields.String,
}


@speech_api.route('/add_record', methods=['POST'])
def add_record():
    """
    添加言论
    ---
    tags:
     - speech_api
    parameters:
      - in: formData
        name: user_id
        type: integer
        required: true
        description: 用户id
        example: 1
      - in: formData
        name: image
        type: file
        required: false
        description: upload a image file
      - in: formData
        name: video
        type: file
        required: false
        description: upload a image file11
      - in: formData
        name: content
        description: 言论
        required: true
        type: string
        example: 我发现...
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    content = request.form.get('content')
    try:
        image = request.files('image')
    except:
        image = ""
    try:
        video = request.files('video')
    except:
        video = ""
    user_id = request.form.get('user_id')
    vo = RecordVO(user_id=user_id, content=content, image=image, video=video)
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("操作成功"))


@speech_api.route('/add_comment', methods=['POST'])
def add_comment():
    """
    添加评论
    ---
    tags:
     - speech_api
    parameters:
      - in: body
        name: body
        description:
          评论
        required: true
        schema:
          id: comment
          required:
            - id
            - content
          properties:
            id:
              description: 评论id
              type: integer
              example: 1
            title:
              description: 一句评论
              type: string
              example: 我认为
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    data = request.get_json()
    record_id = data.get('id')
    content = data.get('content')
    vo = CommentVO(record_id=record_id, content=content)
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("操作成功"))


@speech_api.route('/get_record_all', methods=['GET'])
def get_record_all():
    """
    获取所有言论
    ---
    tags:
     - speech_api
    parameters:
      - in: query
        name: id
        description: 用户id
        example: 1
        require: true
    responses:
      500:
        description:  server error!!!
      200:
        description: success
     """
    # 获取所有日志加评论
    user_id = request.args.get("id")
    message_list = RecordVO.query.filter_by(user_id=user_id).order_by(RecordVO.createTime).all()
    message_list = [marshal(vo, record_fields) for vo in message_list]
    return jsonify(ResUtil.success(message_list))


@speech_api.route('/get_record_by_id', methods=['GET'])
def get_record():
    """
    获取所有言论
    ---
    tags:
     - speech_api
    parameters:
      - in: query
        name: id
        description: 言论id
        example: 1
        require: true
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
    """
    record_id = request.args.get('id')
    message_list = CommentVO.query.filter_by(record_id=record_id).order_by(CommentVO.createTime).all()
    message_list = [marshal(vo, comment_fields) for vo in message_list]
    return jsonify(ResUtil.success(message_list))
