import datetime
import os

from flask import Blueprint, send_file, jsonify, make_response
from flask import request

from global_variable import UPLOAD_FILE_PATH
from util import ResUtil
from util.LogUtil import logger
from util.time_util import getDatetimeByStr
from util.time_util import getTimeStr

fileApi = Blueprint("fileApi", __name__, url_prefix='/fileApi')


@fileApi.route('/fileUpload', methods=['POST'])
def fileUpload():
    file1 = request.files["file"]
    time_str = getTimeStr()
    file_path = UPLOAD_FILE_PATH + '/' + "upload-" + time_str + "-" + file1.filename
    file1.save(file_path)
    return jsonify(ResUtil.success(file_path))


@fileApi.route('/fileDownload', methods=['GET'])
def fileDownload():
    path = request.args.get("path")
    response = make_response(send_file(path))
    response.headers["Content-Disposition"] = "application/octet-stream"
    return response


def clear_file():
    root, dirs, files = os.walk(UPLOAD_FILE_PATH).__next__()
    for fileName in files:
        if not fileName.startswith("upload"):
            continue
        create_time = getDatetimeByStr(fileName.split("-")[1])
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=7)
        if now > create_time + delta:
            name = os.path.join(UPLOAD_FILE_PATH, fileName)
            os.remove(name)
            logger.info("delete: " + name)
