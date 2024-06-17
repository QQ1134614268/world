# encoding: utf-8
"""
@Time: 2021/2/15
@Description:
"""
import json
import socket
import traceback

from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from api.HelloApi import hello_api
from api.code.code_api import code_blueprint_api
from api.member.member_api import StoreApi, OrderApi, GoodsApi, order_api, QrCodeApi, goods_api
from api.message.socket.SocketApi import socket_api
from api.my_cloud_space.CloudSpaceApi import cloud_space_api, CloudSpaceApi
from api.project_api import ProjectInit
from api.stone_game.StoneGameApi import stone_game_api
from api.sys.SysApi import sys_api, AllApi, SuggestApi, AnnouncementApi
from api.sys.config_api import ConfigApi, enum_api
from api.sys.customize.customize_api import customize_api
from api.sys.file.file_api import FileApi2
from api.sys.log_api import LogApi
from api.sys.scheduler.scheduler_api import scheduler_api
from api.sys.system_level_api import SystemLevelApi
from api.tree.tree_api import UploadDataApi, prove_api, ProveApi, StoryApi
from api.user.permission_api import PermissionApi
from api.user.user_api import user_api, UserApi
from api.user.wallet.wallet_api import WalletApi
from api.video.video_api import TargetApi, TargetListApi, MarketTargetListApi, WorksApi, WorksListApi, WorksRankListApi, \
    TargetRankListApi, MarketWorksListApi, VideoUserApi, InvitationCodeApi, ReviewTargetApi, ReviewWorksApi, \
    video_blueprint_api
from api.worker.work_api import WorkerApi, WorkerTimeApi, WorkerExcelApi, WorkTimeAnalyseApi, \
    work_time_analyse_api
from config.apscheduler_conf import scheduler
from config.conf import VERSION
from config.env_default import world_env
from config.exception import WorldNoLoginException, WorldException
from config.json_config import MyJsonEncoder
from config.log_conf import logger
from config.mysql_db import db
from util import mail_util
from util import res_util
from util import socket_util

app = Flask(__name__)

api2 = Api(app)
# 跨域
CORS(app, supports_credentials=True)

app.config["SQLALCHEMY_DATABASE_URI"] = world_env.sqlalchemy_database_uri
# app.config["SQLALCHEMY_BINDS"] = SQLALCHEMY_BINDS
app.config["SECRET_KEY"] = "session_key_world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_POOL_RECYCLE"] = 14400
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 10
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30

app.config["SQLALCHEMY_ECHO"] = world_env.debug
app.config["DEBUG"] = world_env.debug
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
db.init_app(app)
app.json_encoder = MyJsonEncoder

# cd src
# D:/workspace/world/venv/Scripts/flask db init
# D:/workspace/world/venv/Scripts/flask db migrate
# D:/workspace/world/venv/Scripts/flask db upgrade
migrate = Migrate()
migrate.init_app(app, db)


@app.before_request
def before_request():
    """

    :return:
    """
    url_path = request.path
    ip_adder = request.remote_addr
    logger.info({
        "url_path": url_path,
        "ip": ip_adder,
        "action": "before_request"
    })
    # 校验系统权限 -> 子网关

    # 校验登录

    # # 需登录api, 没有登录 登录校验
    # allow_path=[]
    # if url_path not in [] and not check_token():
    #     raise WorldNoLoginException("请重新登录")


@app.errorhandler(404)  # 当发生404错误时，会被该路由匹配
def handle_404_error(err_msg):
    """
    自定义的异常处理函数
    :param err_msg:
    :return:
    """
    # 这个函数的返回值就是前端用户看到的最终结果 (404错误页面)
    url_path = request.path
    logger.warning({
        "404": {
            "url_path": url_path,
            "err_msg": str(err_msg)
        }
    })
    return res_util.fail(str(err_msg))


@app.errorhandler(405)
def handle_405_error(err_msg):
    url_path = request.path
    logger.warning({
        "405": {
            "url_path": url_path,
            "err_msg": str(err_msg)
        }
    })
    return res_util.fail(str(err_msg))


@app.errorhandler(Exception)
def flask_global_exception_handler(err):
    """
    :param err:
    :return:
    """
    # traceback.print_exc()  # str(e)  repr(e)  e.message
    message = traceback.format_exc()
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except:
        host_name = "unknown hostname"
        host_ip = "unknown ip"
    try:
        data = {
            "remote_ip": request.remote_addr,
            "url": request.path,
            "method": request.method,
            "host_ip": host_ip,
            "host_name": host_name
        }
        logger.error(message, data)  # 日志输出到控制台和日志文件
        traceback.print_exc()
    except:
        logger.error("global_exception_handler 发生异常")
    # 邮件服务 发送异常通知邮件  邮件模板
    try:
        if not socket_util.get_host_name() in world_env.mail_host_block_list:
            mail_util.send_email(json.dumps(data) + message, world_env.developer_mail)
    except Exception as e:
        # logger.exception(e)
        logger.error(str(e))
    if app.config["DEBUG"]:
        return res_util.exception(message)
    return res_util.exception("服务器发生了一个错误")


@app.errorhandler(AssertionError)
def flask_global_assertion_handler(exception):
    """

    :param exception:
    :return:
    """
    traceback.print_exc()
    message = traceback.format_exc()
    logger.error(message)
    return res_util.fail(str(exception))


@app.errorhandler(WorldException)
def flask_global_world_exception_handler(exception):
    """

    :param exception:
    :return:
    """
    traceback.print_exc()
    logger.error("WorldException", traceback.format_exc())
    return res_util.fail(exception.message, exception.code)


@app.errorhandler(WorldNoLoginException)
def flask_world_no_login_exception_handler(err):
    traceback.print_exc()
    logger.error("未登录异常", traceback.format_exc())
    return res_util.fail(err.message, err.code)


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
app.register_blueprint(cloud_space_api)
app.register_blueprint(stone_game_api)
app.register_blueprint(socket_api)
app.register_blueprint(customize_api)
app.register_blueprint(scheduler_api)
# sys
api2.add_resource(SystemLevelApi, "/api/sys/SystemLevelApi/<int:_id>")

api2.add_resource(ProjectInit, "/help")
api2.add_resource(ConfigApi, "/api/config_api/ConfigApi/<int:_id>")
api2.add_resource(SuggestApi, "/api/sys_api/SuggestApi/<int:_id>")
api2.add_resource(AnnouncementApi, "/api/sys_api/AnnouncementApi/<int:_id>")
app.register_blueprint(enum_api)

api2.add_resource(CloudSpaceApi, "/api/file/CloudSpaceApi")

api2.add_resource(FileApi2, "/api/file/FileApi2", "/api/file/FileApi2/<string:path>")

api2.add_resource(LogApi, "/api/log_api/LogApi/<int:_id>")

api2.add_resource(AllApi, "/api/video_api/AllApi/<int:_id>")

# 用户
app.register_blueprint(user_api)
api2.add_resource(UserApi, "/api/user_api/UserApi/<int:_id>")
api2.add_resource(PermissionApi, "/api/user_api/PermissionApi/<int:_id>")

# model
api2.add_resource(UploadDataApi, "/api/model_api/UploadDataApi/<int:_id>")
app.register_blueprint(prove_api)
api2.add_resource(ProveApi, "/api/model_api/ProveApi/<int:_id>")
api2.add_resource(StoryApi, "/api/model_api/StoryApi/<int:_id>")
# 会员
api2.add_resource(StoreApi, "/api/member/StoreApi/<int:_id>")
api2.add_resource(OrderApi, "/api/member/OrderApi/<int:_id>")
app.register_blueprint(order_api)
app.register_blueprint(goods_api)
api2.add_resource(QrCodeApi, "/api/member/QrCodeApi/<int:_id>")
api2.add_resource(GoodsApi, "/api/goods_api/GoodsApi/<int:_id>")

# 钱包
api2.add_resource(WalletApi, "/api/member/WalletApi")

# 工时
api2.add_resource(WorkerExcelApi, "/api/work_api/WorkerExcelApi")
api2.add_resource(WorkerApi, "/api/work_api/WorkerApi/<int:_id>")
api2.add_resource(WorkerTimeApi, "/api/work_api/WorkerTimeApi/<int:_id>")
api2.add_resource(WorkTimeAnalyseApi, "/api/work_api/WorkTimeAnalyseApi/<int:_id>")
app.register_blueprint(work_time_analyse_api)
# video
api2.add_resource(TargetApi, "/api/video_api/TargetApi/<int:_id>")
api2.add_resource(TargetListApi, "/api/video_api/TargetListApi/<int:_id>")
api2.add_resource(MarketTargetListApi, "/api/video_api/MarketTargetListApi/<int:_id>")

api2.add_resource(InvitationCodeApi, "/api/video_api/InvitationCodeApi/<int:_id>")
api2.add_resource(VideoUserApi, "/api/video_api/VideoUserApi/<int:_id>")
api2.add_resource(WorksApi, "/api/video_api/WorksApi/<int:_id>")
api2.add_resource(WorksListApi, "/api/video_api/WorksListApi/<int:_id>")
api2.add_resource(WorksRankListApi, "/api/video_api/WorksRankListApi/<int:_id>")
api2.add_resource(TargetRankListApi, "/api/video_api/TargetRankListApi/<int:_id>")
api2.add_resource(MarketWorksListApi, "/api/video_api/MarketWorksListApi/<int:_id>")

app.register_blueprint(video_blueprint_api)

api2.add_resource(ReviewTargetApi, "/api/video_api/ReviewTargetApi/<int:_id>")
api2.add_resource(ReviewWorksApi, "/api/video_api/ReviewWorksApi/<int:_id>")

# code 低代码 自动化 效率
app.register_blueprint(code_blueprint_api)

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0', port=19100, debug=True, threaded=True)
    # http_server = WSGIServer(('0.0.0.0', 80), application=app, handler_class=WebSocketHandler )
    # http_server.serve_forever()

    # socketio.run(app,debug=True,host='0.0.0.0',port=80)
