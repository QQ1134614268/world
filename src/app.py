# encoding: utf-8
import os
import re
import traceback

from flasgger import Swagger
from flask import Flask, request
from flask_cors import CORS
from geventwebsocket.handler import WebSocketHandler  # 提供WS（websocket）协议处理
from geventwebsocket.server import WSGIServer  # websocket服务承载

from api.AliPayApi import ali_pay_api
from api.AreaApi import area_api
from api.AreaTableApi import area_table_api
from api.AuthApi import auth_api
from api.HelloApi import hello_api
from api.OrganizationApi import organization_api
from api.SpeechApi import speech_api
from api.SysApi import sys_api
from api.customize.CustomizeApi import customize_api
from api.member.MemberApi import member_api
from api.member.StoreApi import store_api
from api.my_cloud_space.CloudSpaceApi import cloud_space_api
from api.scheduler.APScheduler import scheduler
from api.scheduler.SchedulerApi import scheduler_api
from api.stone_game.StoneGameApi import stone_game_api
from api.user.UserApi import user_api
from api.wb.WbApi import wb_api
from api.wx.SocketApi import socket_api
from db.db import db
from global_variable import DEBUG, MAIL_TO, DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DBNAME, version, \
    RESOURCE_DIR
from service import UserService
from util import MailUtil
from util import ResUtil
from util.LogUtil import logger

app = Flask(__name__, template_folder=os.path.join(RESOURCE_DIR, "template"))
# from config.config import Config
# app.config.from_object(Config)

# 跨域
CORS(app, supports_credentials=True)
# swagger
Swagger(app)

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DBNAME)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = "session_key_world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# {None: 0, False: 0, True: 20, 'debug': 10} True: 所有err, DEBUG=所有sql语句  todo
app.config["SQLALCHEMY_ECHO"] = DEBUG
app.config["DEBUG"] = DEBUG
db.init_app(app)


# 人-时间-效率=注册APScheduler


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
            username = UserService.get_name_by_token()
            userid = UserService.get_name_by_token()
            user_agent = request.headers.get('User-Agent')
            logger.info(
                {"user": {"username": username, "userid": userid}, "url_path": url_path, "ip": ip,
                 "User-Agent": user_agent,
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


@app.errorhandler(404)  # 当发生404错误时，会被该路由匹配
def handle_404_error(err_msg):
    """自定义的异常处理函数"""
    # 这个函数的返回值就是前端用户看到的最终结果 (404错误页面)
    url_path = request.path
    userid = UserService.get_name_by_token()
    logger.error({"404": {"userid": userid, "url_path": url_path, "err_msg": str(err_msg)}})
    return u"server error：%s" % err_msg


@app.errorhandler(Exception)
def flask_global_exception_handler(e):
    # traceback.print_exc()  # str(e)  repr(e)  e.message
    message = traceback.format_exc()
    logger.error(message)  # 日志输出到控制台和日志文件
    # 邮件服务 发送异常通知邮件  邮件模板
    MailUtil.send_email(message, MAIL_TO)
    if app.config["DEBUG"]:
        return ResUtil.fail(message)
    else:
        return ResUtil.fail("server error: " + str(e) + "; please contact your administrator ")


@app.route('/', methods=['GET'])
def welcome():
    txt = """
    welcome to world!
    you can see B-tree for the api : /apidocs
    version: %s 
    """ % version
    return txt


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
app.register_blueprint(store_api)
app.register_blueprint(socket_api)
app.register_blueprint(member_api)
app.register_blueprint(customize_api)
app.register_blueprint(wb_api)
app.register_blueprint(scheduler_api)

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    # app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

    http_server = WSGIServer(('0.0.0.0', 80), application=app, handler_class=WebSocketHandler)
    http_server.serve_forever()

    # socketio.run(app,debug=True,host='0.0.0.0',port=80)
