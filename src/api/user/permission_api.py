# -- coding:UTF-8 --
from flask import request
from flask_restful import Resource

from service.auth_service import _has_permission
from util import res_util


class PermissionApi(Resource):

    def get(self, _id):
        permission = request.args.get('permission')
        if permission:
            return res_util.success(_has_permission(permission))
        return res_util.success(False)
