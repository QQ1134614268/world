# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource
from flask_restful import fields, marshal

# 用户创建 store
# store下创建会员
# 会员添加人
# 系统--会员vo,用户vo,...
#  假设存在某些条件  todo  用户--商店--vip-vip会员-钱包   用户查看会员
from service import user_service
from config.mysql_db import db
from util import res_util
from util.encrypt_util import SHA256Util
from .vo import StoreMemberTable, WalletVO
from .vo import StoreVO

from util import password_util
class StoreApi(Resource):

    def post(self):
        field = {
            "id": fields.Integer,
            "user_id": fields.Integer,
            "name": fields.String,
        }
        data = request.get_json()
        name = data.get('name', '')
        password = data.get('password', '')
        vo = StoreVO(name=name, password=password_util.get_sha256_salt_password(password), user_id=user_service.get_id_by_token())
        db.session.add(vo)
        db.session.commit()
        return res_util.success(marshal(vo, field))

    def get(self):
        field = {
            "id": fields.Integer,
            "user_id": fields.Integer,
            "name": fields.String,
        }
        if request.args.get("id"):
            vo = StoreVO.query.filter(StoreVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, field))

        vos = StoreVO.query.filter(StoreVO.user_id == user_service.get_id_by_token()).all()
        ret = [marshal(vo, field) for vo in vos]
        return res_util.success(ret)


class StoreMemberApi(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id', '')
        store_id = data.get('store_id', '')
        vo = StoreMemberTable(user_id=user_id, store_id=store_id)
        db.session.add(vo)
        db.session.add(WalletVO(user_id=user_id, store_id=store_id))
        db.session.commit()
        return res_util.success(vo.id)

    def get(self):
        field = {
            "id": fields.Integer,
            "user_id": fields.Integer,
            "store_id": fields.String,
        }
        if request.args.get("id"):
            vo = StoreMemberTable.query.filter(StoreVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, field))

        if request.args.get("store_id"):
            vos = StoreMemberTable.query.filter(StoreMemberTable.store_id == request.args.get("store_id")).all()
            ret = [marshal(vo, field) for vo in vos]
            return res_util.success(ret)


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
        field = {
            "id": fields.Integer,
            "user_id": fields.Integer,
            "money": fields.Float,
        }
        if  request.args.get("id"):
            vo = WalletVO.query.filter(WalletVO.id == request.args.get("id")).first()
            return res_util.success(marshal(vo, field))
        if  request.args.get("user_id"):
            vo = WalletVO.query.filter(WalletVO.user_id == request.args.get("user_id")).first()
            return res_util.success(marshal(vo, field))
