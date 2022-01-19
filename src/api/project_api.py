# -*- coding:utf-8 -*-
"""
@Time: 2020/12/14
@Description: 
"""

from flask import request
from flask_restful import Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, make_transient

from config.mysql_db import db
from util import res_util
from util.video_util import get_first_frame_loc
from vo.member_model import GoodsVO
from vo.table_model import UserVO, UserCloudSpaceVO, SuggestVO
from vo.tree_model import ProveVO, StoryVO
from vo.video_model import WorksVO


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
    cte_all = cte_part.union_all(db.session.query(ProveVO.id).filter(ProveVO.parent_id == cte_part._handle_path.id))
    result = db.session.query(ProveVO.id).select_entity_from(cte_all).all()
    ret = [item[0] for item in result]
    if ret:
        ProveVO.query.filter(ProveVO.id.notin_(ret)).delete(synchronize_session=False)
        db.session.commit()
    return res_util.success(ret)


def _handle_path(model, field):
    p = '/%'
    q = '/'
    db.session.query(model).filter(field.notlike(p)).update({field: q + field}, synchronize_session=False)
    db.session.commit()
    # UserVO.query.filter(UserVO.business_license.notlike(p)).update(
    #     UserVO.business_license == q + UserVO.business_license, synchronize_session=False)


def clear_path():
    data = [
        {"class": UserVO, "field": UserVO.avatar},
        {"class": UserVO, "field": UserVO.business_license},
        {"class": UserVO, "field": UserVO.brand},
        {"class": UserVO, "field": UserVO.resume},
        {"class": UserCloudSpaceVO, "field": UserCloudSpaceVO.file_path},
        {"class": GoodsVO, "field": GoodsVO.images},
        {"class": SuggestVO, "field": SuggestVO.image},
        {"class": WorksVO, "field": WorksVO.file},
        {"class": WorksVO, "field": WorksVO.thumbnail},
    ]
    for item in data:
        _handle_path(item["class"], item["field"], )


class ProjectInit(Resource):
    code = {
        "video": "更新视频缩略图",
        "sync_prove_api": "同步ProveVO数据",
        "clear_ProveVO_id": "清除ProveVO没有父节点数据",
        "clear_path": "整理filepath"
    }
    code2 = {
        "video": ref_first_frame_loc,
        "clear_ProveVO_id": clear_id,
        "clear_path": clear_path
    }

    def get(self):
        func_code = request.args.get("code")
        if func_code:
            return ProjectInit.code2[func_code]()
        return ProjectInit.code
