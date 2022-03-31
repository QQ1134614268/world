from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler

_scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
scheduler = APScheduler(scheduler=_scheduler)
