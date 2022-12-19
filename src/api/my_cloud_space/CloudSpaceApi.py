# -- coding:UTF-8 --
import os
import random
import shutil

import time
from flask import Blueprint, send_file, request
from flask_restful import Resource

import service.user_service
from config.dir_conf import DATA_DIR, UPLOAD_FILE_PATH
from config.mysql_db import db
from util import res_util
from vo.table_model import UserCloudSpaceVO

cloud_space_api = Blueprint("cloud_space_api", __name__, url_prefix='/api/cloud_space_api')


@cloud_space_api.route('/init', methods=['GET'])
def init():
    user_id = service.user_service.get_id_by_token()
    os.makedirs(os.path.join(UPLOAD_FILE_PATH, str(user_id)))
    return res_util.success("cloud_space init success")


@cloud_space_api.route('/create_dir', methods=['POST'])
def create_dir():
    data = request.get_json()
    name = data.get('name')
    user_id = service.user_service.get_id_by_token()
    os.makedirs(os.path.join(UPLOAD_FILE_PATH, str(user_id)), name)
    return res_util.success()


@cloud_space_api.route('/get_filename_list_v2', methods=['POST'])
def get_filename_list_v2():
    data = request.get_json()
    name = data.get('name')
    file_dir = getDirName(name)
    ret = getFiles(file_dir)
    return res_util.success(ret)


def getDirName(file_dir):
    user_id = service.user_service.get_id_by_token()
    return os.path.join(UPLOAD_FILE_PATH, str(user_id), file_dir)


def getFiles(file_dir):
    root, dirs, files = os.walk(file_dir).__next__()
    return {"dir": dirs, "file": files}


@cloud_space_api.route('/get_filename_list', methods=['GET'])
def get_filename_list():
    user_id = service.user_service.get_id_by_token()
    vo_list = UserCloudSpaceVO.query.filter(UserCloudSpaceVO.user_id == user_id).all()
    name_list = [vo.file_name for vo in vo_list]
    return res_util.success(name_list)


@cloud_space_api.route('/file_upload', methods=['POST'])
def file_upload():
    file1 = request.files["file"]
    user_id = service.user_service.get_id_by_token()
    vo = UserCloudSpaceVO.query.filter_by(file_name=file1.filename, user_id=user_id).first()
    time_str = time.strftime('%Y%m%d_%H%M%S_') + str(random.randint(1000, 9999))
    file_path = UPLOAD_FILE_PATH + '/' + time_str + "-" + file1.filename
    file1.save(file_path)  # 保存文件到指定路径
    if vo:
        os.remove(vo.file_path)
        vo.file_path = file_path
        db.session.commit()
    else:
        user_id = service.user_service.get_id_by_token()
        vo = UserCloudSpaceVO(user_id=user_id, file_name=file1.filename, file_path=file_path)
        db.session.add(vo)
        db.session.commit()
    return res_util.success()


@cloud_space_api.route('/file_download', methods=['GET'])
def file_download():
    user_id = service.user_service.get_id_by_token()
    filename = request.args.get("filename")
    vo = UserCloudSpaceVO.query.filter_by(file_name=filename, user_id=user_id).first()
    return send_file(vo.file_path, as_attachment=True, attachment_filename=filename)


@cloud_space_api.route('/delete_file', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get("filename")
    user_id = service.user_service.get_id_by_token()
    vo = UserCloudSpaceVO.query.filter_by(file_name=filename, user_id=user_id).first()
    os.remove(vo.file_path)
    db.session.delete(vo)
    db.session.commit()
    return res_util.success()


class CloudSpaceApi(Resource):

    def get(self):
        path = request.args.get("path", "")
        full_path = os.path.join(DATA_DIR, path)
        if not os.path.exists(full_path):
            return res_util.fail("参数异常")
        if os.path.isdir(full_path):
            # root, dirs, files = os.walk(".").__next__()
            return res_util.success(os.listdir())
        return send_file(full_path, as_attachment=True, attachment_filename=full_path)

    def post(self):
        path = request.form.get("path")
        dir_name = request.form.get("dir")
        full_path = os.path.join(path, dir_name)
        # 异常直接抛出,不再校验异常情况
        # if not os.path.exists(path):
        #     return res_util.fail()
        if dir_name:
            os.mkdir(full_path)
            return res_util.success()
        file = request.files["file"]
        file.save(full_path)
        return res_util.success(full_path)

    def delete(self):
        path = request.get_json("path")
        shutil.rmtree(path)
        return res_util.success()
