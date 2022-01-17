import datetime
import os

from sqlalchemy.dialects.mysql import insert
from flask import current_app
from config.conf import LOG_DIR, UPLOAD_FILE_PATH
from config.enum_conf import Permission, Role
from config.mysql_db import db
from util import time_util
from util.log_util import logger
from vo.table_model import EnumConfig
from vo.video_model import InvitationCodeVO


def init_dir():
    logger.info("开始--创建文件目录")
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    if not os.path.exists(UPLOAD_FILE_PATH):
        os.makedirs(UPLOAD_FILE_PATH)
    logger.info("结束--创建文件目录")


def task1(a, b):
    logger.info("开始--task1")
    logger.info(f"{a}+{b}= {a + b}")
    logger.info("结束--task1")


def clear_code():
    from app import app
    with app.app_context():
        logger.info("开始--清除邀请码数据")
        InvitationCodeVO.query.filter(
            InvitationCodeVO.create_time > time_util.get_now() - datetime.timedelta(days=7)
        ).delete()
        db.session.commit()
        logger.info("完成--清除邀请码数据")


def clear_log_data():
    # 清除邀请码数据 清除log日志 todo
    pass


def classname_to_const(name):
    res = []
    for index, char in enumerate(name):
        if char.isupper() and index != 0:
            res.append("_")
        res.append(char.upper())
    return ''.join(res)


def init_enum_table():
    from app import app
    with app.app_context():
        logger.info("开始--同步枚举数据")
        data = [Role, Permission]
        for cla in data:
            for index, item in enumerate(cla):
                sql_data = {
                    'group_code': classname_to_const(cla.__name__),
                    'code': item.name,
                    'value': item.value,
                    'sort': index + 1
                }
                insert_stmt = insert(EnumConfig).values(sql_data)
                on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
                    group_code=insert_stmt.inserted.group_code,
                    code=insert_stmt.inserted.code,
                    value=insert_stmt.inserted.value,
                    sort=insert_stmt.inserted.sort,
                )
                db.session.execute(on_duplicate_key_stmt)
                db.session.commit()
        logger.info("完成--同步枚举数据")
