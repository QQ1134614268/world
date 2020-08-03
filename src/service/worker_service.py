from flask_restful import marshal, fields

from api.worker.vo import WorkerVO, WorkerTimeVO
from config.mysql_db import db
from config.orm_config import DateTime
from util import res_util


def add_worker(data):
    vo = WorkerVO(**data)
    db.session.commit()
    return res_util.success(vo.id)


def delete_worker(worker_id):
    db.session.delete(WorkerVO(id=worker_id))
    db.session.commit()
    return res_util.success(worker_id)


def update_worker(worker_id, data):
    WorkerVO.query.filter(id=worker_id).update(**data)
    db.session.commit()
    return res_util.success(worker_id)


def get_worker_all():
    worker_fields = {
        "id": fields.Integer,
        'name': fields.String,
        'birthday': DateTime,
        'id_card_number': fields.String,
        'sex': fields.String,
        'pay': fields.String,
        'start_time': DateTime,
    }
    vos = WorkerVO.query.all()
    return res_util.success([marshal(vo, worker_fields) for vo in vos])


def add_worker_time(data):
    vo = WorkerTimeVO(**data)
    db.session.commit()
    return res_util.success(vo.id)


def get_worker_time_all():
    worker_fields = {
        'hours': fields.Integer,
    }
    vos = WorkerTimeVO.query.all()
    return res_util.success([marshal(vo, worker_fields) for vo in vos])


def update_worker_time(worker_time_id, data):
    WorkerTimeVO.query.filter(id=worker_time_id).update(**data)
    db.session.commit()
    return res_util.success(worker_time_id)
