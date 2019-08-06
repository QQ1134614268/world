# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/30 23:13
# @Author  : huangran
"""
from flask import Blueprint, jsonify, make_response, request
from config import res
from db.db import db
from vo.user import RecordVO, CommentVO

speech_api = Blueprint("speech", __name__, url_prefix='/speech')


# 添加日志
@speech_api.route('/add_record', methods=['POST'])
def add_record():
    """
    添加言论
    ---
    tags:
     - speech_api
    parameters:
     - name: content
       in: path
       type: string
       required: true
       description: content
     - name: images
       in: query
       type: file
       description: a image
     - name: video
       in: query
       type: file
       description: video
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    data = request.get_json()
    content =data.get('content')
    images = data.get('images')
    video =data.get('video')
    vo = RecordVO(content=content, images=images, video=video)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@speech_api.route('/add_comment', methods=['POST'])
def add_comment():
    """
    添加评论
    ---
    tags:
     - speech_api
    parameters:
     - name: content
       in: path
       type: string
       required: true
       description: content
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    data = request.get_json()
    content = data.get('content')
    vo = CommentVO(content=content)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@speech_api.route('/get_record_all', methods=['GET'])
def get_record_all():
    """
    获取所有言论
    ---
    tags:
     - speech_api
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 获取所有日志加评论
    message_list = RecordVO.query.order_by(RecordVO.createTime).all()
    return make_response(jsonify(res.success(message_list)))


@speech_api.route('/get_record', methods=['GET'])
def get_record():
    """
    获取所有言论
    ---
    tags:
     - speech_api
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
    """
    message_list = RecordVO.query.order_by(RecordVO.createTime).all()
    return make_response(jsonify(res.success(message_list)))

