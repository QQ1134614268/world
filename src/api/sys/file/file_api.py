import os

from flask import request
from flask import send_file
from flask_restful import Resource

from config.env_default import world_env
from config.log_conf import logger
from util import res_util
from util.file_util import get_uuid_file_name


class FileApi2(Resource):

    def get(self, path):
        full_path: str = os.path.join(world_env.upload_file_path2, path)
        if os.path.isfile(full_path):
            return send_file(full_path, as_attachment=True, download_name=full_path.split('/')[-1], max_age=2592000)
        logger.info("文件不存在: " + full_path)
        return res_util.fail("参数异常")

    def post(self):
        file = request.files["file"]
        file_path = get_uuid_file_name(file.filename)
        file.save(os.path.join(world_env.upload_file_path2, file_path))
        return res_util.success(f"/api/file/FileApi2/{file_path}")


if __name__ == '__main__':

    print(os.listdir())
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    root, dirs, files = os.walk("").__next__()
    print("--", root, dirs, files)
