from io import BytesIO

import jieba
from flask import request, send_file, Blueprint
from flask_restful import Resource
from sqlalchemy import func, desc
from sqlalchemy.orm import aliased

from config.log_conf import logger
from config.model_config import Res, ResList
from config.mysql_db import db
from util import res_util, db_util
from vo.tree_model import ProveVO, StoryVO

prove_api = Blueprint("ProveApi", __name__, url_prefix='/api/ProveBlueprintApi')


class ProveBlueprintApi:
    @staticmethod
    @prove_api.route('/prove_child/<int:_id>', methods=['GET'])
    def prove_child(_id):
        # cte 根据id 获取子节点
        cte_part = db.session.query(ProveVO).filter(ProveVO.id == _id).cte(name="hierarchy", recursive=True)
        # parent = aliased(cte_part, name="p")
        # children = aliased(ProveVO, name="c")
        # hierarchy = hierarchy.union_all(db.session.query(children).filter(children.parent_id == parent.c.id))
        cte_all = cte_part.union_all(db.session.query(ProveVO).filter(ProveVO.parent_id == cte_part.c.id))
        result = ProveVO.query.select_entity_from(cte_all).all()
        return res_util.success(result)

    @staticmethod
    @prove_api.route('/prove_parent/<int:_id>', methods=['GET'])
    def prove_parent(_id):
        # cte 根据id 获取父节点
        result = ProveBlueprintApi._prove_parent(_id)
        return res_util.success(result)

    @staticmethod
    @prove_api.route('/get_key_word/<int:_id>', methods=['GET'])
    def get_key_word(_id):
        # 高频词语
        res = ProveVO.query.with_entities(ProveVO.value).all()
        ret = [item[0] for item in res]
        bytes_res = bytes(" ".join(ret), encoding="utf-8")
        words = jieba.lcut(bytes_res)
        counts = {}
        for word in words:
            if len(word) == 1 or word.isspace():
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        result = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        result = [{"name": item[0], "count": item[1]} for item in result if item[1] > 3]
        return res_util.success(result)

    @staticmethod
    def _prove_parent(_id):
        # cte 递归查询父节点
        cte_part = db.session.query(ProveVO).filter(ProveVO.id == _id).cte(name="hierarchy", recursive=True)
        cte_all = cte_part.union_all(db.session.query(ProveVO).filter(ProveVO.id == cte_part.c.parent_id))
        result = db.session.query(ProveVO).select_entity_from(cte_all).all()
        return result

    @staticmethod
    @prove_api.route('/prove_value_parent/<int:_id>', methods=['GET'])
    def prove_value_parent(_id):
        # cte 根据value 获取父节点
        value = request.args.get("value", "")
        vos = ProveVO.query.filter(ProveVO.value.contains(value)).all()
        result = [ProveBlueprintApi._prove_parent(vo.id) for vo in vos]
        return res_util.success(result)

    @staticmethod
    @prove_api.route('/contain_value/<int:_id>', methods=['GET'])
    def get(_id):
        value = request.args.get("value", "")
        vos = ProveVO.query.filter(ProveVO.value.contains(value)).all()
        return res_util.success(vos)

    @staticmethod
    @prove_api.route('/much_children/<int:_id>', methods=['GET'])
    def much_children(_id):
        prove_right = aliased(ProveVO, name='r')
        res = ProveVO.query.outerjoin(
            prove_right, ProveVO.parent_id == prove_right.id
        ).group_by(
            ProveVO.parent_id
        ).order_by(
            desc("count")
        ).with_entities(
            prove_right.id, prove_right.value, func.count(ProveVO.parent_id).label("count")
        ).limit(10).all()

        # prove_right = aliased(ProveVO, name='r')
        # db.session.execute('SET session sql_mode=""')
        # vos = ProveVO.query.outerjoin(
        #     prove_right, ProveVO.parent_id == prove_right.id
        # ).group_by(
        #     ProveVO.parent_id
        # ).order_by(
        #     ProveVO.parent_id.desc()
        # ).limit(10).all()
        ret = db_util.row_to_dic(res)
        return res_util.success(ret)

    @staticmethod
    @prove_api.route('/popular_word/<int:_id>', methods=['GET'])
    def popular_word(_id):
        vos = ProveVO.query.order_by(ProveVO.wight.desc()).limit(10).all()
        return res_util.success(vos)


def count_prove(function):
    def wrapper(*args, **kw):
        if kw.get("_id") == 0:
            _id = request.args.get("parent_id")
            ProveVO.query.filter(ProveVO.id == _id).update({ProveVO.wight: ProveVO.wight + 1})
            db.session.commit()
        res = function(*args, **kw)
        return res

    return wrapper


# 装饰器为函数
def timeit(fn):
    def wrap(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return ret

    return wrap


class ProveApi(Resource):
    @staticmethod
    @count_prove
    def get(_id):
        return Res.get(_id, ProveVO)

    @staticmethod
    def post(_id):
        return Res.add(ProveVO, request.get_json())

    @staticmethod
    def put(_id):
        return Res.update(_id, ProveVO, request.get_json())

    @staticmethod
    def delete(_id):
        # 删除子集
        cte_part = db.session.query(ProveVO.id).filter(ProveVO.id == _id).cte(name="hierarchy", recursive=True)
        cte_all = cte_part.union_all(db.session.query(ProveVO.id).filter(ProveVO.parent_id == cte_part.c.id))
        result = db.session.query(ProveVO.id).select_entity_from(cte_all).all()
        ret = [item[0] for item in result]
        ProveVO.query.filter(ProveVO.id.in_(ret)).delete(synchronize_session=False)
        db.session.commit()
        return res_util.success(ret)
        # return Res.delete(_id, ProveVO)
        # return ResList.delete()


class StoryApi(Resource):
    def get(self, _id):
        return Res.get(_id, StoryVO)

    def post(self, _id):
        return Res.add(StoryVO, request.get_json())

    def put(self, _id):
        return Res.update(_id, StoryVO, request.get_json())

    def delete(self, _id):
        return ResList.delete(_id, StoryVO)


class UploadDataApi(Resource):
    def post(self, _id):
        # 增量, 全量
        file = request.files["file"]

        lines = file.readlines()
        line_list = []

        for line in lines:
            new_line = str(line, encoding="utf-8").replace("\r\n", "").replace("\t", " " * 4).replace("\n", "").replace(
                ":", "")
            # new_line 不为空串,空白串
            if new_line.strip():
                line_list.append(new_line)

        for index, line in enumerate(line_list):
            level = self._get_level(line)
            if level == 0:
                vo = ProveVO(parent_id=1, value=line.strip())
                db.session.add(vo)
                db.session.flush()
                self._find_children(vo, level, line_list[index + 1:])
        db.session.commit()
        return res_util.success()

    def get(self, _id):
        vos = ProveVO.query.with_entities(ProveVO.id, ProveVO.parent_id, ProveVO.value).all()
        ret_list = [dict(zip(item.keys(), item)) for item in vos]
        vo_dic = {val["id"]: val for val in ret_list}

        for val in ret_list:
            if val["parent_id"] in vo_dic:
                data = vo_dic.get(val["parent_id"])
                if data.get("children"):
                    data["children"].append(val)
                else:
                    data["children"] = [val]

        root = [val for val in ret_list if val["parent_id"] == 0]
        lines = list(self._get_line(0, root))
        bytes_io = BytesIO()
        for line in lines:
            bytes_io.write((line + "\n").encode("utf-8"))
        # bytes_io.write("\n".join(lines).encode("utf-8"))
        bytes_io.seek(0)
        return send_file(bytes_io, as_attachment=True, attachment_filename="dump.yml")

    def _get_line(self, deep, arr):
        for val in arr:
            line = " " * deep * 4 + val["value"]
            yield line
            if val.get("children"):
                for i in self._get_line(deep + 1, val["children"]):
                    yield i

    def _find_children(self, p_vo, level, lines):
        for index, line in enumerate(lines):
            new_level = self._get_level(line)
            # 找出子节点,给子节点p_id
            if level + 1 == new_level:
                vo = ProveVO(parent_id=p_vo.id, value=line.strip())
                db.session.add(vo)
                db.session.flush()
                self._find_children(vo, new_level, lines[index + 1:])
            elif level + 1 > new_level:
                break

    @staticmethod
    def _get_level(line: str):
        new = line.lstrip()
        len_space = len(line) - len(new)
        if bool(len_space % 4):
            logger.info('数据异常,有空格', line, len_space % 4)
        return len_space // 4
