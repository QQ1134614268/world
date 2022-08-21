# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request, Blueprint

from util import res_util
from vo.member_model import OrderInfoVO

cooker_order_api = Blueprint(__name__, __name__, url_prefix='/api/member/cooker_order_api')


@cooker_order_api.route('/get_cooker_order', methods=['GET'])
def get_cooker_order():
    query = OrderInfoVO.query
    cooker_status = request.args.get("cooker_status")
    if cooker_status:
        query.filter(OrderInfoVO.cooker_status == cooker_status)
    # store_id = request.args.get("store_id")
    # assert store_id is not None
    # if store_id:
    #     query.filter(OrderInfoVO.store_id == store_id)
    vos = query.order_by(OrderInfoVO.create_time.desc()).all()
    return res_util.success(vos)
