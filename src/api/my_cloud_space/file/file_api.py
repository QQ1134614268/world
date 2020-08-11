import datetime
import os

from flask import Blueprint, send_file, jsonify
from flask import request

from config.conf import UPLOAD_FILE_PATH
from util import res_util
from util.log_util import logger
from util.time_util import getDatetimeByStr
from util.time_util import getUtcTimeStr

fileApi = Blueprint("fileApi", __name__, url_prefix='/api/fileApi')


@fileApi.route('/fileUpload', methods=['POST'])
def fileUpload():
    file1 = request.files["file"]
    time_str = getUtcTimeStr()
    if file1.filename.endswith("\""):
        # todo postman上传文件,文件名会多一个 引号,swagger不会产生这种问题
        filename = file1.filename[:-1]
    else:
        filename = file1.filename
    file_path = UPLOAD_FILE_PATH + '/' + "upload-" + time_str + "-" + filename
    file1.save(file_path)
    return jsonify(res_util.success(file_path))


@fileApi.route('/fileDownload', methods=['GET'])
def fileDownload():
    path = request.args.get("path")
    return send_file(path, as_attachment=False,
                     attachment_filename=path.split('/')[-1].encode(encoding='utf_8', errors="ignore").decode('utf_8'),
                     mimetype='image/jpeg')


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
