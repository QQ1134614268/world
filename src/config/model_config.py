# -*- coding:utf-8 -*-
"""
@Time: 2021/10/23
@Description:
"""
from flask import request

from config.mysql_db import db
from util import res_util


class Res:
    @staticmethod
    def add(obj, data):
        if isinstance(data, list):
            return ResList.delete_list(obj, data)
        vo = obj(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    @staticmethod
    def update(_id, obj, data):
        if not _id:
            return ResList.update_list(obj, data)
        obj.query.filter(obj.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    @staticmethod
    def get(_id, obj):
        if not _id:
            return ResList.get_list(obj, request.args)
        vo = obj.query.filter(obj.id == _id).first()
        return res_util.success(vo)

    @staticmethod
    def delete(_id, obj):
        if not _id:
            return ResList.delete_list(obj)

        vo = obj.query.filter(obj.id == _id).first()
        db.session.delete(vo)
        db.session.commit()
        return res_util.success()


class ResList:

    @staticmethod
    def add_list(obj, data_list):
        vos = [obj(**data) for data in data_list]
        db.session.add_all(vos)
        db.session.commit()
        return res_util.success()

    @staticmethod
    def update_list(obj, data_list):
        for data in data_list:
            Res.update(data.get("id"), obj, data)
        return res_util.success()

    @staticmethod
    def get_list(obj, data):
        vos = obj.query.filter_by(**data).all()
        return res_util.success(vos)

    @staticmethod
    def delete_list(obj):
        vos = obj.query.filter_by(**obj).all()
        for vo in vos:
            db.session.delete(vo)
        db.session.commit()
        return res_util.success()
