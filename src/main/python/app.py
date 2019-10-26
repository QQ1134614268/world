# encoding: utf-8
import re
import traceback

from flasgger import Swagger
from flask import Flask, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from api.AliPayApi import ali_pay_api
from api.AreaApi import area_api
from api.AreaTableApi import area_table_api
from api.AuthApi import auth_api
from api.HelloApi import hello_api
from api.OrganizationApi import organization_api
from api.SpeechApi import speech_api
from api.SysApi import sys_api
from api.UserApi import user_api
from api.my_cloud_space.CloudSpaceApi import cloud_space_api
from api.stone_game.StoneGameApi import stone_game_api
from config import mail
from db.db import db
from global_variable import MAIL_TO
from service import UserService
from util.LogUtil import logger
from world_init import init_all

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
            username = UserService.get_current_username()
            userid = UserService.get_current_username()
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
        mail.send_email(message, MAIL_TO)
        return message
    else:
        traceback.print_exc()  # str(e)  repr(e)  e.message
        # 控制台打印异常栈信息,便于开发调试
        traceback.print_exc()
        # 日志记录异常信息
        message = traceback.format_exc()
        logger.error(message)
        # 邮件服务 发送异常通知邮件  邮件模板
        mail.send_email(message, MAIL_TO)
        return "server error"


app.register_blueprint(hello_api)
app.register_blueprint(user_api)
app.register_blueprint(sys_api)
app.register_blueprint(speech_api)
app.register_blueprint(organization_api)
app.register_blueprint(area_api)
app.register_blueprint(auth_api)
app.register_blueprint(area_table_api)
app.register_blueprint(ali_pay_api)
app.register_blueprint(cloud_space_api)
app.register_blueprint(stone_game_api)

if __name__ == '__main__':
    print(888)
    init_all()
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
    print(888)

    # http_server = WSGIServer(('0.0.0.0', 80), app, handler_class=WebSocketHandler)  # 找对象
    # http_server.serve_forever()  # 对象的属性

