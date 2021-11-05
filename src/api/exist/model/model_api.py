from io import BytesIO

from flask import jsonify, request, send_file
from flask_restful import Resource

from api.exist.model.Util import Res
from api.exist.model.model import ProveVO, StoryVO
from config.mysql_db import db
from util import res_util


class ProveApi(Resource):
    @staticmethod
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
        return Res.delete(_id, ProveVO)


class Prove2Api(Resource):
    @staticmethod
    def get(_id):
        value = request.args.get("value")
        vos = ProveVO.query.filter(ProveVO.value.contains(value)).all()
        return jsonify(res_util.success(vos))


class StoryApi(Resource):
    def get(self, _id):
        return Res.get(_id, StoryVO)

    def post(self, _id):
        return Res.add(StoryVO, request.get_json())

    def put(self, _id):
        return Res.update(_id, StoryVO, request.get_json())

    def delete(self, _id):
        return Res.delete(_id, StoryVO)


class UploadDataApi(Resource):
    def post(self, _id):
        # 增量, 全量
        file = request.files["file"]
        lines = file.readlines()
        line_list = []
        for line in lines:
            new_line = line.replace("\r\n", "").replace("\t", " " * 4).replace("\n", "").replace(":", "")
            if not new_line.isspace():
                line_list.append(new_line)

        for index, parent_line in enumerate(line_list):
            level = self.get_level(parent_line)
            if level == 0:
                vo = ProveVO(parent_id=1, value=parent_line)
                db.session.add(vo)
                db.session.flush()
                self.find_children(vo, level, line_list[index + 1:])
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
        lines = list(self.get_line(0, root))
        bytes_io = BytesIO()
        for line in lines:
            bytes_io.write((line + "\n").encode("utf-8"))
        # bytes_io.write("\n".join(lines).encode("utf-8"))
        bytes_io.seek(0)
        return send_file(bytes_io, as_attachment=True, attachment_filename="dump.yml")

    def get_line(self, deep, arr):
        for val in arr:
            line = " " * deep * 4 + val["value"]
            yield line
            if val.get("children"):
                for i in self.get_line(deep + 1, val["children"]):
                    yield i

    def find_children(self, p_vo, level, lines):
        for index, line in enumerate(lines):
            new_level = self.get_level(line)
            # 找出子节点,给子节点p_id
            if level + 1 == new_level:
                vo = ProveVO(parent_id=p_vo.id, value=line)
                db.session.add(vo)
                db.session.flush()
                self.find_children(vo, new_level, lines[index + 1:])
            elif level + 1 > new_level:
                break

    @staticmethod
    def get_level(line: str):
        new = line.lstrip()
        len_space = len(line) - len(new)
        return bool(len_space % 4) + len_space // 4
