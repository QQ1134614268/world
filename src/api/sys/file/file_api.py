import os
import shutil

from flask import request
from flask import send_file
from flask_restful import Resource

from config.conf import DATA_DIR
from config.conf import UPLOAD_FILE_PATH2
from util import res_util
from util.file_util import get_file_name_by_uuid
from util.log_util import logger


# todo  space 云空间接口 FileApi2
class FileApi(Resource):

    def get(self):
        path = request.args.get("path", "")
        full_path = os.path.join(DATA_DIR, path)
        if not os.path.exists(full_path):
            return res_util.fail("参数异常")
        if os.path.isdir(full_path):
            # root, dirs, files = os.walk(".").__next__()
            return res_util.success(os.listdir())
        return send_file(full_path, as_attachment=True,
                         attachment_filename=full_path.split('/')[-1],
                         mimetype='application/octet-stream')

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


class FileApi2(Resource):

    def get(self):
        path = request.args.get("path", "")
        full_path = os.path.join(DATA_DIR, path)
        if os.path.isfile(full_path):
            return send_file(full_path, as_attachment=True,
                             attachment_filename=full_path.split('/')[-1],
                             mimetype='application/octet-stream')
        logger.info("文件不存在: " + full_path)

    def post(self):
        file = request.files["file"]
        # file     print()    # 打印文件名
        f_name = get_file_name_by_uuid() + "_" + file.filename
        full_path = os.path.join(UPLOAD_FILE_PATH2, f_name)
        file.save(full_path)
        return res_util.success("upload_file/" + f_name)

    def delete(self):
        path = request.get_json("path")
        shutil.rmtree(path)
        return res_util.success()


class GetFileApi3(Resource):

    def get(self):
        path = request.args.get("path", "")
        full_path = os.path.join(DATA_DIR, path)
        if os.path.isfile(full_path):
            return send_file(full_path)
        logger.info("文件不存在: " + full_path)


if __name__ == '__main__':

    print(os.listdir())
    for root, dirs, files in os.walk("", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    root, dirs, files = os.walk("").__next__()
    print("--", root, dirs, files)
