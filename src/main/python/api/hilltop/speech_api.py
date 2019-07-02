# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/30 23:13
# @Author  : huangran
"""
from flask import Blueprint, jsonify, make_response, request
from config import res
from db.db import db
from vo.user import RecordVO, CommentVO

speech_api = Blueprint("speech_api", __name__, url_prefix='/sys')


# 添加日志
@speech_api.route('/add_record', methods=['POST'])
def add_record():
    content = request.POST.get('content')
    images = request.POST.get('images')
    video = request.POST.get('video')
    vo = RecordVO(content=content, images=images, video=video)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@speech_api.route('/add_comment', methods=['POST'])
def add_comment():
    content = request.POST.get('content')
    vo = CommentVO(content=content)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@speech_api.route('/get_record_all', methods=['GET'])
def get_record_all():
    # 获取所有日志加评论
    message_list = RecordVO.query.order_by(RecordVO.createTime).all()
    return make_response(jsonify(res.success(message_list)))


@speech_api.route('/get_record', methods=['GET'])
def get_record():
    # 获取日志
    message_list = RecordVO.query.order_by(RecordVO.createTime).all()
    return make_response(jsonify(res.success(message_list)))
