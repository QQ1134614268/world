# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:33
# @Author  : huangran
"""

from flask import Blueprint, jsonify, make_response, request, send_file
from config import res
from db.db import db
from .AreaVO import AreaVO

area_api = Blueprint("area_api", __name__, url_prefix='/area_api')


@area_api.route('/add_origin', methods=['POST'])
def add_origin():
    """
    添加起源
    ---
    tags:
     - area_api
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
    # 同级不重复
    name = data.get('name')
    level = 0
    vo = AreaVO(name=name, level=level, video=1)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))
