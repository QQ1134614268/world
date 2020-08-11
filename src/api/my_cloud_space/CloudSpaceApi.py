# -- coding:UTF-8 --
import os
import random

import time
from flask import Blueprint, send_file, jsonify, make_response, request

from config.mysql_db import db
from config.conf import UPLOAD_FILE_PATH
from service import user_service
from util import res_util
from vo.CloudSpaceVO import UserCloudSpaceVO

cloud_space_api = Blueprint("cloud_space_api", __name__, url_prefix='/api/cloud_space_api')


@cloud_space_api.route('/init', methods=['GET'])
def init():
    user_id = user_service.get_id_by_token()
    os.makedirs(os.path.join(UPLOAD_FILE_PATH, str(user_id)))
    return jsonify(res_util.success("cloud_space init success"))


@cloud_space_api.route('/create_dir', methods=['POST'])
def create_dir():
    data = request.get_json()
    name = data.get('name')
    user_id = user_service.get_id_by_token()
    os.makedirs(os.path.join(UPLOAD_FILE_PATH, str(user_id)), name)
    return jsonify(res_util.success("操作成功"))


@cloud_space_api.route('/get_filename_list_v2', methods=['POST'])
def get_filename_list_v2():
    data = request.get_json()
    name = data.get('name')
    file_dir = getDirName(name)
    ret = getFiles(file_dir)
    return jsonify(res_util.success(ret))


def getDirName(file_dir):
    user_id = user_service.get_id_by_token()
    return os.path.join(UPLOAD_FILE_PATH, str(user_id), file_dir)


def getFiles(file_dir):
    root, dirs, files = os.walk(file_dir).__next__()
    return {"dir": dirs, "file": files}


@cloud_space_api.route('/get_filename_list', methods=['GET'])
def get_filename_list():
    """
    获取文件列表
    ---
    tags:
      - cloud_space_api
    responses:
      500:
        description: server err
      200:
        description: success
    """
    user_id = user_service.get_id_by_token()
    vo_list = UserCloudSpaceVO.query.filter(UserCloudSpaceVO.user_id == user_id).all()
    name_list = [vo.file_name for vo in vo_list]
    return jsonify(res_util.success(name_list))


@cloud_space_api.route('/file_upload', methods=['POST'])
def file_upload():
    """
    上传一个文件
    ---
    tags:
      - cloud_space_api
    parameters:
      - in: formData
        name: file
        type: file
        required: true
        description: upload a file
    responses:
      500:
        description: server err
      200:
        description: success
    """
    file1 = request.files["file"]
    user_id = user_service.get_id_by_token()
    vo = UserCloudSpaceVO.query.filter_by(file_name=file1.filename, user_id=user_id).first()
    time_str = time.strftime('%Y%m%d_%H%M%S_') + str(random.randint(1000, 9999))
    file_path = UPLOAD_FILE_PATH + '/' + time_str + "-" + file1.filename
    file1.save(file_path)  # 保存文件到指定路径
    if vo:
        os.remove(vo.file_path)
        vo.file_path = file_path
        db.session.commit()
    else:
        user_id = user_service.get_id_by_token()
        vo = UserCloudSpaceVO(user_id=user_id, file_name=file1.filename, file_path=file_path)
        db.session.add(vo)
        db.session.commit()
    return jsonify(res_util.success("success"))


@cloud_space_api.route('/file_download', methods=['GET'])
def file_download():
    """
    下载一个文件
    ---
    tags:
      - cloud_space_api
    parameters:
     - name: filename
       type: string
       required: true
       description: user_id
       in: query
       example: 1
    responses:
      500:
        description: server err
      200:
        description: success
    """
    user_id = user_service.get_id_by_token()
    filename = request.args.get("filename")
    vo = UserCloudSpaceVO.query.filter_by(file_name=filename, user_id=user_id).first()
    response = make_response(send_file(vo.file_path))
    response.headers["Content-Disposition"] = "attachment; filename={};".format(filename).encode("utf_8").decode(
        'latin-1')
    return response


@cloud_space_api.route('/delete_file', methods=['POST'])
def delete_file():
    """
    删除一个文件
    ---
    tags:
      - cloud_space_api
    parameters:
      - in: body
        name: body
        description:
          文件名
        required: true
        schema:
          required:
            - filename
          properties:
            filename:
              description: filename
              type: string
              example: a.txt
    responses:
      500:
        description: server err
      200:
        description: success
    """
    data = request.get_json()
    filename = data.get("filename")
    user_id = user_service.get_id_by_token()
    vo = UserCloudSpaceVO.query.filter_by(file_name=filename, user_id=user_id).first()
    os.remove(vo.file_path)
    db.session.delete(vo)
    db.session.commit()
    return jsonify(res_util.success("success"))
