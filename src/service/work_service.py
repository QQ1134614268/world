# -*- coding:utf-8 -*-
"""
@Time: 2022/3/9
@Description:
"""
from sqlalchemy import and_

from config.conf import DATE_FORMAT
from util import time_util
from util.db_util import row_to_dic
from vo.worker_model import WorkerVO, WorkerTimeVO


def get_day_report(user_id):
    # 日报模式
    query_filter = [WorkerVO.belong == user_id, WorkerTimeVO.date == time_util.get_now_str(DATE_FORMAT)]
    join_filter = [WorkerTimeVO.worker_id == WorkerVO.id]
    res = WorkerVO.query.outerjoin(
        WorkerTimeVO,
        and_(*join_filter)
    ).with_entities(
        WorkerVO.id,
        WorkerVO.name,
        WorkerTimeVO.date,
        WorkerTimeVO.morning,
        WorkerTimeVO.morning_area,
        WorkerTimeVO.morning_content,
        WorkerTimeVO.noon,
        WorkerTimeVO.noon_area,
        WorkerTimeVO.noon_content,
        WorkerTimeVO.afternoon,
        WorkerTimeVO.afternoon_area,
        WorkerTimeVO.afternoon_content,
        WorkerTimeVO.night,
        WorkerTimeVO.night_area,
        WorkerTimeVO.night_content,
    ).filter(*query_filter).order_by(
        WorkerVO.name,
    ).all()
    ret = []
    for item in row_to_dic(res):
        ret.append({
            "area": item["morning_area"] or '',
            "time": "上午",
            "hours": item["morning"],
            "content": item["morning_content"],
            "name": item["name"],
        })
        ret.append({
            "area": item["noon_area"] or '',
            "time": "中午",
            "hours": item["noon"],
            "content": item["noon_content"],
            "name": item["name"],
        })
        ret.append({
            "area": item["afternoon_area"] or '',
            "time": "下午",
            "hours": item["afternoon"],
            "content": item["afternoon_area"],
            "name": item["name"],
        })
        ret.append({
            "area": item["night_area"] or '',
            "time": "晚上",
            "hours": item["night"],
            "content": item["night_content"],
            "name": item["name"],
        })

    ret = sorted(ret, key=lambda x: x["name"])
    return ret
