from flask import Flask, request

from api import hello_api

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


app.register_blueprint(hello_api, url_prefix='/admin')  # 其他模块路由

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
