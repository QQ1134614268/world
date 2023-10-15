# -*- coding:utf-8 -*-
"""
@Time: 2021/12/23
@Description:
"""
from flask import request
from flask_restful import Resource

from service.user_service import get_id_by_token
from util import res_util
from vo.table_model import LogVO


class LogApi(Resource):

    def get(self, _id):
        page = request.args.get("currentPage", 1, int)
        page_size = request.args.get("pageSize", 10, int)

        vos = LogVO.query.filter(
            LogVO.user_id == get_id_by_token(),
        ).order_by(
            LogVO.create_time.desc()
        ).paginate(page=page, per_page=page_size)
        return res_util.success(vos)
