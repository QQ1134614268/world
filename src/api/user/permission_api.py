# -- coding:UTF-8 --
from flask import request
from flask_restful import Resource

from service.auth_service import has_permission
from util import res_util


class PermissionApi(Resource):

    def post(self, _id):
        permission = request.args.get('permission')
        if permission:
            return res_util.success(has_permission(permission))
        # todo permission
        return res_util.success(True)
