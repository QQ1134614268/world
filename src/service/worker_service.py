import time

from flask_restful import marshal, fields
from sqlalchemy.sql import and_

from api.worker.vo import WorkerVO, WorkerTimeVO
from config.mysql_db import db
from config.orm_config import DateTime
from util import res_util


def add_worker(data):
    vo = WorkerVO(**data)
    db.session.commit()
    return res_util.success(vo.id)


def delete_worker(data):
    WorkerVO.query.filter(WorkerVO.id.in_(data)).delete(synchronize_session=False)
    db.session.commit()
    return res_util.success()


def update_worker(worker_id, data):
    WorkerVO.query.filter(id=worker_id).update(**data)
    db.session.commit()
    return res_util.success(worker_id)


def update_or_add_worker(data):
    vos = []
    for i in data:
        if i.get("id"):
            WorkerVO.query.filter(WorkerVO.id == i.pop("id")).update(i)
        else:
            vos.append(WorkerVO(**i))
    db.session.add_all(vos)
    db.session.commit()
    return res_util.success()


def get_worker_all():
    worker_fields = {
        "id": fields.Integer,
        'name': fields.String,
        'birthday': DateTime,
        'id_card_number': fields.String,
        'sex': fields.String,
        'pay': fields.String,
        'start_time': DateTime,
        'phone': fields.String,
    }
    vos = WorkerVO.query.all()
    return res_util.success([marshal(vo, worker_fields) for vo in vos])


def add_worker_time(data):
    vos = [WorkerTimeVO(**i) for i in data]
    db.session.commit_all(vos)
    return res_util.success()


def get_worker_time_all():
    res = WorkerVO.query.outerjoin(WorkerTimeVO, and_(WorkerTimeVO.date == time.strftime('%Y-%m-%d 00:00:00'),
                                                      WorkerVO.id == WorkerTimeVO.worker_id)).with_entities(
        WorkerVO.id.label("worker_id"),
        WorkerVO.name,
        WorkerTimeVO.id,
        WorkerTimeVO.morning,
        WorkerTimeVO.noon,
        WorkerTimeVO.afternoon,
        WorkerTimeVO.night,
    ).order_by(WorkerVO.name).all()
    ret = [dict(zip(item.keys(), item)) for item in res]
    return res_util.success(ret)


def update_worker_time(data):
    vos = []
    for i in data:
        if i.get("id"):
            WorkerTimeVO.query.filter(WorkerTimeVO.id == i.pop("id")).update(i)
        else:
            i["date"] = time.strftime('%Y-%m-%d 00:00:00')
            vos.append(WorkerTimeVO(**i))
    db.session.add_all(vos)
    db.session.commit()
    return res_util.success()
