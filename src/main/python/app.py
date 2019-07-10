# encoding: utf-8
from flask import Flask, request
from api.user.user_api import user_api
from api.hello_api import hello_api
from api.sys.sys_api import sys_api
from api.hilltop.speech_api import speech_api
from db.db import db
from config import log
from config import jwt_config
import traceback
import re
from config import mail

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/world?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.before_request
def before_request():  # 登录过滤,正则匹配,日志记录,IP分析
    allow = [".*"]
    path = request.path
    for i in allow:
        if re.match(i, path):
            ip = request.remote_addr
            username = jwt_config.get_current_username()
            userid = jwt_config.get_current_username()
            log.info({"user": {"username": username, "userid": userid}, "path": path, "ip": ip, "action": "before_request"})
            break
    else:
        return "请登录"


# @app.after_request  todo  所有数据都转成  格式
# def after_request():
#     from flask import Response
#     data = Response.get_data()
#     print(type(data), data)
#     pass

SERVER_MAIL='1134614268@qq.com'


@app.errorhandler(Exception)
def flask_global_exception_handler(e):
    if app.config["DEBUG"]:
        # traceback.print_exc()  str(e)  repr(e)  e.message
        # 控制台打印异常栈信息,便于开发调试
        traceback.print_exc()
        # 日志记录异常信息
        message = traceback.format_exc()
        log.error(message)
        # 邮件服务 发送异常通知邮件  邮件模板
        mail.send_email(message,SERVER_MAIL)
        return message
    else:
        traceback.print_exc()  # str(e)  repr(e)  e.message
        # 控制台打印异常栈信息,便于开发调试
        traceback.print_exc()
        # 日志记录异常信息
        message = traceback.format_exc()
        log.error(message)
        # 邮件服务 发送异常通知邮件  邮件模板
        mail.send_email(message, SERVER_MAIL)
        return "server error"


app.register_blueprint(hello_api)
app.register_blueprint(user_api)
app.register_blueprint(sys_api)
app.register_blueprint(speech_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, threaded=True)
