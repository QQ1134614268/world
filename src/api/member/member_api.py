# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource

import service.user_service
from config.enum_conf import StoreMemberType, OrderStatus
from config.mysql_db import db
from util import res_util
from vo.member_model import StoreVO, StoreMemberTable, GoodsVO, OrderVO
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

        vos = GoodsVO.query.filter(*query_filter).order_by(GoodsVO.label).all()  # todo 标签排序 连表
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

    def get(self, _id):
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
        user_id = service.user_service.get_id_by_token()
        for item in data:
            new_data = {
                'goods_name': item["name"],
                'user_id': user_id,
                'goods_id': item["id"],
                'num': item["num"],
                'store_id': item["store_id"],
                'total_price': price_dic.get(item["id"]) * item.get("num"),
            }
            db.session.add(OrderVO(**new_data))
        db.session.commit()
        return res_util.success()

    def get(self, _id):
        if _id:
            vo = OrderVO.query.filter(OrderVO.id == _id).first()
            return res_util.success(vo)
        user_id = service.user_service.get_id_by_token()
        store_id = request.args.get("store_id")

        table_id = request.args.get("table_id")
        if table_id:
            order = OrderVO.query.filter(
                OrderVO.table_id == table_id,
                OrderVO.status == OrderStatus.UN_PAYMENT.UN_PAYMENT,
                OrderVO.user_id == user_id,
            ).order_by(OrderVO).first()
            return res_util.success(order)
        # user_type 用户类型
        user_type = StoreMemberTable.query.filter(
            StoreMemberTable.store_id == store_id, StoreMemberTable.user_id == user_id
        ).with_entities(StoreMemberTable.user_type).scalar()  # 登陆用户角色? 店长,普通用户
        # user_type = request.args.get('user_type')  # 登陆角色??todo
        # user_type = request.args.get('user_type')  # 根据权限 厨师? 每个节点 厨房 集群
        customer_list = [None, StoreMemberType.NormalVip.name, StoreMemberType.HighVip.name,
                         StoreMemberType.TopVip.name]
        if user_type in customer_list:
            vos = OrderVO.query.filter(OrderVO.user_id == user_id, OrderVO.store_id == store_id).order_by(
                OrderVO.create_time.desc()
            ).all()
            return res_util.success(vos)
        worker_list = [None, StoreMemberType.Kitchen.name, StoreMemberType.Admin.name,
                       StoreMemberType.NormalEmp.name, StoreMemberType.StoreAdmin.name]
        if user_type in worker_list:
            vos = OrderVO.query.filter(OrderVO.store_id == store_id).order_by(
                OrderVO.create_time.desc()
            ).all()
            return res_util.success(vos)


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
