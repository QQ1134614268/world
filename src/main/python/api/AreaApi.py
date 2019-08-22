# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:33
# @Author  : huangran
"""

from flask import Blueprint, jsonify, request

from config import res
from db.db import db
from vo.AreaVO import AreaVO

area_api = Blueprint("area_api", __name__, url_prefix='/area_api')


@area_api.route('/add_origin', methods=['POST'])
def add_origin():
    """
    添加起源
    ---
    tags:
     - area_api
    parameters:
     - name: name
       type: string
       required: true
       description: content
     - name: images
       type: file
       description: a image
     - name: video
       type: file
       description: video
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    name = request.form.get('name')
    image = request.files['image']
    video = request.files['video']
    level = 0
    vo = AreaVO(name=name, level=level, video=1)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res.success("操作成功"))
