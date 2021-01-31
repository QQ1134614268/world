# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource
from flask_restful import fields, marshal

from config.mysql_db import db
from util import res_util
from vo.table_model import WalletVO

wallet_field = {
    "id": fields.Integer,
    "store_id": fields.Integer,
    "user_id": fields.Integer,
}


class WalletApi(Resource):
    def put(self):
        data = request.get_json()
        money = data.get('money', '')
        wallet_id = data.get('id', '')
        # todo 查看sql语句 检验正确性
        vo = WalletVO.query.filter(WalletVO.id == wallet_id).with_for_update().first()
        if vo.money + money > 0:
            vo.money += money
        db.session.commit()
        return res_util.success(vo.money)

    def get(self):
        if request.args.get("id"):
            vo = WalletVO.query.filter(WalletVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, wallet_field))
        if request.args.get("user_id"):
            vo = WalletVO.query.filter(WalletVO.user_id == request.args.get("user_id")).first()
            return res_util.success(marshal(vo, wallet_field))
