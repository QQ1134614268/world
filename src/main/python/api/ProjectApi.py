# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/11 22:16
"""
from flask import Blueprint, make_response, jsonify

from config import res
from db.db import db
from vo.OrganizationVO import OrganizationVO

world_project_api = Blueprint("project_api", __name__, url_prefix='/project_api')


# 项目数据库初始化,定时任务


@world_project_api.route('/project_api', methods=['POST'])
def project_init():
    """
    项目数据库初始化
    ---
    tags:
      - world_project_api
    responses:
      500:
        description: server Error !
      200:
        description: success
    """
    message = "init- "
    if not OrganizationVO.query.filter_by(id=1).first():
        vo = OrganizationVO(id=1, code="origin", parent_id=0, name="W&G company", level=0, full_name="/W&G company/",
                            full_path_code="/origin/", full_path_id="/1/")
        db.session.add(vo)
        db.session.commit()
        message += "组织初始化成功;"

    return jsonify(res.success(message))
