# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:35
# @Author  : huangran
"""
from flask import Blueprint, jsonify, make_response, request
from config import res
from db.db import db
from api.organization.OrganizationVO import OrganizationVO
from flask_restful import fields, marshal_with, marshal

organization_api = Blueprint("organization_api", __name__, url_prefix='/organization_api')


# todo 创建起源 , 创建子级组织  ,,前端or后端创建子级full_name,level变量?

@organization_api.route('/add_origin', methods=['POST'])
def add_origin():
    """
    添加起源
    ---
    tags:
     - organization_api
    parameters:
     - name: name
       in: path
       type: string
       required: true
       description: name
     - name: code
       in: query
       type: file
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()
    name = data.get('name')
    code = data.get('code')
    level = 0
    full_name = "/" + name + "/"
    # todo
    full_path = "/" + code + "/"
    vo = OrganizationVO(name=name, code=code, level=level, full_name=full_name, full_path=full_path)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/add_children_organization', methods=['POST'])
def add_children_organization():
    """
    添加子级组织
    ---
    tags:
     - organization_api
    parameters:
     - name: name
       in: path
       type: string
       required: true
       description: name
     - name: code
       in: query
       type: file
       description: code
     - name: parent_id
       in: query
       type: file
       description: parent_id
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()
    vo_id = data.get('id')
    name = data.get('name')
    code = data.get('code')
    parent_vo = OrganizationVO.query.filter_by(id=vo_id)
    full_name = parent_vo["full_name"] + name + "/"
    # todo
    full_path = parent_vo["full_path"] + code + "/"
    level = parent_vo["level"] + 1
    vo = OrganizationVO(name=name, parent_id=vo_id, level=level, full_name=full_name, full_path=full_path)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/update_organization', methods=['POST'])
def update_organization():
    """
    修改级组织
    ---
    tags:
     - organization_api
    parameters:
     - name: name
       in: path
       type: string
       required: true
       description: name
     - name: code
       in: query
       type: string
       description: code
     - name: id
       in: query
       type: int
       description: id
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()
    vo_id = data.get('id')
    name = data.get('name')
    code = data.get('code')
    vo = OrganizationVO.query.filter_by(id=vo_id)
    index = vo["full_name"].rfind("/")
    full_name = vo["full_name"][0:index] + "/" + name + "/"
    vo = OrganizationVO(name=name, full_name=full_name, code=code)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/delete_organization', methods=['POST'])
def delete_organization():
    """
    添加子级组织
    ---
    tags:
     - organization_api
    parameters:
     - name: id
       in: query
       type: int
       description: id
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()
    vo_id = data.get('id')
    obj = OrganizationVO(id=vo_id)
    db.session.delete(obj)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/get_child_organization', methods=['POST'])
def get_child_organization():
    """
    获取子级组织
    ---
    tags:
     - organization_api
    parameters:
     - name: id
       in: query
       type: file
       description: 要查的组织id
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()
    vo_id = data.get('id')
    parent_vo_list = OrganizationVO.query.filter_by(parent_id=vo_id)
    todo_fields = {
        'id': fields.Integer,
        'userid': fields.Integer,
        'content': fields.String,
        'images': fields.String
    }
    data_list = [marshal(parent_vo_list, todo_fields) for i in parent_vo_list]
    return jsonify(res.success(data_list))


@organization_api.route('/move_organization', methods=['POST'])
def move_organization():
    """
    移动组织
    ---
    tags:
     - organization_api
    parameters:
     - name: id
       in: query
       type: int
       description: 要移动的组织id
     - name: parent_id
       in: query
       type: int
       description: 要移动到的组织id
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()
    vo_id = data.get('id')
    parent_id = data.get('parent_id')
    # todo
    return make_response(jsonify(res.success("操作成功")))
