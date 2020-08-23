from flask_apscheduler import APScheduler

scheduler = APScheduler()
# todo
# from api.apply.robot.robot import robot1
# from api.apply.robot.robot import robot1_wg
# from api.scheduler.SchedulerFunc import init, data
# from api.scheduler.SchedulerFunc import init_db
# scheduler.add_job('init', init)
# scheduler.add_job("init_db", init_db)
# scheduler.add_job("robot1", robot1, trigger='interval', hours=24)
# scheduler.add_job("robot1_wg", robot1_wg, trigger='cron', hour=8, minute=30)


# now = datetime.datetime.now()
# time_dely = now + datetime.timedelta(seconds=10)
# scheduler.add_job("init_dely", init_db, trigger='date', run_date=time_dely)
