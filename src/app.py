# encoding: utf-8
"""
@Time: 2021/2/15
@Description:
"""
import json
import socket
import traceback

from flasgger import Swagger
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api

from api.HelloApi import hello_api
from api.member.member_api import StoreMemberListApi, StoreListApi, StoreMemberApi, StoreApi, OrderApi, OrderListApi, \
    GoodsApi, GoodsListApi
from api.message.Speech.SpeechApi import speech_api
from api.message.attention_api import attention_api
from api.message.message_api import message_api
from api.message.wb.WbApi import wb_api
from api.message.wx.SocketApi import socket_api
from api.my_cloud_space.CloudSpaceApi import cloud_space_api, FileApi
from api.project_api import ProjectInit
from api.stone_game.StoneGameApi import stone_game_api
from api.sys.SysApi import sys_api
from api.sys.config_api import ConfigApi
from api.sys.customize.CustomizeApi import customize_api
from api.sys.file.file_api import FileApi2
from api.sys.scheduler.APScheduler import scheduler
from api.sys.scheduler.SchedulerApi import scheduler_api
from api.tree.all import AllApi
from api.tree.tree_api import UploadDataApi, prove_api, ProveApi, StoryApi
from api.user.user_api import user_api
from api.user.wallet.wallet_api import WalletApi
from api.video.video_api import TargetApi, TargetListApi, MarketTargetListApi, WorksApi, WorksListApi, WorksRankListApi, \
    TargetRankListApi, VideoUserApi, VideoUserLoginApi, InvitationCodeApi, MarketWorksListApi
from api.worker.work_api import WorkerApi, WorkerTimeApi, WorkerExcelApi, WorkTimeAnalyseApi, \
    work_time_analyse_api
from api.worker.work_api2 import work_api2
from config.conf import DEBUG, MAIL_TO, DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DBNAME, VERSION
from config.conf import MAIL_HOST_BLOCK_LIST
from config.exception import WorldException
from config.json_config import JSONEncoder
from config.mysql_db import db
from util import mail_util
from util import res_util
from util import socket_util
from util.log_util import logger

app = Flask(__name__)
api2 = Api(app)
# 跨域
CORS(app, supports_credentials=True)
# swagger
Swagger(app)

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DBNAME)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = "session_key_world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_POOL_RECYCLE"] = 14400
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 10
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30

app.config["SQLALCHEMY_ECHO"] = DEBUG
app.config["DEBUG"] = DEBUG
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
db.init_app(app)
app.json_encoder = JSONEncoder


@app.before_request
def before_request():  # 登录过滤,正则匹配,日志记录,IP分析 todo
    """

    :return:
    """
    url_path = request.path
    ip_addr = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    logger.info({
        "url_path": url_path,
        "ip": ip_addr,
        "User-Agent": user_agent,
        "action": "before_request"
    })
    # for path in allow_path:
    #     if re.match(path, url_path):
    #         break
    # else:
    #     for path2 in intercept_path:
    #         username = user_service.get_name_by_token()
    #         userid = user_service.get_id_by_token()
    #         logger.info({"user": {"username": username, "userid": userid}, "url_path": url_path, "ip": ip,
    #                      "User-Agent": user_agent, "action": "before_request"})
    #         if re.match(path2, url_path):
    #             if not token_util.check_token():
    #                 return res_util.fail("请登录")


# @app.after_request  todo  所有数据都转成  格式
# def after_request():
#     from flask import Response
#     data = Response.get_data()
#     print(type(data), data)
#     pass


@app.errorhandler(404)  # 当发生404错误时，会被该路由匹配
def handle_404_error(err_msg):
    """
    自定义的异常处理函数
    :param err_msg:
    :return:
    """
    # 这个函数的返回值就是前端用户看到的最终结果 (404错误页面)
    url_path = request.path
    logger.error({
        "404": {
            "url_path": url_path,
            "err_msg": str(err_msg)
        }
    })
    return res_util.exception(u"server error：%s" % err_msg)


@app.errorhandler(Exception)
def flask_global_exception_handler(err):
    """

    :param err:
    :return:
    """
    # traceback.print_exc()  # str(e)  repr(e)  e.message
    try:
        message = traceback.format_exc()
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
        except:
            host_name = "unknown hostname"
            host_ip = "unknown ip"
        data = {
            "remote_ip": request.remote_addr,
            "url": request.path,
            "method": request.method,
            "host_ip": host_ip,
            "host_name": host_name
        }
        logger.error(message, data)  # 日志输出到控制台和日志文件
        try:
            traceback.print_exc()
        except Exception as e:
            # logger.exception(e)
            logger.error(str(e))
        # 邮件服务 发送异常通知邮件  邮件模板
        try:
            if not socket_util.get_host_name() in MAIL_HOST_BLOCK_LIST:
                mail_util.send_email(json.dumps(data) + message, MAIL_TO)
        except Exception as e:
            # logger.exception(e)
            logger.error(str(e))
    except:
        logger.error("global_exception_handler 发生异常")
    if app.config["DEBUG"]:
        return res_util.exception(message)
    return res_util.exception("服务器发生了一个错误")


@app.errorhandler(AssertionError)
def flask_global_assertion_handler(exception):
    """

    :param exception:
    :return:
    """
    print(exception)
    print(str(exception))
    return res_util.fail(str(exception))


@app.errorhandler(WorldException)
def flask_global_world_exception_handler(exception):
    """

    :param exception:
    :return:
    """
    return res_util.fail(exception.message)


@app.route('/', methods=['GET'])
def welcome():
    """

    :return:
    """
    txt = """
    welcome to world!
    you can see B-tree for the api : /apidocs
    version: {} 
    """.format(VERSION)
    return res_util.success(txt)


app.register_blueprint(hello_api)
app.register_blueprint(sys_api)
app.register_blueprint(speech_api)
app.register_blueprint(cloud_space_api)
app.register_blueprint(stone_game_api)
app.register_blueprint(socket_api)
app.register_blueprint(customize_api)
app.register_blueprint(wb_api)
app.register_blueprint(scheduler_api)
app.register_blueprint(message_api)
# 用户
app.register_blueprint(user_api)
app.register_blueprint(attention_api)

api2.add_resource(ProjectInit, "/help")
api2.add_resource(ConfigApi, "/api/config_api/ConfigApi/<int:_id>")

api2.add_resource(FileApi, "/api/file/FileApi")
api2.add_resource(FileApi2, "/api/file/FileApi2")
# model
api2.add_resource(UploadDataApi, "/api/model_api/UploadDataApi/<int:_id>")
app.register_blueprint(prove_api)
api2.add_resource(ProveApi, "/api/model_api/ProveApi/<int:_id>")
api2.add_resource(StoryApi, "/api/model_api/StoryApi/<int:_id>")
# 会员
api2.add_resource(StoreApi, "/api/member/StoreApi", "/api/member/StoreApi/<int:_id>")
api2.add_resource(StoreListApi, "/api/member/StoreListApi")
api2.add_resource(StoreMemberApi, "/api/member/StoreMemberApi")
api2.add_resource(StoreMemberListApi, "/api/member/StoreMemberListApi")
api2.add_resource(OrderApi, "/api/member/OrderApi")
api2.add_resource(OrderListApi, "/api/member/OrderListApi")

# 钱包
api2.add_resource(WalletApi, "/api/member/WalletApi")

# 会员
api2.add_resource(GoodsApi, "/api/goods", "/api/goods/<int:_id>")
api2.add_resource(GoodsListApi, "/api/goods_list")

# 工时
api2.add_resource(WorkerExcelApi, "/api/work_api/WorkerExcelApi")
api2.add_resource(WorkerApi, "/api/work_api/WorkerApi/<int:_id>")
api2.add_resource(WorkerTimeApi, "/api/work_api/WorkerTimeApi/<int:_id>")
api2.add_resource(WorkTimeAnalyseApi, "/api/work_api/WorkTimeAnalyseApi/<int:_id>")
app.register_blueprint(work_api2)
app.register_blueprint(work_time_analyse_api)
# video
api2.add_resource(TargetApi, "/api/video_api/TargetApi/<int:_id>")
api2.add_resource(TargetListApi, "/api/video_api/TargetListApi/<int:_id>")
api2.add_resource(MarketTargetListApi, "/api/video_api/MarketTargetListApi/<int:_id>")

api2.add_resource(WorksApi, "/api/video_api/WorksApi/<int:_id>")
api2.add_resource(WorksListApi, "/api/video_api/WorksListApi/<int:_id>")
api2.add_resource(WorksRankListApi, "/api/video_api/WorksRankListApi/<int:_id>")
api2.add_resource(TargetRankListApi, "/api/video_api/TargetRankListApi/<int:_id>")
api2.add_resource(MarketWorksListApi, "/api/video_api/MarketWorksListApi/<int:_id>")
api2.add_resource(VideoUserApi, "/api/video_api/VideoUserApi/<int:_id>")
api2.add_resource(VideoUserLoginApi, "/api/video_api/VideoUserLoginApi")
api2.add_resource(AllApi, "/api/video_api/AllApi/<int:_id>")
api2.add_resource(InvitationCodeApi, "/api/video_api/InvitationCodeApi/<int:_id>")

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0', port=9090, debug=True, threaded=True)
    # http_server = WSGIServer(('0.0.0.0', 80), application=app, handler_class=WebSocketHandler )
    # http_server.serve_forever()

    # socketio.run(app,debug=True,host='0.0.0.0',port=80)
