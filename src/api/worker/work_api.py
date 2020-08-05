# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from flask import request
from flask_restful import Resource

from service import worker_service


class WorkerApi(Resource):
    """工人"""

    def post(self):
        data = request.get_json()
        return worker_service.add_worker(data)

    def get(self):
        return worker_service.get_worker_all()

    def put(self):
        data = request.get_json()
        if request.args.get("id"):
            worker_id = request.args.get("id")
            return worker_service.update_worker(worker_id, data)
        return worker_service.update_or_add_worker(data)

    def delete(self):
        data = request.get_json()
        worker_id = data.get("id")
        return worker_service.delete_worker(worker_id)


class WorkerTimeApi(Resource):
    """工时"""

    def post(self):
        data = request.get_json()
        return worker_service.add_worker_time(data)

    def get(self):
        return worker_service.get_worker_time_all()

    def put(self):
        data = request.get_json()
        return worker_service.update_worker_time(data)
