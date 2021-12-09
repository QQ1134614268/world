import datetime
from datetime import date

from sqlalchemy.dialects.mysql import insert
from sqlalchemy.sql import and_

import service.token_service
from config.conf import DATE_FORMAT, TIME_ENUM
from config.mysql_db import db
from util import res_util
from vo.table_model import WorkerVO, WorkerTimeVO


def get_worker_day(date):
    res = WorkerVO.query.outerjoin(
        WorkerTimeVO, and_(WorkerTimeVO.date == date, WorkerVO.id == WorkerTimeVO.worker_id)
    ).filter(WorkerVO.belong == service.token_service.get_id_by_token()).with_entities(
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


def get_worker_month(month, work_id):
    month = datetime.datetime.strptime(month, DATE_FORMAT)
    month = date(month.year, month.month, 1)
    last_month = date(month.year, month.month + 1, 1) - datetime.timedelta(days=1)
    res = WorkerVO.query.outerjoin(
        WorkerTimeVO,
        and_(WorkerTimeVO.date.between(month, last_month),
             WorkerVO.id == WorkerTimeVO.worker_id)
    ).filter(WorkerVO.id == work_id).with_entities(
        WorkerVO.id.label("worker_id"),
        WorkerVO.name.label("name"),
        WorkerTimeVO.id.label("id"),
        WorkerTimeVO.date.label("date"),
        WorkerTimeVO.morning.label("morning"),
        WorkerTimeVO.noon.label("noon"),
        WorkerTimeVO.afternoon.label("afternoon"),
        WorkerTimeVO.night.label("night"),
    ).order_by(WorkerVO.name).order_by(WorkerTimeVO.date).all()
    ret = [dict(zip(item.keys(), item)) for item in res]
    for i in ret:
        i["date"] = i["date"].strftime(DATE_FORMAT)
    return res_util.success(ret)


def cover_worker_time(data):
    vo = WorkerVO(**data)
    db.session.add()
    db.session.commit()
    return res_util.success(vo.id)


def cover_worker_time3(data):
    # 3个策略  --  批量
    # 输入时间  时间-上下午标签- 多选人--场景  早上签到
    # 人,勾选 上下午,,避免手动输入时间
    for i in data["worker_id"]:
        sql = insert(WorkerTimeVO).values(worker_id=i, **TIME_ENUM[data.get("type")],
                                          date=data["date"]).on_duplicate_key_update(
            **TIME_ENUM[data.get("type")])
        db.session.execute(sql)
    db.session.commit()
    return res_util.success()


def cover_worker_time2(data):
    data2 = {}
    for i in data["type"]:
        data2.update(TIME_ENUM.get(i))
    sql = insert(WorkerTimeVO).values(worker_id=data["worker_id"], **data2,
                                      date=data["date"]).on_duplicate_key_update(**data2)
    db.session.execute(sql)
    db.session.commit()
    return res_util.success()
