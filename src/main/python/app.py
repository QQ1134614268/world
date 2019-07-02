# encoding: utf-8
from flask import Flask, request
from api.user.user_api import user_api
from api.hello_api import hello_api
from api.sys.sys_api import sys_api
from api.hilltop.speech_api import speech_api
from db.db import db
from config import log
from config import jwt_config
from config.exception import WorldException
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/world?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.before_request
def before_request():  # log   异常捕捉 TODO
    allow = []
    url = request.url
    if url in allow:
        pass
    else:
        # return  "请登录"
        pass
    ip = request.remote_addr
    # username = jwt_config.get_current_username()
    # log.info("username" + username + ";url: " + url + ";ip: " + ip)
    log.info("username:" + "w&g" + "; url: " + "/" + "; ip: " + "127.0.0.1")

# @app.after_request
# def after_request():
#     from flask import Response
#     data = Response.get_data()
#     print(type(data), data)
#     pass


# @app.errorhandler(Exception)
# def flask_global_exception_handler(e):
#     # 判断异常是不是APIException
#     if isinstance(e, WorldException):
#         return e
#     # 判断异常是不是HTTPException
#     elif isinstance(e, HTTPException):
#         error = WorldException()
#         error.code = e.code
#         error.message = e.description
#         return error
#     # 异常肯定是Exception
#     else:
#         from flask import current_app
#         # 如果是调试模式,则返回e的具体异常信息。否则返回json格式的ServerException对象！
#         if current_app.config["DEBUG"]:
#             return e
#         else:
#             return WorldException()


app.register_blueprint(hello_api)  # 其他模块路由
app.register_blueprint(user_api)  # 其他模块路由
app.register_blueprint(sys_api)  # 其他模块路由
app.register_blueprint(speech_api)  # 其他模块路由


@app.route("/")
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, threaded=True)
