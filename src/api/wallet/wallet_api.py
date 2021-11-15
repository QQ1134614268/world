# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource
from flask_restful import fields, marshal

from service import WalletService
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
        return res_util.success(WalletService.pay(wallet_id, money))

    def get(self):
        if request.args.get("id"):
            vo = WalletVO.query.filter(WalletVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, wallet_field))
        if request.args.get("user_id"):
            vo = WalletVO.query.filter(WalletVO.user_id == request.args.get("user_id")).first()
            return res_util.success(marshal(vo, wallet_field))
