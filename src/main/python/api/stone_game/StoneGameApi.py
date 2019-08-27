# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/27 21:20
"""
from flask import Blueprint, redirect, request

from service import UserService
from service.alipay import AliPayService
from .GameSquare import Game

stone_game_api = Blueprint("stone_game_api", __name__, url_prefix='/stone_game_api')

game = Game()


@stone_game_api.route('/pay_for_product', methods=['POST'])
def pay_for_product():
    """
    添加起源
    ---
    tags:
     - stone_game_api
    parameters:
      - in: body
        name: body
        description:
          配置权限
        required: true
        schema:
          required:
            - out_trade_no
          properties:
            out_trade_no:
              description: 订单号
              type: string
              example: candy20190824_123
    responses:
      200:
        description: Successful operation
      400:
        description: Invalid input
     """
    data = request.get_json()
    # 数据库有一条订单记录,未支付
    out_trade_no = data.get('out_trade_no')
    # 查询数据库,获取金额,主题
    money = 100
    subject = "糖果"
    user_id = UserService.get_current_userid()

    alipay = AliPayService.AliPay()

    query_params = alipay.direct_pay(
        subject=subject,  # 商品简单描述
        out_trade_no=out_trade_no,  # 商户订单号
        total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
    )

    pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
    result = redirect(pay_url)
    return result
