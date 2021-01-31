# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource
from flask_restful import fields, marshal

from config.mysql_db import db
from service import user_service
from util import password_util
from util import res_util
from vo.table_model import GoodsVO
from vo.table_model import StoreVO, StoreMemberTable

goods_field = {
    "id": fields.Integer,
    "price": fields.Float,
    "duration": fields.Float,
    "describe": fields.String,
    "images": fields.String,
    "name": fields.String,
}
store_field = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "name": fields.String,
}
store_member_field = {
    "id": fields.Integer,
    "store_id": fields.Integer,
    "user_id": fields.Integer,
}


class StoreApi(Resource):

    def post(self):
        data = request.get_json()
        name = data.get('name', '')
        password = data.get('password', '')
        vo = StoreVO(name=name, password=password_util.get_sha256_salt_password(password),
                     user_id=user_service.get_id_by_token())
        db.session.add(vo)
        db.session.commit()
        return res_util.success(marshal(vo, store_field))

    def get(self, _id):
        vo = StoreVO.query.filter(StoreVO.id == request.args.get("id")).first()
        return res_util.success(marshal(vo, store_field))

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
        vo = GoodsVO.query.filter(GoodsVO.id == _id).first()
        return res_util.success(marshal(vo, goods_field))

    def post(self):
        data = request.get_json()
        model = GoodsVO(**data).save()
        return res_util.success(model.id)

    def put(self, _id):
        data = request.get_json()
        # GoodsVO(id=_id).update(_id, data)
        # db.session.query().filter(GoodsVO.id == _id).update(data)
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
        return res_util.success(marshal(vo, store_member_field))

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


class StoreListApi(Resource):
    def get(self):
        vo = StoreVO.query.all()
        return res_util.success(marshal(vo, store_field))


class GoodsListApi(Resource):

    def get(self):
        goods_list = GoodsVO.query.all()
        return res_util.success([marshal(vo, goods_field) for vo in goods_list])


class StoreMemberApi(Resource):

    def get(self, _id):
        vo = StoreMemberTable.query.all()
        return res_util.success(marshal(vo, store_member_field))
