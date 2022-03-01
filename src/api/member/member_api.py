# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request, Blueprint, send_file
from flask_restful import Resource
from sqlalchemy import func

import service.user_service
import util.unique_util
from config.enum_conf import StoreMemberType, OrderStatus
from config.mysql_db import db
from util import res_util, time_util
from util.tree_code_util import make_code
from vo.member_model import StoreVO, StoreMemberTable, GoodsVO, OrderVO, QrCodeVO
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


# todo StoreMemberListApi 合并
class StoreMemberListApi(Resource):

    def get(self, _id):
        query = [StoreMemberTable.store_id == request.args.get("store_id")]
        vos = UserVO.query.outerjoin(StoreMemberTable, UserVO.id == StoreMemberTable.user_id).filter(*query).all()
        return res_util.success(vos)


class OrderApi(Resource):

    def post(self, _id):
        data = request.get_json()
        user_id = service.user_service.get_id_by_token()
        order_code = util.unique_util.get_uuid()
        create_time = time_util.get_now_str()
        for item in data:
            goods = GoodsVO.query.filter(GoodsVO.id == item["id"]).first()
            new_data = {
                'goods_name': item["name"],
                'user_id': user_id,
                'goods_id': item["id"],
                'num': item["num"],
                'store_id': item["store_id"],
                'price': goods.price * item.get("num"),
                'order_code': order_code,
                'table_id': item.get("store_id"),
                'create_time': create_time,
                'goods_img': goods.images,
            }
            db.session.add(OrderVO(**new_data))
        db.session.commit()
        return res_util.success(order_code)

    def get(self, _id):
        if _id:
            vo = OrderVO.query.filter(OrderVO.id == _id).first()
            return res_util.success(vo)

        order_code = request.args.get("order_code")
        if order_code:
            vos = OrderVO.query.filter(OrderVO.order_code == order_code).order_by(OrderVO.create_time.desc()).all()
            return res_util.success(vos)

        user_id = service.user_service.get_id_by_token()
        store_id = request.args.get("store_id")

        vos = OrderVO.query.filter(
            OrderVO.user_id == user_id,
            OrderVO.store_id == store_id,
        ).with_entities(
            OrderVO.order_code,
            OrderVO.status,
            func.any_value(OrderVO.create_time).label('create_time')
        ).group_by(
            OrderVO.order_code,
            OrderVO.status,
            OrderVO.create_time,
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
        vo = QrCodeVO.query.filter(QrCodeVO.id == _id).first()
        if not vo:
            return res_util.fail("资源不存在")
        img = make_code(vo.url_dic, url=vo.url, img_path=vo.img_path, img_width=vo.img_width, img_height=vo.img_height)
        return send_file(img, mimetype='image/png')

    def put(self, _id):
        data = request.get_json()
        vo = QrCodeVO.query.filter(QrCodeVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(vo.id)


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
            query = OrderVO.query.filter(OrderVO.store_id == store_id)
            user_id = request.args.get("user_id")
            if user_id:
                query.filter(OrderVO.store_id == store_id)
            vos = query.order_by(OrderVO.create_time.desc()).all()
            return res_util.success(vos)

    @staticmethod
    @order_api.route('/get_order_by_table_id/<int:_id>', methods=['GET'])
    def get_order_by_table_id(_id):
        store_id = request.args.get("store_id")
        table_id = request.args.get("table_id")
        if table_id:
            order = OrderVO.query.filter(
                OrderVO.table_id == table_id,
                OrderVO.store_id == store_id,
                OrderVO.status == OrderStatus.UN_PAYMENT.UN_PAYMENT,
            ).order_by(OrderVO.create_time.desc()).all()
            return res_util.success(order)
