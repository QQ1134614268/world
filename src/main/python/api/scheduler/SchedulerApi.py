# -- coding:UTF-8 --
"""
@author:huangran
"""
from flask import Blueprint

from api.scheduler.APScheduler import scheduler
from api.scheduler.SchedulerFunc import task1

scheduler_api = Blueprint("scheduler_api", __name__, url_prefix='/scheduler_api')


@scheduler_api.route('/addjob', methods=['GET', 'POST'])
def addtask():
    scheduler.add_job(func=task1, id='1', args=(1, 2), trigger='interval', seconds=5, replace_existing=True)
    return 'sucess'


@scheduler_api.route('/remove_task')
def remove_task(job_id):  # 移除
    scheduler.delete_job(job_id)
    return 111


@scheduler_api.route('/gettask')
def get_task():  # 获取
    jobs = scheduler.get_jobs()
    print(jobs)
    return '111'


@scheduler_api.route('/pause')
def pausetask(job_id):  # 暂停
    scheduler.pause_job(job_id)
    return "Success!"


@scheduler_api.route('/resume')
def resumetask(job_id):  # 恢复
    scheduler.resume_job(job_id)
    return "Success!"
