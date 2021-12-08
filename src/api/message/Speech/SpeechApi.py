# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/30 23:13

"""
from flask import Blueprint, jsonify, request

from config.mysql_db import db
from util import res_util
from vo.table_model import RecordVO, CommentVO

speech_api = Blueprint("speech", __name__, url_prefix='/api/speech')


@speech_api.route('/add_record', methods=['POST'])
def add_record():
    content = request.form.get('content')
    image = request.files.get('image')
    video = request.files.get('video')
    user_id = request.form.get('user_id')
    vo = RecordVO(user_id=user_id, content=content, image=image, video=video)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))


@speech_api.route('/add_comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    record_id = data.get('id')
    content = data.get('content')
    vo = CommentVO(record_id=record_id, content=content)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))


@speech_api.route('/get_record_all', methods=['GET'])
def get_record_all():
    message_list = RecordVO.query.order_by(RecordVO.create_time).limit(10)
    return jsonify(res_util.success(message_list))


@speech_api.route('/get_record_by_id', methods=['GET'])
def get_record():
    record_id = request.args.get('id')
    message_list = CommentVO.query.filter_by(record_id=record_id).order_by(CommentVO.create_time).all()
    return jsonify(res_util.success(message_list))
