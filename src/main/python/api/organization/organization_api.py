# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:35
# @Author  : huangran
"""
from flask import Blueprint, jsonify, make_response, request, send_file
from config import res
from db.db import db
from vo.user import RecordVO, CommentVO
from .OrganizationVO import OrganizationVO

organization_api = Blueprint("organization_api", __name__, url_prefix='/organization_api')


# todo 创建起源 , 创建子级组织  ,,前端or后端创建子级full_name,level变量?

@organization_api.route('/add_origin', methods=['POST'])
def add_origin():
    """
    组织
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
    vo = OrganizationVO(name=name, code=code,level=level, full_name=full_name, full_path=full_path)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/add_children_organization', methods=['POST'])
def add_children_organization():
    """
    组织
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
    parent_id = data.get('parent_id')
    name = data.get('name')
    code = data.get('code')
    parent_vo = OrganizationVO.query.filter_by(id=parent_id)
    full_name = parent_vo["full_name"] + name + "/"
    # todo
    full_path = parent_vo["full_path"] + code + "/"
    level = parent_vo["level"] + 1
    vo = OrganizationVO(name=name, level=level, full_name=full_name, full_path=full_path)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/update_organization', methods=['POST'])
def update_organization():
    """
    组织
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
     - name: id
       in: query
       type: file
       description: id
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()
    parent_id = data.get('parent_id')
    vo_id = data.get('id')
    parent_vo = OrganizationVO.query.filter_by(id=parent_id)
    # UserVO.query.filter_by(username=username, password=UserVO.get_password(password)).first()
    name = data.get('name')
    code = data.get('code')
    vo = OrganizationVO.query.filter_by(id=vo_id)
    full_name = parent_vo["full_name"] + name + "/"
    # todo
    full_path = parent_vo["full_path"] + code + "/"
    level = parent_vo["level"] + 1
    vo = OrganizationVO(name=name, level=level, full_name=full_name, full_path=full_path)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/delete_organization', methods=['POST'])
def delete_organization():
    """
    组织
    添加子级组织
    ---
    tags:
     - organization_api
    parameters:
     - name: id
       in: query
       type: file
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
    return make_response(jsonify(res.success("操作成功")))


