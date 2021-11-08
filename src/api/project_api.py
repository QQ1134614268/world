# -*- coding:utf-8 -*-
"""
@Time: 2020/12/14
@Description: 
"""

from flask import request
from flask_restful import Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, make_transient

from api.exist.model.model import ProveVO, StoryVO
from config.mysql_db import db
from util import res_util
from util.video_util import get_first_frame_loc
from vo.table_model import WorksVO


def ref_first_frame_loc():
    vos = WorksVO.query.all()
    for vo in vos:
        vo.thumbnail = get_first_frame_loc(vo.file)
    db.session.commit()


def sync_prove_api():
    # 直接连生产数据 --- 文件  上传
    ggok_url = "ggok.top"
    url = 'mysql+pymysql://{}:{}@{}/{}'.format('wg', "123456", ggok_url, 'world')
    engine = create_engine(url, echo=True)
    session = sessionmaker(bind=engine)()

    # ProveVO.query.delete()
    session.execute("truncate table {}".format(ProveVO.__tablename__))
    vos = session.query(ProveVO).all()
    for vo in vos:
        make_transient(vo)
    db.session.add_all(vos)

    # StoryVO.query.delete()
    session.execute("truncate table {}".format(StoryVO.__tablename__))
    sty_vos = session.query(StoryVO).all()
    for vo in sty_vos:
        make_transient(vo)
    db.session.add_all(sty_vos)

    db.session.commit()


class ProjectInit(Resource):
    code = {
        "video": "更新视频缩略图",
        "sync_prove_api": "同步ProveVO数据",
    }
    code2 = {
        "video": ref_first_frame_loc,
        "sync_prove_api": sync_prove_api,
    }

    def get(self):
        func_code = request.args.get("code")
        if func_code:
            ProjectInit.code2[func_code]()
            return res_util.success(func_code)
        return ProjectInit.code
