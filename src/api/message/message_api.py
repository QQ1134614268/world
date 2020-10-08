# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal

from api.message.vo import PersonSpeech
from api.user.user_type import UserType
from config.mysql_db import db
from config.orm_config import DateTime
from service import user_service
from util import res_util

message_api = Blueprint("message_api", __name__, url_prefix='/api/message_api')

speechFields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'create_time': DateTime
}


# 个人发表
@message_api.route('/add_speech', methods=['POST'])
def add_speech():
    data = request.get_json()
    title = data.get('title', '')
    content = data.get('content', '')
    group = data.get('group', '')
    userId = user_service.get_id_by_token()
    vo = PersonSpeech(title=title, content=content, userId=userId, group=group)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success(vo.id))


@message_api.route('/get_my_speech', methods=['GET'])
def get_my_speech():
    userId = user_service.get_id_by_token()
    parent_vo_list = PersonSpeech.query.filter_by(userId=userId).all()
    data_list = [marshal(i, speechFields) for i in parent_vo_list]
    return jsonify(res_util.success(data_list))


@message_api.route('/get_speech_all', methods=['GET'])
def get_speech_all():
    parent_vo_list = PersonSpeech.query.order_by(PersonSpeech.create_time.desc())
    data_list = [marshal(i, speechFields) for i in parent_vo_list]
    return jsonify(res_util.success(data_list))


@message_api.route('/get_speech_by_id', methods=['GET'])
def get_speech_by_id():
    speech_id = request.args.get("id")
    vo = PersonSpeech.query.filter(PersonSpeech.id == speech_id).first()
    return jsonify(res_util.success(marshal(vo, speechFields)))


@message_api.route('/get_other_user_speech', methods=['GET'])
def get_other_user_speech():
    # TODO 时间 所有好友 分组可视
    attentionList = user_service.getAttentionList()
    attentionIds = [attenion.userId for attenion in attentionList]
    parent_vo_list = PersonSpeech.query.filter_by(PersonSpeech.userId.in_(attentionIds), )  # todo group
    data_list = [marshal(i, speechFields) for i in parent_vo_list]
    return jsonify(res_util.success(data_list))


@message_api.route('/getSpeechByUserId', methods=['GET'])
def getSpeechByUserId():
    userId = request.args.get('userId')
    parent_vo_list = PersonSpeech.query.filter_by(userId=userId)
    data_list = [marshal(i, speechFields) for i in parent_vo_list]
    return jsonify(res_util.success(data_list))


@message_api.route('/delete_speech', methods=['POST'])
def delete_speech():
    data = request.get_json()
    content = data.get('content', '')
    group = data.get('group', '')
    user_id = user_service.get_id_by_token()
    vo = PersonSpeech(content=content, user_id=user_id, group=group)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("操作成功"))


@message_api.route('/addAnnouncement', methods=['POST'])
def addAnnouncement():
    data = request.get_json()
    content = data.get('content', '')
    userId = user_service.get_id_by_token()
    vo = PersonSpeech(content=content, userId=userId, group=UserType.strange.value)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success(vo.id))


@message_api.route('/getAnnouncementByUserId', methods=['GET'])
def getAnnouncementByUserId():
    userId = request.args.get('userId')
    parent_vo_list = PersonSpeech.query.filter_by(userId=userId)
    data_list = [marshal(i, speechFields) for i in parent_vo_list]
    return jsonify(res_util.success(data_list))
