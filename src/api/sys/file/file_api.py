import os

from flask import request
from flask import send_file
from flask_restful import Resource

from config.conf import SINGLE_DIR_PATH
from config.conf import UPLOAD_FILE_PATH2
from util import res_util
from util.file_util import get_file_name_by_uuid
from util.log_util import logger


class FileApi2(Resource):

    def get(self, path):
        full_path = os.path.join(UPLOAD_FILE_PATH2, path)
        if os.path.isfile(full_path):
            return send_file(full_path, as_attachment=True,
                             attachment_filename=full_path.split('/')[-1],
                             mimetype='application/octet-stream')
        logger.info("文件不存在: " + full_path)
        return res_util.fail("参数异常")

    def post(self):
        file = request.files["file"]
        f_name = get_file_name_by_uuid(file.filename)
        full_path = os.path.join(UPLOAD_FILE_PATH2, f_name)
        file.save(full_path)
        return res_util.success("upload_file/" + f_name)

    def delete(self, _path):
        pass


class SingleDirFileApi(Resource):
    # 全局唯一
    base_dir = SINGLE_DIR_PATH

    def get(self, file_name):
        path = os.path.join(self.base_dir, file_name)
        if os.path.isfile(path):
            return send_file(path, as_attachment=True, attachment_filename=file_name,
                             mimetype='application/octet-stream')
        logger.info("文件不存在: " + path)
        return res_util.fail("参数异常")

    def post(self):
        file = request.files["file"]
        f_name = get_file_name_by_uuid(file.filename)
        file.save(os.path.join(self.base_dir, f_name))
        return res_util.success(f_name)


if __name__ == '__main__':

    print(os.listdir())
    for root, dirs, files in os.walk("", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    root, dirs, files = os.walk("").__next__()
    print("--", root, dirs, files)
