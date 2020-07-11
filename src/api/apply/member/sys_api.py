# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask_restful import Resource
from flask_restful import fields

from .vo import ExistVO

model_fields = {
    'id': fields.Integer,
    'path': fields.String,
    'value': fields.String,
}


# 用户创建 store
# store下创建会员
# 会员添加人
# 系统--会员vo,用户vo,...
#  假设存在某些条件  todo  用户--商店--vip-vip会员-钱包   用户查看会员


class Model(Resource):

    def post(self):
        ExistVO
        pass

    def get(self):
        ExistVO
        pass
