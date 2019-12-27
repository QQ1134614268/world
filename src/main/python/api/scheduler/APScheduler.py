from flask_apscheduler import APScheduler

from api.scheduler.SchedulerFunc import init, data
from api.scheduler.SchedulerFunc import init_db

scheduler = APScheduler()
scheduler.add_job('init', init)
scheduler.add_job("init_db", init_db)
scheduler.add_job("data2", data, trigger='cron', hour=8, minute=30)


# now = datetime.datetime.now()
# time_dely = now + datetime.timedelta(seconds=10)
# scheduler.add_job("init_dely", init_db, trigger='date', run_date=time_dely)


class Config(object):  # 创建配置，用类
    # 任务列表
    JOBS = [
        {
            'id': 'data',
            'func': data,  # 方法名
            'args': (),  # 入参
            'trigger': 'interval',  # interval表示循环任务
            'hours': 24,
        }
    ]
