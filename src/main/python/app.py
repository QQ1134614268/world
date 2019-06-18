from flask import Flask, request

app = Flask(__name__)


@app.before_request
def before_request():  # log   异常捕捉 TODO
    allow = []
    url = request.url
    if url in allow:
        pass

    ip = request.remote_addr
    token = request.headers.get("token")

    print(url, ip, token)


# @app.after_request
# def before_request():
#     ip = request.remote_addr
#     url = request.url

@app.route('/')
def hello_world():
    return 'Hello World!'

from api.user.user_api import user
from api.hello_api import hello

app.register_blueprint(hello)  # 其他模块路由
app.register_blueprint(user)  # 其他模块路由

# from flask_restplus import Api
# program = Flask(__name__, static_url_path='', static_folder='../uploads')
# api = Api(program, doc=False)
# CORS(program, supports_credentials=True)
#
# # api with doc string
# api.add_namespace(station)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, threaded=True)
