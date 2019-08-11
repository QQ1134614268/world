# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:35
# @Author  : huangran
"""
from flask import Blueprint, jsonify, make_response, request
from flask_restful import fields, marshal

from config import jwt_config
from config import res
from db.db import db
from vo.OrganizationVO import OrganizationVO

organization_api = Blueprint("organization_api", __name__, url_prefix='/organization_api')

# todo 创建起源 , 创建子级组织  ,,前端or后端创建子级full_name,level变量?
organization_fields = {
    'id': fields.Integer,
    'parent_id': fields.Integer,
    'name': fields.String,
    'level': fields.Integer,
    'full_name': fields.String,
    'full_path_code': fields.String,
    'full_path_id': fields.String,
    'leader': fields.Integer,
}


@organization_api.route('/get_origin_organization', methods=['GET'])
def get_origin_organization():
    """
    获取origin级组织
    ---
    tags:
     - organization_api
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    user_id = jwt_config.get_current_userid()
    # auth 组织权限 user_id
    # 组织下有组织,和人员,,类 文件和文件夹
    vo = OrganizationVO.query.filter_by(id=1).first()
    return jsonify(res.success(marshal(vo, organization_fields)))


@organization_api.route('/add_children_organization', methods=['POST'])
def add_children_organization():
    """
    添加子级组织
    ---
    tags:
     - organization_api
    parameters:
      - in: body
        name: body
        description:
          创建子级组织
        required: true
        schema:
          id: organization
          required:
            - name
            - code
            - id
          properties:
            id:
              description: 当前组织id
              type: integer
              example: 1
            name:
              description: 组织名
              type: string
              example: 问题部
            code:
              description: 唯一编码
              type: string
              example: problem_department
    responses:
      500:
        description: server Error !
      200:
        description: success
     """
    # 同级不重复
    data = request.get_json()
    parent_id = data.get('id')
    name = data.get('name')
    code = data.get('code')
    parent_vo = OrganizationVO.query.filter_by(id=parent_id).first()
    # parent_vo
    full_path_code = parent_vo.full_path_code + code + "/"
    full_name = parent_vo.full_name+ name + "/"
    full_path_id = parent_vo.full_path_id + code + "/"
    level = parent_vo.level + 1
    vo = OrganizationVO(name=name, parent_id=parent_id, level=level, full_name=full_name, full_path_code=full_path_code,
                        full_path_id=full_path_id)
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
      - in: body
        name: body
        description:
          创建子级组织
        required: true
        schema:
          id: organization
          required:
            - name
            - code
            - id
          properties:
            id:
              description: 当前组织id
              type: integer
              example: 1
            name:
              description: 组织名
              type: string
              example: 问题部
            code:
              description: 唯一编码
              type: string
              example: problem_department
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
    index = vo.full_name.rfind("/")
    full_name = vo.full_name[0:index] + "/" + name + "/"
    #  todo 子级组织都要修改 ??? 正则表达事
    vo = OrganizationVO(name=name, full_name=full_name, code=code)
    db.session.add(vo)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/delete_organization', methods=['POST'])
def delete_organization():
    """
    删除子级组织
    ---
    tags:
     - organization_api
    parameters:
     - name: id
       in: query
       type: integer
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
    #  todo 子级组织都要删除 ??? 正则表达事

    obj = OrganizationVO(id=vo_id)
    db.session.delete(obj)
    db.session.commit()
    return make_response(jsonify(res.success("操作成功")))


@organization_api.route('/get_child_organization', methods=['GET'])
def get_child_organization():
    """
    获取子级组织
    ---
    tags:
     - organization_api
    parameters:
     - name: id
       in: query
       type: integer
       description: 要查的组织id
       example: 1
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    vo_id = request.args.get('id')
    parent_vo_list = OrganizationVO.query.filter_by(parent_id=vo_id)
    data_list = [marshal(i, organization_fields) for i in parent_vo_list]
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
       type: integer
       description: 要移动的组织id
     - name: parent_id
       in: query
       type: integer
       description: 要移动到的组织id
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
     """
    # 同级不重复
    data = request.get_json()

    # todo 修改父级子级关系 冗余数据 full 都要修改
    vo_id = data.get('id')
    parent_id = data.get('parent_id')
    return make_response(jsonify(res.success("操作成功")))
