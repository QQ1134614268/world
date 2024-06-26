import os

from flask import request
from flask import send_file
from flask_restful import Resource

from config.conf import world_env
from config.enum_conf import FileServeDirEnum
from config.exception import WorldException
from config.log_conf import logger
from util import res_util
from util.file_util import get_file_name_by_uuid


class FileApi2(Resource):

    def get(self, path):
        full_path = os.path.join(world_env.upload_file_path2, path)
        if os.path.isfile(full_path):
            return send_file(full_path, as_attachment=True, attachment_filename=full_path.split('/')[-1])
        logger.info("文件不存在: " + full_path)
        return res_util.fail("参数异常")

    def post(self):
        file = request.files["file"]
        f_name = get_file_name_by_uuid(file.filename)
        full_path = os.path.join(world_env.upload_file_path2, f_name)
        file.save(full_path)
        return res_util.success(world_env.upload_file_dir_name + f_name)


class FileApi3(Resource):

    def get(self, file_dir, file_name):
        full_path = os.path.join(world_env.upload_file_path2, file_dir, file_name)
        if os.path.isfile(full_path):
            return send_file(full_path, as_attachment=True, attachment_filename=full_path.split('/')[-1])
        logger.info("文件不存在: " + full_path)
        return res_util.fail("参数异常")

    def post(self, file_dir):
        if file_dir not in FileServeDirEnum.__members__:
            raise WorldException("不存在路径")
        file = request.files["file"]
        f_name = get_file_name_by_uuid(file.filename)
        full_path = os.path.join(world_env.upload_file_path2, file_dir, f_name)
        file.save(full_path)
        return res_util.success(f"/FILE_SERVE/{file_dir}/{f_name}")


if __name__ == '__main__':

    print(os.listdir())
    for root, dirs, files in os.walk("", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    root, dirs, files = os.walk("").__next__()
    print("--", root, dirs, files)
