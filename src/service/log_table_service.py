# -*- coding:utf-8 -*-
"""
@Time: 2021/12/22
@Description:
"""
from config.mysql_db import db
from vo.table_model import LogVO


def log_table(user_id, msg, tag):
    vo = LogVO(user_id=user_id, message=msg, tag=tag)
    db.session.add(vo)
    db.session.commit()
