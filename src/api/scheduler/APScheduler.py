from flask_apscheduler import APScheduler

from api.apply.robot.robot import robot1
from api.apply.robot.robot import robot1_wg
from api.scheduler.SchedulerFunc import init_dir
from api.scheduler.SchedulerFunc import init_db


scheduler = APScheduler()
# https://blog.csdn.net/qq_40125653/article/details/103662019
# https://www.cnblogs.com/zhaoyingjie/p/9664081.html
# 1. 立即执行
scheduler.add_job('init_dir', init_dir, trigger='date')
scheduler.add_job("init_db", init_db, trigger='date')
scheduler.add_job("robot1", robot1, trigger='interval', hours=24)
scheduler.add_job("robot1_wg", robot1_wg, trigger='cron', hour=8, minute=30)

# 1. date 定时
# scheduler.add_job("2",my_job, 'date', run_date='2009-11-06 16:30:05', args=['text'])
# 2. interval 以固定的时间间隔运行作业时使用
# scheduler.add_job("3",my_job, 'interval', hours=2, start_date='2018-10-10 09:30:00', end_date='2019-06-15 11:00:00')
# 3. cron：在一天中的特定时间定期运行作业时使用
# sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
