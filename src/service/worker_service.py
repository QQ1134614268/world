import time

from flask_restful import marshal, fields
from sqlalchemy.sql import and_

from api.worker.vo import WorkerVO, WorkerTimeVO
from config.mysql_db import db
from config.orm_config import DateTime
from service import user_service
from util import res_util


def add_worker(data):
    data["belong"] = user_service.get_id_by_token()
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
    user_id = user_service.get_id_by_token()
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
    vos = WorkerVO.query.filter(WorkerVO.belong == user_id).all()
    return res_util.success([marshal(vo, worker_fields) for vo in vos])


def add_worker_time(data):
    # data["date"] = time.strftime('%Y-%m-%d 00:00:00')
    vos = [WorkerTimeVO(**i) for i in data]
    db.session.commit_all(vos)
    return res_util.success()


# def get_worker_time_all():
#     res = WorkerVO.query.outerjoin(WorkerTimeVO, and_(WorkerTimeVO.date == time.strftime('%Y-%m-%d 00:00:00'),
#                                                       WorkerVO.id == WorkerTimeVO.worker_id)).with_entities(
#         WorkerVO.id.label("worker_id"),
#         WorkerVO.name,
#         WorkerTimeVO.id,
#         WorkerTimeVO.morning,
#         WorkerTimeVO.noon,
#         WorkerTimeVO.afternoon,
#         WorkerTimeVO.night,
#     ).order_by(WorkerVO.name).all()
#     ret = [dict(zip(item.keys(), item)) for item in res]
#     return res_util.success(ret)


def update_worker_time(data):
    vos = []
    for i in data:
        if i.get("id"):
            WorkerTimeVO.query.filter(WorkerTimeVO.id == i.pop("id")).update(i)
        else:
            vos.append(WorkerTimeVO(**i))
    db.session.add_all(vos)
    db.session.commit()
    return res_util.success()


def get_worker_day(date):
    res = WorkerVO.query.outerjoin(
        WorkerTimeVO, and_(WorkerTimeVO.date == date, WorkerVO.id == WorkerTimeVO.worker_id)
    ).filter(WorkerVO.belong == user_service.get_id_by_token()).with_entities(
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


def get_worker_month(month):
    res = WorkerVO.query.outerjoin(
        WorkerTimeVO, and_(WorkerTimeVO.date.between(month, month + 1), WorkerVO.id == WorkerTimeVO.worker_id)
    ).filter(WorkerVO.belong == user_service.get_id_by_token()).with_entities(
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
