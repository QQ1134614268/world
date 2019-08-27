# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/24 15:55
"""

from flask import Blueprint, jsonify, request, redirect

from config import res
from service.alipay import AliPayService

ali_pay_api = Blueprint("ali_pay_api", __name__, url_prefix='/ali_pay_api')

# todo 增加商品表,订单表,然后购买
@ali_pay_api.route('/pay_for_product', methods=['POST', "GET"])
def pay_for_product():
    """
    添加起源
    ---
    tags:
     - ali_pay_api
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
    # data = request.get_json()
    # 数据库有一条订单记录,未支付
    # out_trade_no = data.get('out_trade_no')
    print(999)
    out_trade_no = "candy20190824_123"
    # 查询数据库,获取金额,主题
    money = 100
    subject = "糖果"
    # user_id = data.get('user_id')

    alipay = AliPayService.AliPay()

    query_params = alipay.direct_pay(
        subject=subject,  # 商品简单描述
        out_trade_no=out_trade_no,  # 商户订单号
        total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
    )

    pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
    result = redirect(pay_url)
    return result


@ali_pay_api.route('/add_origin', methods=['POST'])
def update_order():
    from urllib.parse import parse_qs

    body_str = request.body.decode('utf-8')
    post_data = parse_qs(body_str)

    post_dict = {}
    for k, v in post_data.items():
        post_dict[k] = v[0]

    alipay = AliPayService.AliPay()

    sign = post_dict.pop('sign', None)
    status = alipay.verify(post_dict, sign)
    if status:
        # 1. 获取订单号
        out_trade_no = post_dict.get('out_trade_no')
        # 2. 根据订单号将数据库中的数据进行更新
        return jsonify(res.success("操作成功"))
    else:
        return jsonify(res.success("fail"))


@ali_pay_api.route('/add_origin', methods=['POST'])
def pay_result(request):
    """
    支付完成后，跳转回的地址
    :param request:
    :return:
    """
    params = request.GET.dict()
    sign = params.pop('sign', None)

    alipay = AliPayService.AliPay()
    # 校验支付是否成功
    status = alipay.verify(params, sign)

    if status:
        return jsonify(res.success("支付成功"))
    return jsonify(res.success("支付失败"))
