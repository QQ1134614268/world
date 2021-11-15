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
    url = 'mysql+mysqlconnector://{}:{}@{}/{}'.format('wg', "123456", ggok_url, 'world')
    engine = create_engine(url, echo=True)
    session = sessionmaker(bind=engine)()

    prove_vos = session.query(ProveVO).all()
    for vo in prove_vos:
        make_transient(vo)

    story_vos = session.query(StoryVO).all()
    for vo in story_vos:
        make_transient(vo)

    ProveVO.query.delete()
    db.session.add_all(prove_vos)

    StoryVO.query.delete()
    db.session.add_all(story_vos)

    db.session.commit()
    return res_util.success("sync_prove_api")


def clear_id():
    cte_part = db.session.query(ProveVO.id).filter(ProveVO.id == 1).cte(name="hierarchy", recursive=True)
    cte_all = cte_part.union_all(db.session.query(ProveVO.id).filter(ProveVO.parent_id == cte_part.c.id))
    result = db.session.query(ProveVO.id).select_entity_from(cte_all).all()
    ret = [item[0] for item in result]
    if ret:
        ProveVO.query.filter(ProveVO.id.notin_(ret)).delete(synchronize_session=False)
        db.session.commit()
    return res_util.json_success(ret)


class ProjectInit(Resource):
    code = {
        "video": "更新视频缩略图",
        "sync_prove_api": "同步ProveVO数据",
        "clear_ProveVO_id": "清除ProveVO没有父节点数据",
    }
    code2 = {
        "video": ref_first_frame_loc,
        "clear_ProveVO_id": clear_id,
    }

    def get(self):
        func_code = request.args.get("code")
        if func_code:
            return ProjectInit.code2[func_code]()
        return ProjectInit.code
