# encoding: utf-8
"""
@author:huangran
"""
from flask import Blueprint, jsonify, make_response, request, json
from config import res
from db.db import db
from vo.user import AnnouncementVO, MessageVO
import time

sys_api = Blueprint("sys", __name__, url_prefix='/sys')


# 添加公告
@sys_api.route('/add_announcement', methods=['POST'])
def add_announcement():
    """
       sys
       ---
       tags:
         - sys
       parameters:
         - name: title
           in: path
           type: string
           required: true
           description: The language name
         - name: content
           in: query
           type: integer
           description: size of awesomeness
         - name: image
           in: query
           type: file
           description: size of awesomeness
       """
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
@sys_api.route('/get_announcement', methods=['GET'])
def get_announcement():
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    ---
    tags:
      - sys
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
    """
    message_list = list(AnnouncementVO.query.order_by(AnnouncementVO.createTime).all())
    #  todo bug : return list
    # message_list = [obj.__dict__ for obj in message_list]
    print(type(message_list[0]))
    # list_0 = [lambda  x : x .__dict__ for x in range(5)]
    message_list = [x for x in message_list]

    # json_str = json.dumps(message_list, default=lambda obj: obj.__dict__)
    # print(json_str)
    # return make_response(jsonify(res.success(message_list)))
    return  jsonify(res.success(message_list))

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
