import time
from service.alipay2 import ali_pay_service

class AlipayApi(object):
    def __init__(self, app_id, notify_url, return_url, merchant_private_key_path, alipay_public_key_path,debug):
        """
        :param app_id:
        :param notify_url:支付宝post回调地址，用来修改订单信息
        :param return_url:支付宝get回调地址，用来给用户展示
        :param merchant_private_key_path:商户的私钥
        :param alipay_public_key_path:支付宝的公钥
        """
        self.app_id = app_id
        self.notify_url = notify_url
        self.return_url = return_url
        self.merchant_private_key_path = merchant_private_key_path
        self.alipay_public_key_path = alipay_public_key_path
        self.debug=debug
        self.alipay = ali_pay_service(
            appid=app_id,
            app_notify_url=notify_url,
            return_url=return_url,
            app_private_key_path=merchant_private_key_path,
            alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
            debug=debug,  # 默认False,
        )

    def getAlipayPage(self,subject,total_amount,out_trade_no,):
        """
        :param subject: 商品简单描述
        :param total_amount: 交易总金额(单位: 元 保留俩位小数)
        :param out_trade_no: 商户订单号
        :return: 支付宝支付页面
        """
        query_params = self.alipay.direct_pay(
            subject=subject,
            out_trade_no=out_trade_no,
            total_amount=total_amount,
        )
        if self.debug:
            pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
        else:
            pay_url = "https://openapi.alipay.com/gateway.do?{}".format(query_params)
        return pay_url

    def alipayCallbackPost(self,body_str):
        """
        :param body_str: post回调的数据
        :return:
        """
        from urllib.parse import parse_qs
        post_data = parse_qs(body_str)
        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        # 做二次验证
        sign = post_dict.pop('sign', None)
        # 通过调用alipay的verify方法去认证
        status = self.alipay.verify(post_dict, sign)
        if status:
            # 修改自己订单状态
            return True
        else:
            return False

    def alipayCallbackGet(self,params):
        """
        :param params: get回调的数据
        :return:
        """
        dic_params = {k: v for k, v in params.items()}
        sign = dic_params.pop('sign', None)
        status = self.alipay.verify(dic_params, sign)
        if status:
            return True
        else:
            return False


if __name__ == '__main__':
    app_id = "填写自己的"
    notify_url = "填写自己的"
    return_url = "填写自己的"
    merchant_private_key_path = "app_private_2048.txt"
    alipay_public_key_path = "alipay_public_2048.txt"
    ali=AlipayApi(app_id=app_id,
                  notify_url=notify_url,
                  return_url=return_url,
                  merchant_private_key_path=merchant_private_key_path,
                  alipay_public_key_path=alipay_public_key_path,
                  debug=True)

    subject="充气娃娃"
    out_trade_no="OFG"+str(time.time())
    total_amount=1000
    url=ali.getAlipayPage(subject=subject,out_trade_no=out_trade_no,total_amount=total_amount)
    print(url)