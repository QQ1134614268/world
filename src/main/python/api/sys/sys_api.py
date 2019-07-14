# encoding: utf-8
"""
@author:huangran
"""
from flask import Blueprint, Response
from flask import jsonify, make_response, request, json
from config import res
from db.db import db
from vo.user import AnnouncementVO, MessageVO
import time

sys_api = Blueprint("sys", __name__, url_prefix='/sys')


# 添加公告
@sys_api.route('/addAnnouncement', methods=['POST'])
def add_announcement():
    title = request.form.get('title')
    content = request.form.get('content')
    image = request.files['image']

    t = time.strftime('%Y%m%d_%H%M%S')
    from app import PROJECT_DIR
    image_path = PROJECT_DIR + '/data/upload/images/' + t + "-" + image.filename
    image.save(image_path)  # 保存文件到指定路径
    # with open("a.jpg","wb") as f:
    #     f.write(images.read())
    vo = AnnouncementVO(title=title, content=content, images=image_path)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


# 公告栏
@sys_api.route('/getAnnouncement', methods=['GET'])
def get_announcement():
    message_list = list(AnnouncementVO.query.order_by(AnnouncementVO.createTime).all())
    return make_response(jsonify(res.success(message_list)))


# 意见栏
@sys_api.route('/add_suggest', methods=['POST'])
def add_suggest():
    data = request.get_json()
    content = data.get('content')
    images = data.get('images')
    vo = MessageVO(content=content, images=images)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


# 公告栏
@sys_api.route('/get_suggest', methods=['GET'])
def get_suggest():
    message_list = MessageVO.query.order_by(MessageVO.createTime).all()
    return make_response(jsonify(res.success(message_list)))
