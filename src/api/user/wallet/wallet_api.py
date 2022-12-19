# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource

from service import wallet_service
from util import res_util
from vo.member_model import WalletVO


class WalletApi(Resource):
    def put(self):
        data = request.get_json()
        money = data.get('money', '')
        wallet_id = data.get('id', '')
        return res_util.success(wallet_service.pay(wallet_id, money))

    def get(self):
        if request.args.get("id"):
            vo = WalletVO.query.filter(WalletVO.id == request.args.get("id")).first()
            return res_util.success(vo)
        if request.args.get("user_id"):
            vo = WalletVO.query.filter(WalletVO.user_id == request.args.get("user_id")).first()
            return res_util.success(vo)
