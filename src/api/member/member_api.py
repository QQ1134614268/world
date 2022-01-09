# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource

import service.user_service
from config.mysql_db import db
from service import wallet_service
from util import res_util
from vo.member_model import StoreVO, StoreMemberTable, WalletVO, GoodsVO, OrderVO
from vo.table_model import UserVO


class StoreApi(Resource):

    def post(self):
        data = request.get_json()
        data['user_id'] = service.user_service.get_id_by_token()
        vo = StoreVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success()

    def get(self, _id):
        vo = StoreVO.query.filter(StoreVO.id == request.args.get("id")).first()
        return res_util.success(vo)

    def put(self, _id):
        data = request.get_json()
        StoreVO.query.filter(StoreVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        model = StoreVO.query.filter(StoreVO.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)


class GoodsApi(Resource):

    def get(self, _id):
        query_filter = []
        if _id:
            query_filter.append(GoodsVO.id == _id)
        if request.args.get("store_id"):
            query_filter.append(GoodsVO.store_id == request.args.get("store_id"))

        vos = GoodsVO.query.filter(*query_filter).all()
        return res_util.success(vos)

    def post(self, _id):
        data = request.get_json()
        model = GoodsVO(**data)
        db.session.add(model)
        db.session.commit()
        return res_util.success(model.id)

    def put(self, _id):
        data = request.get_json()
        GoodsVO.query.filter(GoodsVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        model = GoodsVO.query.filter(GoodsVO.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)


class StoreMemberApi(Resource):

    def post(self):
        data = request.get_json()
        vo = StoreMemberTable(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        vo = StoreMemberTable.query.filter(StoreVO.id == _id).first()
        return res_util.success(vo)

    def put(self, _id):
        data = request.get_json()
        StoreMemberTable.query.filter(StoreMemberTable.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        model = StoreMemberTable.query.filter(StoreMemberTable.id == _id).first()
        db.session.delete(model)
        db.session.commit()
        return res_util.success(_id)


class StoreMemberListApi(Resource):

    def get(self):
        query = [StoreMemberTable.store_id == request.args.get("store_id")]
        vos = UserVO.query.outerjoin(StoreMemberTable, UserVO.id == StoreMemberTable.user_id).filter(*query).all()
        return res_util.success(vos)


class StoreListApi(Resource):
    def get(self):
        vos = StoreVO.query.all()
        return res_util.success(vos)


class GoodsListApi(Resource):

    def get(self):
        query = [GoodsVO.store_id == request.args.get("store_id")]
        goods_list = GoodsVO.query.filter(*query).all()
        return res_util.success(goods_list)


class OrderApi(Resource):

    def post(self, _id):
        data = request.get_json()
        goods = GoodsVO.query.filter(GoodsVO.id.in_([item["id"] for item in data])).all()
        price_dic = {item.id: item.price for item in goods}
        money = sum([item["num"] * price_dic.get(item.id) for item in data])
        user_id = service.user_service.get_id_by_token()
        wallet = WalletVO.query.filter(WalletVO.user_id == user_id).one()
        wallet_service.pay(wallet.id, money)

        vos = [OrderVO(user_id=user_id, goods_id=item["id"], num=item["num"]) for item in data]
        db.session.add_all(vos)
        db.session.commit()
        return res_util.success()

    def get(self, _id):
        vo = GoodsVO.query.filter(GoodsVO.id == _id).all()
        return res_util.success(vo)


class OrderListApi(Resource):

    def get(self):
        # 获取用户订单
        user_id = service.user_service.get_id_by_token()
        res = OrderVO.query.outerjoin(
            GoodsVO, OrderVO.goods_id == GoodsVO.id
        ).filter(
            OrderVO.user_id == user_id).with_entities(
            GoodsVO.id,
            GoodsVO.name,
            OrderVO.num,
        ).all()
        ret = [dict(zip(item.keys(), item)) for item in res]
        return res_util.success(ret)
