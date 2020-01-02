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


