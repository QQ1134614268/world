# 类似微信  --  在线消息 ,离线消息

from flask import Blueprint, jsonify, request, redirect

from config import res
from service.alipay import AliPayService
from geventwebsocket.websocket import WebSocket

wx_api = Blueprint("wx_api", __name__, url_prefix='/wx_api')

user_dict = {}  # 空字典,用来存放用户名和发送消息


# # 发送在线消息
@wx_api.route('/send_message', methods=['POST' ])
def pay_for_product():

    return


# # 登录获取消息
@wx_api.route('/get_unread_message', methods=['POST', "GET"])
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



#