# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
import time

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
        return worker_service.delete_worker(data)


class WorkerTimeApi(Resource):
    """工时"""

    def post(self):
        data = request.get_json()

        # 1
        ids = data.get("worker_ids")
        worker_service.cover_worker_time(data)
        return worker_service.add_worker_time(data)

    def get(self):
        if request.args.get("month"):
            print(type(request.args.get("month")))
            return worker_service.get_worker_month(request.args.get("month"), request.args.get("workerId"))
        date = request.args.get("date", time.strftime('%Y-%m-%d 00:00:00'))
        return worker_service.get_worker_day(date)

    def put(self):
        data = request.get_json()
        return worker_service.update_worker_time(data)
