# encoding: utf-8
"""
@author:huangran
"""
from flask import Blueprint, Response
from flask import jsonify, make_response, request, json
from config import res
from db.db import db
from vo.user import AnnouncementVO, MessageVO

sys_api = Blueprint("sys", __name__, url_prefix='/sys')


# 添加公告
@sys_api.route('/addAnnouncement', methods=['POST'])
def add_announcement():
    title = request.POST.get('title')
    content = request.POST.get('content')
    images = request.POST.get('images')
    vo = AnnouncementVO(title=title, content=content, images=images)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


# 公告栏
@sys_api.route('/getAnnouncement', methods=['GET'])
def get_announcement():
    message_list = AnnouncementVO.query.order_by(MessageVO.createTime).all()
    return make_response(jsonify(res.success(message_list)))


# 意见栏
@sys_api.route('/addAnnouncement', methods=['POST'])
def add_suggest():
    content = request.POST.get('content')
    images = request.POST.get('images')
    vo = MessageVO(content=content, images=images)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


# 公告栏
@sys_api.route('/getSuggest', methods=['GET'])
def get_suggest():
    message_list = MessageVO.query.order_by(MessageVO.createTime).all()
    return make_response(jsonify(res.success(message_list)))
