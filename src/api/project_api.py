# -*- coding:utf-8 -*-
"""
@Time: 2020/12/14
@Description: 
"""

from flask import request
from flask_restful import Resource

from config.data import user_data2, user_data
from config.mysql_db import db
from util import res_util
from util.video_util import get_first_frame_loc
from vo.table_model import WorksVO


def init():
    user_data2, user_data
    pass


def ref_first_frame_loc():
    vos = WorksVO.query.all()
    for vo in vos:
        vo.thumbnail = get_first_frame_loc(vo.file)
    db.session.commit()


class ProjectInit(Resource):
    code = {"video": "更新视频缩略图"}
    code2 = {"video": ref_first_frame_loc}

    def get(self):
        func_code = request.args.get("code")
        if func_code:
            ProjectInit.code2[func_code]()
            return res_util.success(func_code)
        return ProjectInit.code
