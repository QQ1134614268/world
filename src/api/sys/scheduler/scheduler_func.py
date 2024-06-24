import datetime
import os

from sqlalchemy.dialects.mysql import insert

from config.apscheduler_conf import scheduler
from config.enum_conf import Permission, Role, ReviewEnum, SexEnum
from config.env_default import world_env
from config.log_conf import logger
from config.mysql_db import db
from util import time_util
from vo.table_model import EnumConfig
from vo.video_model import InvitationCodeVO


def init_dir():
    logger.info("开始--创建文件目录")
    if not os.path.exists(world_env.log_dir):
        os.makedirs(world_env.log_dir)
    if not os.path.exists(world_env.upload_file_path):
        os.makedirs(world_env.upload_file_path)
    logger.info("结束--创建文件目录")


def task1(a, b):
    logger.info("开始--task1")
    logger.info(f"{a}+{b}= {a + b}")
    logger.info("结束--task1")


def clear_code():
    logger.info("开始--清除邀请码数据")
    from app import app
    with app.app_context():
        InvitationCodeVO.query.filter(
            InvitationCodeVO.create_time > time_util.get_now() - datetime.timedelta(days=7)
        ).delete()
        db.session.commit()
    logger.info("完成--清除邀请码数据")


def classname_to_const(name):
    res = []
    for index, char in enumerate(name):
        if char.isupper() and index != 0:
            res.append("_")
        res.append(char.upper())
    return ''.join(res)


def init_enum_table():
    logger.info("开始--插入枚举数据")
    # todo 验证枚举数据, 不一致告警,
    from app import app
    with app.app_context():
        group = [Role, Permission, ReviewEnum, SexEnum]
        for cla in group:
            group_code = classname_to_const(cla.__name__)
            ex = EnumConfig.query.filter(EnumConfig.group_code == group_code).first()
            if ex:
                continue
            data = [{'group_code': group_code, 'code': item.name, 'value': item.value, 'sort': index + 1} for
                    index, item in enumerate(cla)]

            insert_stmt = insert(EnumConfig).values(data)
            on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
                group_code=insert_stmt.inserted.group_code,
                code=insert_stmt.inserted.code,
                value=insert_stmt.inserted.value,
                sort=insert_stmt.inserted.sort,
            )
            db.session.execute(on_duplicate_key_stmt)
            db.session.commit()
    logger.info("完成--插入枚举数据")


# @scheduler.task('interval', id='blah', seconds=10, misfire_grace_time=900)
# def blah():
#     with scheduler.app.app_context():
#         vo = UserVO.query.filter(UserVO.id == 1).first()
#         print("============================================================")
#         return res_util.success(vo)


# https://blog.csdn.net/qq_40125653/article/details/103662019
# https://www.cnblogs.com/zhaoyingjie/p/9664081.html
# 1. 立即执行
scheduler.add_job('init_dir', init_dir, trigger='date')
scheduler.add_job('init_enum_table', init_enum_table, trigger='date')
scheduler.add_job("clear_code", clear_code, trigger='cron', hour=23, minute=0)

# scheduler.add_job("ana_worker_time", WorkerSchedule.ana_worker_time, trigger='cron', hour=22, minute=35)

# 1. date 定时
# scheduler.add_job("2",my_job, 'date', run_date='2009-11-06 16:30:05', args=['text'])
# 2. interval 以固定的时间间隔运行作业时使用
# scheduler.add_job("3",my_job, 'interval', hours=2, start_date='2018-10-10 09:30:00', end_date='2019-06-15 11:00:00')
# 3. cron: 在一天中的特定时间定期运行作业时使用
# sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
