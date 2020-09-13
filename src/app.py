# encoding: utf-8
import json
import re
import socket
import traceback

from flasgger import Swagger
from flask import Flask, request, make_response
from flask_cors import CORS
from flask_restful import Api

from api.HelloApi import hello_api
from api.apply.member.member_api import StoreApi, StoreMemberApi, WalletApi
from api.apply.stone_game.StoneGameApi import stone_game_api
from api.customize.CustomizeApi import customize_api
from api.exist.class_api import ClassApi
from api.message.Speech.SpeechApi import speech_api
from api.message.message_api import message_api
from api.message.wb.WbApi import wb_api
from api.message.wx.SocketApi import socket_api
from api.model.model_api import ModelApi
from api.my_cloud_space.CloudSpaceApi import cloud_space_api
from api.my_cloud_space.file.file_api import FileApi
from api.root.OrganizationApi import organization_api
from api.root.btree_api import btree_api
from api.scheduler.APScheduler import scheduler
from api.scheduler.SchedulerApi import scheduler_api
from api.script_api import ScriptApi
from api.sys.SysApi import sys_api
from api.user.AuthApi import auth_api
from api.user.user_api import user_api
from api.wallet.AliPayApi import ali_pay_api
from api.worker.work_api import WorkerApi, WorkerTimeApi
from config.conf import DEBUG, MAIL_TO, DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DBNAME, VERSION
from config.conf import MAIL_HOST_BLOCK_LIST
from config.mysql_db import db
from service import user_service
from util import mail_util
from util import res_util
from util import socket_util
from util import token_util
from util.log_util import logger

app = Flask(__name__)
api = Api(app)
# 跨域
CORS(app, supports_credentials=True)
# swagger
Swagger(app)

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DBNAME)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = "session_key_world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = DEBUG
app.config["DEBUG"] = DEBUG
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
db.init_app(app)


@app.before_request
def before_request():  # 登录过滤,正则匹配,日志记录,IP分析 todo
    if request.method == "OPTIONS":
        return make_response(), 200
    intercept_path = ["/api"]
    allow_path = ["/api/sys_api/register", "/api/sys_api/get_verify_code", "/api/sys_api/login",
                  "/api/sys_api/logout", "/api/hello_api"]
    url_path = request.path
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    for path in allow_path:
        logger.info({"url_path": url_path, "ip": ip, "User-Agent": user_agent, "action": "before_request"})
        if re.match(path, url_path):
            break
    else:
        for path2 in intercept_path:
            username = user_service.get_name_by_token()
            userid = user_service.get_id_by_token()
            logger.info({"user": {"username": username, "userid": userid}, "url_path": url_path, "ip": ip,
                         "User-Agent": user_agent, "action": "before_request"})
            if re.match(path2, url_path):
                if not token_util.check_token():
                    return res_util.fail("请登陆")


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
    userId = user_service.get_name_by_token()
    logger.error({"404": {"userId": userId, "url_path": url_path, "err_msg": str(err_msg)}})
    return res_util.err(u"server error：%s" % err_msg)


@app.errorhandler(Exception)
def flask_global_exception_handler(e):
    # traceback.print_exc()  # str(e)  repr(e)  e.message
    message = traceback.format_exc()
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except ConnectionError:
        host_name = "unknown hostname"
        host_ip = "unknown ip"
    data = {"remote_ip": request.remote_addr, "url": request.path, "method": request.method,
            "host_ip": host_ip, "host_name": host_name}
    logger.error(message, data)  # 日志输出到控制台和日志文件
    traceback.print_exc()
    # 邮件服务 发送异常通知邮件  邮件模板
    if not socket_util.get_host_name() in MAIL_HOST_BLOCK_LIST:
        mail_util.send_email(json.dump(data) + message, MAIL_TO)
    if app.config["DEBUG"]:
        return res_util.err(message)
    else:
        return res_util.err("服务器发生了一个错误")


@app.route('/', methods=['GET'])
def welcome():
    txt = """
    welcome to world!
    you can see B-tree for the api : /apidocs
    version: %s 
    """ % VERSION
    return res_util.success(txt)


app.register_blueprint(hello_api)
app.register_blueprint(user_api)
app.register_blueprint(sys_api)
app.register_blueprint(speech_api)
app.register_blueprint(organization_api)
app.register_blueprint(auth_api)
app.register_blueprint(ali_pay_api)
app.register_blueprint(cloud_space_api)
app.register_blueprint(stone_game_api)
app.register_blueprint(socket_api)
app.register_blueprint(customize_api)
app.register_blueprint(wb_api)
app.register_blueprint(scheduler_api)
app.register_blueprint(message_api)
app.register_blueprint(btree_api)
api.add_resource(FileApi, "/api/file/FileApi")
api.add_resource(ModelApi, "/api/model_api/ModelApi")
api.add_resource(StoreApi, "/api/member/StoreApi")
api.add_resource(StoreMemberApi, "/api/member/StoreMemberApi")
api.add_resource(WalletApi, "/api/member/WalletApi")
api.add_resource(WorkerApi, "/api/work_api/WorkerApi")
api.add_resource(WorkerTimeApi, "/api/work_api/WorkerTimeApi")
api.add_resource(ClassApi, "/api/class_api/ClassApi")
api.add_resource(ScriptApi, "/api/class_api/ScriptApi")

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0', port=9090, debug=True, threaded=True)
    # http_server = WSGIServer(('0.0.0.0', 80), application=app, handler_class=WebSocketHandler )
    # http_server.serve_forever()

    # socketio.run(app,debug=True,host='0.0.0.0',port=80)
