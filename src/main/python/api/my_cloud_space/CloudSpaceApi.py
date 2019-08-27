# -- coding:UTF-8 --
"""
@author:huangran
"""
import os
import random
import time

from flask import Blueprint, send_file, jsonify, make_response, request

from config import res
from db.db import db
from service import UserService
from vo.CloudSpaceVO import UserCloudSpaceVO

cloud_space_api = Blueprint("cloud_space_api", __name__, url_prefix='/cloud_space_api')


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
    user_id = UserService.get_current_userid()
    vo_list = UserCloudSpaceVO.query.filter(UserCloudSpaceVO.user_id == user_id).all()
    name_list = [vo.file_name for vo in vo_list]
    return jsonify(res.success(name_list))


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
    user_id = UserService.get_current_userid()
    vo = UserCloudSpaceVO.query.filter_by(file_name=file1.filename, user_id=user_id).first()
    time_str = time.strftime('%Y%m%d_%H%M%S_') + str(random.randint(1000, 9999))
    from app import PROJECT_DIR
    file_path = PROJECT_DIR + '/data/upload/cloud_space/' + time_str + "-" + file1.filename
    file1.save(file_path)  # 保存文件到指定路径
    if vo:
        os.remove(vo.file_path)
        vo.file_path = file_path
        db.session.commit()
    else:
        user_id = UserService.get_current_userid()
        vo = UserCloudSpaceVO(user_id=user_id, file_name=file1.filename, file_path=file_path)
        db.session.add(vo)
        db.session.commit()
    return jsonify(res.success("success"))


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
    user_id = UserService.get_current_userid()
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
    user_id = UserService.get_current_userid()
    vo = UserCloudSpaceVO.query.filter_by(file_name=filename, user_id=user_id).first()
    os.remove(vo.file_path)
    db.session.delete(vo)
    db.session.commit()
    return jsonify(res.success("success"))
