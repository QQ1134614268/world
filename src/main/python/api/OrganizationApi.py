# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 9:35
# @Author  : huangran
"""
from flask import Blueprint, jsonify, make_response, request
from flask_restful import fields, marshal

from service import UserService
from config import res
from db.db import db
from vo.OrganizationVO import OrganizationVO

organization_api = Blueprint("organization_api", __name__, url_prefix='/organization_api')

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

# todo 组织不控制权限,,,  查询时候权限控制, 提供权限控制接口??
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
    user_id = UserService.get_current_userid()
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
    data = request.get_json()
    parent_id = data.get('id')
    name = data.get('name')
    code = data.get('code')
    parent_vo = OrganizationVO.query.filter_by(id=parent_id).first()
    full_path_code = parent_vo.full_path_code + code + "/"
    full_name = parent_vo.full_name + name + "/"
    level = parent_vo.level + 1
    vo = OrganizationVO(name=name, parent_id=parent_id, level=level, full_name=full_name, full_path_code=full_path_code)
    db.session.add(vo)
    db.session.flush()
    vo.full_path_id = parent_vo.full_path_id + str(vo.id) + "/"
    db.session.commit()
    return jsonify(res.success("操作成功"))


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
          修改级组织
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
    data = request.get_json()
    vo_id = data.get('id')
    name = data.get('name')
    code = data.get('code')
    vo = OrganizationVO.query.filter_by(id=vo_id).first()
    full_name = vo.full_name
    name_index = vo.full_name.rfind("/", 0, -1)
    full_name_new = vo.full_name[0:name_index] + "/" + name + "/"
    full_path_code = vo.full_path_code
    code_index = vo.full_path_code.rfind("/", 0, -1)
    full_path_code_new = vo.full_path_code[0:code_index] + "/" + code + "/"
    db.session.query(OrganizationVO).filter(OrganizationVO.id == vo_id).update({"name": name, "code": code})
    sql = 'UPDATE organization SET full_name = REPLACE(full_name,"%s","%s"),full_path_code=REPLACE(full_path_code,"%s","%s") WHERE full_name like "%s" ' % (
        full_name, full_name_new, full_path_code, full_path_code_new, full_name)
    db.session.execute(sql)
    db.session.commit()
    return jsonify(res.success("操作成功"))


@organization_api.route('/move_organization', methods=['POST'])
def move_organization():
    """
    移动组织
    ---
    tags:
     - organization_api
    parameters:
      - in: body
        name: body
        description:
          移动组织
        required: true
        schema:
          id: move_organization
          required:
            - id
            - parent_id
          properties:
            id:
              description: organization的id
              type: integer
              example: 2
            parent_id:
              description: organization的id
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
    vo = OrganizationVO.query.filter_by(id=vo_id).first()
    parent_vo = OrganizationVO.query.filter_by(id=parent_id).first()
    full_name = vo.full_name
    full_name_new = parent_vo.full_name
    full_path_code = vo.full_path_code
    full_path_code_new = parent_vo.full_path_code
    full_path_id = vo.full_path_id
    full_path_id_new = parent_vo.full_path_id
    db.session.query(OrganizationVO).filter(OrganizationVO.id == vo_id).update({"parent_id": parent_id})
    sql = 'UPDATE organization SET full_path_id = REPLACE(full_path_id,"%s","%s"),full_name = REPLACE(full_name,"%s","%s"),full_path_code = REPLACE(full_path_code, "%s", "%s") WHERE full_name like "%s"' % (
    full_path_id, full_path_id_new,
    full_name, full_name_new, full_path_code, full_path_code_new, full_name)
    db.session.execute(sql)
    db.session.commit()
    return jsonify(res.success("操作成功"))


@organization_api.route('/delete_organization', methods=['POST'])
def delete_organization():
    """
    删除当前组织及子级组织
    ---
    tags:
     - organization_api
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
              description: organization的id
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
    sql = 'DELETE FROM organization where full_path_id like "%s"' % ("%" + str(vo_id) + "%")
    print(sql)
    db.session.execute(sql)
    db.session.commit()
    return jsonify(res.success("操作成功"))


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
