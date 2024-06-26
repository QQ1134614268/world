# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from functools import reduce

from flask import request, Blueprint
from flask_restful import Resource
from sqlalchemy import and_

import service.user_service
import util.unique_util
from config.enum_conf import OrderStatus
from config.mysql_db import db
from util import res_util
from util.to_class_util import to_class
from vo.member_model import StoreVO, GoodsVO, OrderInfoVO, QrCodeVO, OrderVO
from vo.table_model import EnumConfig

order_api = Blueprint("order", "order", url_prefix='/api/member/order_api')
goods_api = Blueprint("goods", "goods", url_prefix='/api/member/goods_api')


class GoodsApi(Resource):

    def get(self, _id):
        query_filter = []
        if _id:
            query_filter.append(GoodsVO.id == _id)
        if request.args.get("store_id"):
            query_filter.append(GoodsVO.store_id == request.args.get("store_id"))

        vo = GoodsVO.query.filter(*query_filter).first()
        return res_util.success(vo)

    @staticmethod
    @goods_api.route('/page', methods=['GET'])
    def page():
        req = request.args
        page = req.get("currentPage", 1, int)
        page_size = req.get("pageSize", 10, int)
        query = GoodsVO.query \
            .outerjoin(EnumConfig, and_(EnumConfig.value == GoodsVO.type_id, EnumConfig.group_code == 'FOOD_ENUM')) \
            .add_entity(EnumConfig)
        #            .add_columns(GoodsVO.id, EnumConfig.comment)\
        page_data = query.order_by(GoodsVO.create_time.desc()).paginate(page=page, per_page=page_size)
        for vo1, vo2 in page_data.items:
            vo1.type_name = vo2 and vo2.label
        page_data.items = [vo1 for vo1, vo2 in page_data.items]
        return res_util.success(page_data)

    def post(self, _id):
        data = request.get_json()
        data = {k: v for k, v in data.items() if k in GoodsVO.__dict__.keys()}
        model = GoodsVO(**data)
        db.session.add(model)
        db.session.commit()
        return res_util.success(model.id)

    def put(self, _id):
        data = request.get_json()
        data = {k: v for k, v in data.items() if k in GoodsVO.__dict__.keys()}
        GoodsVO.query.filter(GoodsVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        GoodsVO.query.filter(GoodsVO.id == _id).delete()
        db.session.commit()
        return res_util.success(_id)


class OrderApi(Resource):

    def post(self, _id):
        data = request.get_json()
        order_vo = to_class(data, OrderVO)
        order_vo.user_id = service.user_service.get_id_by_token()
        order_vo.order_code = util.unique_util.get_uuid()
        order_vo.status = OrderStatus.UN_PAYMENT.name
        # order_vo.store_id =
        order_vo.total_price = reduce(lambda x, y: x + y,
                                      map(lambda v: v.get("price") * v.get("num"), data["info_list"]))
        db.session.add(order_vo)
        db.session.flush()
        for info in data["info_list"]:
            del info["id"]
            info["order_id"] = order_vo.id
            order_info = to_class(info, OrderInfoVO)
            db.session.add(order_info)
        db.session.commit()
        return res_util.success(order_vo.id)

    def get(self, _id):
        req = request.args
        query = OrderInfoVO.query
        if _id:
            query.filter(OrderVO.id == _id)
        if req.get("user_id"):
            query.filter(OrderVO.user_id == req.get("user_id"))
        vo = query.first()
        return res_util.success(vo)

    @staticmethod
    @order_api.route('/page', methods=['GET'])
    def page():
        req = request.args
        page = request.args.get("currentPage", 1, int)
        page_size = request.args.get("pageSize", 10, int)
        query = OrderVO.query
        # 根据角色查询, 如果是商家, 用户, 系统管理员 get_role()
        # 数据来源 StoreMemberTable  StoreMemberType
        if req.get("user_id"):  # 用户
            query.filter(OrderVO.user_id == req.get("user_id"))
        if req.get('store_id'):  # 商家
            query.filter(OrderVO.store_id == req.get("store_id"))
        if req.get('table_id'):  # 桌号
            query.filter(OrderVO.table_id == req.get("table_id"))
        if req.get("is_admin"):  # 默认
            pass
        page_data = query.order_by(OrderVO.create_time.desc()).paginate(page=page, per_page=page_size)
        for vo in page_data.items:
            vo.info_list = OrderInfoVO.query.filter(OrderInfoVO.order_id == vo.id).all()
        return res_util.success(page_data)


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
