import json
import os

from config.conf import LOG_PATH, UPLOAD_FILE_PATH
from util.log_util import logger


def init_dir():
    logger.info("init_dir start")
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    if not os.path.exists(UPLOAD_FILE_PATH):
        os.makedirs(UPLOAD_FILE_PATH)
    logger.info("init_dir end")


def init_db():
    from app import app
    with app.app_context():
        # logger.info("init_db start")
        # if not OrganizationVO.query.filter_by(id=1).first():
        #     vo = OrganizationVO(id=1, code="origin", parent_id=0, name="W&G company", level=0,
        #                         full_name="/W&G company/",
        #                         full_path_code="/origin/", full_path_id="/1/")
        #     from config.mysql_db import db
        #     db.session.add(vo)
        #     db.session.commit()
        logger.info("init_db end")


def task1(a, b):
    print(str(a) + ' ' + str(b))


def data():
    from app import app
    logger.info("定时  添加数据 ")
    url = "/wb_api/add_blog"
    data = {
        "content": "天气晴",
    }
    response = app.test_client().post(url, data=json.dumps(data), content_type='application/json',
                                      headers={
                                          "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoicm9vdCIsImlkIjoxLCJ0aW1lc3RhbXAiOjE1NzcxMTc1NDJ9.-FKeKaMO9RIyAramv5HgGHAxxVfOEIiBSvpcSLfRp_w"
                                      })
    json_data = response.data
    json_dict = json.loads(json_data)
    message = "定时  添加数据 over" if json_dict['code'] == 1 else "定时  添加数据失败"
    logger.info(message)
