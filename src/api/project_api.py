# -*- coding:utf-8 -*-
"""
@Time: 2020/12/14
@Description: 
"""
import os

from flask import request
from flask_restful import Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, make_transient

from config.conf import world_env
from config.enum_conf import FileServeDirEnum
from config.log_conf import logger
from config.mysql_db import db
from util import res_util
from vo.member_model import GoodsVO
from vo.table_model import UserVO, UserCloudSpaceVO, SuggestVO
from vo.tree_model import ProveVO, StoryVO
from vo.video_model import WorksVO


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


def clear_path():
    data = [
        {"class": UserVO, "field": UserVO.avatar},
        {"class": UserCloudSpaceVO, "field": UserCloudSpaceVO.file_path},
        {"class": GoodsVO, "field": GoodsVO.image},
        {"class": SuggestVO, "field": SuggestVO.image},
        {"class": WorksVO, "field": WorksVO.file},
        {"class": WorksVO, "field": WorksVO.thumbnail},
    ]
    for item in data:
        _handle_path(item["class"], item["field"])


class ProjectScript:

    @staticmethod
    def init_dir():
        logger.info("开始--创建文件目录")
        for item in FileServeDirEnum.__members__.keys():
            path = os.path.join(world_env.data_dir, item)
            if not os.path.exists(path):
                os.makedirs(path)
        logger.info("结束--创建文件目录")


class ProjectInit(Resource):
    list_func = [
        {"id": "clear_ProveVO_id", "desc": "清除ProveVO没有父节点数据", "func": clear_id},
        {"id": "clear_path", "desc": "整理filepath", "func": clear_path},
        {"id": "init_dir", "desc": "创建文件服务器dir", "func": ProjectScript.init_dir},
        {"id": "sync_prove_api", "desc": "同步ProveVO数据", "func": sync_prove_api},
    ]

    def get(self):
        func_code = request.args.get("code")
        if func_code:
            data = {item.id: item.func for item in self.list_func}
            return data[func_code]()

        data = [{"id": item.id, "desc": item.desc} for item in self.list_func]
        return res_util.success(data)
