# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/24 15:51
"""
import json
from base64 import decodebytes, encodebytes
from datetime import datetime
from urllib.parse import quote_plus

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from service.alipay import Config


class AliPay():
    """
    支付宝支付接口(PC端支付接口)
    """

    def __init__(self, debug=False):
        self.appid = Config.APPID
        self.app_notify_url = Config.NOTIFY_URL  # 如果支付成功，支付宝会向这个地址发送POST请求（校验是否支付已经完成）
        self.return_url = Config.RETURN_URL  # 如果支付成功，重定向回到你的网站的地址。
        self.debug = True  # 默认False

        self.app_private_key_path = Config.PRI_KEY_PATH  # 应用私钥
        self.app_private_key = None
        with open(self.app_private_key_path,mode="r",encoding="utf_8") as fp:
            self.app_private_key = RSA.importKey(fp.read())

        self.alipay_public_key_path = Config.PUB_KEY_PATH  # 支付宝公钥
        with open(self.alipay_public_key_path) as fp:
            self.alipay_public_key = RSA.importKey(fp.read())

        if debug is True:
            self.__gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.__gateway = "https://openapi.alipay.com/gateway.do"

    def direct_pay(self, subject, out_trade_no, total_amount, return_url=None, **kwargs):
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "FAST_INSTANT_TRADE_PAY",
            # "qr_pay_mode":4
        }
        biz_content.update(kwargs)
        data = {
            "app_id": self.appid,
            "method": "alipay.trade.page.pay",
            "charset": "utf-8",
            "sign_type": "RSA2",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0",
            "biz_content": json.dumps(biz_content, separators=(',', ':'))
        }

        if self.return_url is not None:
            data["notify_url"] = self.app_notify_url
            data["return_url"] = self.return_url
        data.pop("sign", None)
        # 排序后的字符串
        unsigned_items = [(k, v) for k, v in data.items()]
        unsigned_string = "&".join("{0}={1}".format(k, v) for k, v in unsigned_items)
        unsigned_string=unsigned_string.encode("utf-8")
        # 开始计算签名
        key = self.app_private_key
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(SHA256.new(unsigned_string))
        # base64 编码，转换为unicode表示并移除回车
        sign = encodebytes(signature).decode("utf8").replace("\n", "")
        # ordered_items = self.ordered_data(data)
        quoted_string = "&".join("{0}={1}".format(k, quote_plus(v)) for k, v in unsigned_items)

        # 获得最终的订单信息字符串
        signed_string = quoted_string + "&sign=" + quote_plus(sign)

        return signed_string

    # def ordered_data(self, data):
    #     complex_keys = []
    #     for key, value in data.items():
    #         if isinstance(value, dict):
    #             complex_keys.append(key)
    #
    #     # 将字典类型的数据dump出来
    #     for key in complex_keys:
    #         data[key] = json.dumps(data[key], separators=(',', ':'))
    #
    #     return sorted([(k, v) for k, v in data.items()])

    def _verify(self, raw_content, signature):
        # 开始计算签名
        key = self.alipay_public_key
        signer = PKCS1_v1_5.new(key)
        digest = SHA256.new()
        digest.update(raw_content.encode("utf8"))
        if signer.verify(digest, decodebytes(signature.encode("utf8"))):
            return True
        return False

    def verify(self, data, signature):
        if "sign_type" in data:
            sign_type = data.pop("sign_type")
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        message = "&".join(u"{}={}".format(k, v) for k, v in unsigned_items)
        return self._verify(message, signature)
