# -*- coding:utf-8 -*-
"""
@Time: 2021/2/21
@Description:
"""
from config.mysql_db import db

from vo.table_model import WalletVO


def pay(wallet_id, money):
    vo = WalletVO.query.filter(WalletVO.id == wallet_id).with_for_update().first()
    if vo.money - money >= 0:
        vo.money -= money
        db.session.commit()
    else:
        db.session.commit()
        assert Exception, "余额不足"
    return money
