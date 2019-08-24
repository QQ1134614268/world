# encoding: utf-8
import re
import traceback
from os import path

from flasgger import Swagger
from flask import Flask, request
from flask_cors import CORS

from api.AliPayApi import ali_pay_api
from api.AreaApi import area_api
from api.AreaTableApi import area_table_api
from api.AuthApi import auth_api
from api.HelloApi import hello_api
from api.OrganizationApi import organization_api
from api.ProjectApi import world_project_api
from api.SpeechApi import speech_api
from api.SysApi import sys_api
from api.UserApi import user_api
from config import jwt_config
from config import mail
from db.db import db
from util.LogUtil import logger

APP_DIR = path.abspath(__file__)
PROJECT_DIR = path.dirname(path.dirname(path.dirname(path.dirname(APP_DIR))))
DATA_DIR = PROJECT_DIR + "/data"
RESOURCE_DIR = PROJECT_DIR + "/src/main/resource"
PARENT_DIR = path.dirname(PROJECT_DIR)

app = Flask(__name__)
# 跨域
CORS(app, supports_credentials=True)
# swagger
Swagger(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/world?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.config["SECRET_KEY"] = "session_key_world"


# app.config["PERMANENT_SESSION_LIFETIME"] = 60  # 设置session失效时间


@app.before_request
def before_request():  # 登录过滤,正则匹配,日志记录,IP分析
    allow = [".*"]
    url_path = request.path
    for i in allow:
        if url_path == "/favicon.ico":
            return "favicon.ico"
        if re.match(i, url_path):
            ip = request.remote_addr
            username = jwt_config.get_current_username()
            userid = jwt_config.get_current_username()
            logger.info(
                {"user": {"username": username, "userid": userid}, "url_path": url_path, "ip": ip,
                 "action": "before_request"})
            break
    else:
        return "请登录"


# @app.after_request  todo  所有数据都转成  格式
# def after_request():
#     from flask import Response
#     data = Response.get_data()
#     print(type(data), data)
#     pass


SERVER_MAIL = '1134614268@qq.com'


@app.errorhandler(Exception)
def flask_global_exception_handler(e):
    if app.config["DEBUG"]:
        # traceback.print_exc()  str(e)  repr(e)  e.message
        # 控制台打印异常栈信息,便于开发调试
        traceback.print_exc()
        # 日志记录异常信息
        message = traceback.format_exc()
        logger.error(message)
        # 邮件服务 发送异常通知邮件  邮件模板
        mail.send_email(message, SERVER_MAIL)
        return message
    else:
        traceback.print_exc()  # str(e)  repr(e)  e.message
        # 控制台打印异常栈信息,便于开发调试
        traceback.print_exc()
        # 日志记录异常信息
        message = traceback.format_exc()
        logger.error(message)
        # 邮件服务 发送异常通知邮件  邮件模板
        mail.send_email(message, SERVER_MAIL)
        return "server error"


app.register_blueprint(hello_api)
app.register_blueprint(user_api)
app.register_blueprint(sys_api)
app.register_blueprint(speech_api)
app.register_blueprint(organization_api)
app.register_blueprint(area_api)
app.register_blueprint(auth_api)
app.register_blueprint(world_project_api)
app.register_blueprint(area_table_api)
app.register_blueprint(ali_pay_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, threaded=True)
