# -*- coding:utf-8 -*-
"""
@Time: 2021/2/21
@Description:
"""
from config.exception import WorldException
from config.mysql_db import db
from vo.member_model import WalletVO


class WeiXinPay:

    # 跳转支付
    def pay(self):
        pass

    # 出示付款码,用户扫描
    def pay2(self):
        pass

    # 扫描用户的收款码
    def pay3(self):
        pass


class ZhiFuBaoPay:

    # 跳转支付
    def pay(self):
        pass

    # 出示付款码,用户扫描
    def pay2(self):
        pass

    # 扫描用户的收款码
    def pay3(self):
        pass


# 内部钱包支付
def pay(wallet_id, money):
    vo = WalletVO.query.filter(WalletVO.id == wallet_id).with_for_update().first()
    if vo.money - money >= 0:
        vo.money -= money
        db.session.commit()
    else:
        db.session.commit()
        raise WorldException("余额不足")
    return money
