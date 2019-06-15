import random
import time

from flask import Flask

from api import hello_api

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(hello_api, url_prefix='/admin')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
