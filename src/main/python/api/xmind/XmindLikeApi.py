# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/28 0:35
"""

from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal

from config import res
from db.db import db
from service import UserService
from vo.XmindVO import XmindLikeVO

x_mind_like_api = Blueprint("x_mind_like_api", __name__, url_prefix='/x_mind_like_api')

organization_fields = {
    'id': fields.Integer,
    'parent_id': fields.Integer,
    'name': fields.String,
    'content': fields.Integer,
    'sort': fields.String,
}


@x_mind_like_api.route('/add_children_message', methods=['POST'])
def add_children_message():
    """
    添加子级组织
    ---
    tags:
     - x_mind_like_api
    parameters:
      - in: body
        name: body
        description:
          创建子级组织
        required: true
        schema:
          id: x_mind_like_vo
          required:
            - id
            - content
          properties:
            id:
              description: 父级id
              type: integer
              example: 1
            name:
              description: 记录的内容
              type: string
              example: 问题部
    responses:
      500:
        description: server Error !
      200:
        description: success
     """
    data = request.get_json()
    parent_id = data.get('id')
    content = data.get('content')
    # sort = data.get('sort')
    user_id = UserService.get_current_userid()
    vo = XmindLikeVO(content=content, parent_id=parent_id, user_id=user_id)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res.success("操作成功"))


@x_mind_like_api.route('/update_content', methods=['POST'])
def update_content():
    """
    修改内容
    ---
    tags:
     - x_mind_like_api
    parameters:
      - in: body
        name: body
        description:
          创建子级组织
        required: true
        schema:
          id: x_mind_like_vo
          required:
            - id
            - content
          properties:
            id:
              description: 父级id
              type: integer
              example: 1
            name:
              description: 记录的内容
              type: string
              example: 问题部
    responses:
      500:
        description: server Error !
      200:
        description: success
     """
    data = request.get_json()
    vo_id = data.get('id')
    content = data.get('content')
    XmindLikeVO.filter(XmindLikeVO.id == vo_id).update({"content": content})
    db.session.commit()
    return jsonify(res.success("操作成功"))


@x_mind_like_api.route('/move_content', methods=['POST'])
def move_content():
    """
    移动组织
    ---
    tags:
     - x_mind_like_api
    parameters:
      - in: body
        name: body
        description:
          移动结构
        required: true
        schema:
          required:
            - id
            - parent_id
          properties:
            id:
              description: 当前节点的id
              type: integer
              example: 2
            parent_id:
              description: 移动到的节点的id
              type: integer
              example: 3
    responses:
      200:
        description: Successful operation
      400:
        description: Invalid input
     """
    data = request.get_json()
    vo_id = data.get('id')
    parent_id = data.get('parent_id')
    XmindLikeVO.filter(XmindLikeVO.id == vo_id).update({"parent_id": parent_id})
    db.session.commit()
    return jsonify(res.success("操作成功"))


@x_mind_like_api.route('/delete_content', methods=['POST'])
def delete_content():
    """
    删除当前组织及子级组织
    ---
    tags:
     - x_mind_like_api
    parameters:
      - in: body
        name: body
        description:
          删除当前组织及子级组织
        required: true
        schema:
          required:
            - id
          properties:
            id:
              description: _content的id
              type: integer
              example: 2
    responses:
      200:
        description: Successful operation
      400:
        description: Invalid input
     """
    data = request.get_json()
    vo_id = data.get('id')
    sql = 'DELETE FROM _content where full_path_id like "%s"' % ("%" + str(vo_id) + "%")
    db.session.execute(sql)
    db.session.commit()
    return jsonify(res.success("操作成功"))


@x_mind_like_api.route('/get_child_content', methods=['GET'])
def get_child_content():
    """
    获取子级组织
    ---
    tags:
     - x_mind_like_api
    parameters:
     - name: id
       in: query
       type: integer
       description: 要查的id
       example: 1
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    vo_id = request.args.get('id')
    vo = XmindLikeVO.query.filter_by(parent_id=vo_id)
    data_list = [marshal(i, _content_fields) for i in parent_vo_list]
    return jsonify(res.success(data_list))


@x_mind_like_api.route('/get_content_all', methods=['GET'])
def get_content_all():
    # todo
    pass
