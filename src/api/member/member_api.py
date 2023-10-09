# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request, Blueprint
from flask_restful import Resource
from sqlalchemy import func

import service.user_service
import util.unique_util
from config.enum_conf import StoreMemberType, OrderStatus
from config.mysql_db import db
from util import res_util, time_util
from vo.member_model import StoreVO, StoreMemberTable, GoodsVO, OrderInfoVO, QrCodeVO, OrderVO


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


class OrderApi(Resource):

    def post(self, _id):
        data = request.get_json()
        user_id = service.user_service.get_id_by_token()
        order_code = util.unique_util.get_uuid()
        create_time = time_util.get_now_str()
        order_vo = OrderVO(
            store_id=data[0].get("store_id"),
            table_id=data[0].get("table_id"),
            order_code=order_code
        )
        db.session.add(order_vo)
        db.session.flush()
        for item in data:
            goods = GoodsVO.query.filter(GoodsVO.id == item["id"]).first()

            new_data = {
                'goods_name': item["name"],
                'user_id': user_id,
                'goods_id': item["id"],
                'num': item["num"],
                'order_id': order_vo.id,
                'price': goods.price * item.get("num"),
                'create_time': create_time,
                'goods_img': goods.images,
            }
            db.session.add(OrderInfoVO(**new_data))
        db.session.commit()
        return res_util.success(order_code)

    def get(self, _id):
        if _id:
            vo = OrderInfoVO.query.filter(OrderInfoVO.id == _id).first()
            return res_util.success(vo)

        order_code = request.args.get("order_code")
        if order_code:
            vos = OrderInfoVO.query.filter(OrderInfoVO.order_code == order_code).order_by(
                OrderInfoVO.create_time.desc()).all()
            return res_util.success(vos)

        user_id = service.user_service.get_id_by_token()
        store_id = request.args.get("store_id")

        vos = OrderVO.query.filter(
            OrderVO.user_id == user_id,
            OrderVO.store_id == store_id,
        ).with_entities(
            OrderVO.order_code,
            OrderVO.status,
            func.any_value(OrderInfoVO.create_time).label('create_time')
        ).group_by(
            OrderVO.order_code,
            OrderVO.status,
            OrderInfoVO.create_time,
        ).order_by(
            OrderVO.create_time.desc()
        ).all()
        return res_util.success(vos)


class QrCodeApi(Resource):

    def post(self, _id):
        data = request.get_json()
        vo = QrCodeVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        if _id:
            vo = QrCodeVO.query.filter(QrCodeVO.id == _id).first()
            return res_util.success(vo)
        vos = QrCodeVO.query.all()
        return res_util.success(vos)

        # img = make_code(vo.url_dic, url=vo.url, img_path=vo.img_path, img_width=vo.img_width, img_height=vo.img_height)
        # return send_file(img, mimetype='image/png')

    def put(self, _id):
        data = request.get_json()
        vo = QrCodeVO.query.filter(QrCodeVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(vo.id)


# todo
# 思考 订单, 厨师, 商家, 顾客,不同的页面,订单接口

order_api = Blueprint("order", __name__, url_prefix='/api/member/order_api')


class OrderBlueprintApi(Resource):

    @staticmethod
    @order_api.route('/get_order_by_type/<int:_id>', methods=['GET'])
    def get_order_by_type(_id):
        cur_id = service.user_service.get_id_by_token()
        store_id = request.args.get("store_id")
        user_type = StoreMemberTable.query.filter(
            StoreMemberTable.store_id == store_id,
            StoreMemberTable.user_id == cur_id
        ).with_entities(StoreMemberTable.user_type).scalar()  # 登陆用户角色? 店长,普通用户
        # user_type = request.args.get('user_type')  # 登陆角色??todo
        # user_type = request.args.get('user_type')  # 根据权限 厨师? 每个节点 厨房 集群
        worker_list = [None, StoreMemberType.Kitchen.name, StoreMemberType.Admin.name,
                       StoreMemberType.NormalEmp.name, StoreMemberType.StoreAdmin.name]
        if user_type in worker_list:  # todo  permission_required
            query = OrderInfoVO.query.filter(OrderInfoVO.store_id == store_id)
            user_id = request.args.get("user_id")
            if user_id:
                query.filter(OrderInfoVO.store_id == store_id)
            vos = query.order_by(OrderInfoVO.create_time.desc()).all()
            return res_util.success(vos)

    @staticmethod
    @order_api.route('/get_order_by_table_id/<int:_id>', methods=['GET'])
    def get_order_by_table_id(_id):
        store_id = request.args.get("store_id")
        table_id = request.args.get("table_id")
        if table_id:
            order = OrderInfoVO.query.filter(
                OrderInfoVO.table_id == table_id,
                OrderInfoVO.store_id == store_id,
                OrderInfoVO.status == OrderStatus.UN_PAYMENT.UN_PAYMENT,
            ).order_by(OrderInfoVO.create_time.desc()).all()
            return res_util.success(order)
