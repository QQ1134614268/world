# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from io import BytesIO

import openpyxl
from flask import request, make_response, send_file, Blueprint
from flask_restful import Resource
from openpyxl import Workbook
from sqlalchemy import and_, func
from sqlalchemy.dialects.mysql import insert

from config.conf import header_dic
from config.mysql_db import db
from service.token_service import get_id_by_token
from util import res_util, db_util
from vo.table_model import WorkerVO, WorkerTimeVO

work_time_analyse_api = Blueprint("WorkTimeAnalyseApi", __name__, url_prefix='/api/work_api/WorkTimeAnalyseApi')


class WorkerExcelApi(Resource):
    """工人"""

    def post(self):
        file = request.files.get("file")
        wb = openpyxl.load_workbook(file)
        # sheet = wb["Sheet"]
        sheet = wb.active
        # get_column_letter column_index_from_string
        values = list(sheet.values)
        headers = values[0]
        header_dic_resvese = {v: k for k, v in header_dic.items()}
        en_header = [header_dic_resvese.get(header) for header in headers]
        data = []
        for v in values[1:]:
            data.append(dict(zip(en_header, v)))

        for val in data:
            val["belong"] = get_id_by_token()
        insert_stmt = insert(WorkerVO).values(data)
        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
            name=insert_stmt.inserted.name,
            birthday=insert_stmt.inserted.birthday,
            id_card_number=insert_stmt.inserted.id_card_number,
            start_time=insert_stmt.inserted.start_time,
            sex=insert_stmt.inserted.sex,
            phone=insert_stmt.inserted.phone,
            pay=insert_stmt.inserted.pay,
            belong=insert_stmt.inserted.belong,
        )
        db.session.execute(on_duplicate_key_stmt)
        db.session.commit()
        return res_util.success()

    def get(self):
        vos = WorkerVO.query.filter(WorkerVO.belong == get_id_by_token()).all()
        wb = Workbook()
        ws = wb.active
        for index, header_name in enumerate(header_dic.values()):
            ws.cell(row=1, column=(index + 1)).value = header_name

        for row_index, vo in enumerate(vos):
            for col_index, attr in enumerate(header_dic.keys()):
                ws.cell(row=(row_index + 2), column=(col_index + 1)).value = getattr(vo, attr)
        byte_ios = BytesIO()
        wb.save(byte_ios)
        byte_ios.seek(0)
        filename = "名单.xlsx"
        response = make_response(
            send_file(byte_ios, as_attachment=True, attachment_filename=filename, mimetype='application/octet-stream'))
        response.headers.add("Cache control", "no cache")
        return response


class WorkerApi(Resource):
    """工人"""

    def post(self, _id):
        data = request.get_json()
        data["belong"] = get_id_by_token()
        vo = WorkerVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        page = request.args.get("currentPage", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        user_id = get_id_by_token()
        query_build = [WorkerVO.belong == user_id]
        if request.args.get("name"):
            query_build.append(WorkerVO.name.contains(request.args.get("name")))
        if request.args.get("phone"):
            query_build.append(WorkerVO.phone == request.args.get("phone"))
        if request.args.get("idCard"):
            query_build.append(WorkerVO.id_card_number == request.args.get("idCard"))
        if request.args.get("startDate"):
            query_build.append(WorkerVO.start_time >= request.args.get("startDate"))
        if request.args.get("endDate"):
            query_build.append(WorkerVO.start_time <= request.args.get("endDate"))
        vos = WorkerVO.query.filter(*query_build).paginate(page=page, per_page=page_size)
        return res_util.page_success(vos)

    def put(self, _id):
        data = request.get_json()
        WorkerVO.query.filter(WorkerVO.id == _id).update(data)
        db.session.commit()
        return res_util.success(_id)

    def delete(self, _id):
        WorkerVO.query.filter(WorkerVO.id == _id).delete()
        db.session.commit()
        return res_util.success()


class WorkerTimeApi(Resource):
    """工时"""

    def post(self, _id):
        data = request.get_json()
        db.session.add(WorkerTimeVO(**data))
        db.session.commit()
        return res_util.success()

    def get(self, _id):
        date = request.args.get("date")
        name = request.args.get("name")
        page = request.args.get("currentPage", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        user_id = get_id_by_token()

        query_filter = [WorkerVO.belong == user_id]
        if name:
            query_filter.append(WorkerVO.name.contains(name))

        join_filter = [WorkerTimeVO.worker_id == WorkerVO.id]
        if date:
            join_filter.append(WorkerTimeVO.date == date)
        res = WorkerVO.query.outerjoin(
            WorkerTimeVO,
            and_(*join_filter)
        ).with_entities(
            WorkerVO.id,
            WorkerVO.name,
            WorkerTimeVO.date,
            WorkerTimeVO.morning,
            WorkerTimeVO.noon,
            WorkerTimeVO.afternoon,
            WorkerTimeVO.night,
            WorkerTimeVO.hours,
        ).filter(*query_filter).paginate(page=page, per_page=page_size)
        return res_util.page_success_row(res)

    def put(self, _id):
        data = request.get_json()
        insert_stmt = insert(WorkerTimeVO).values(data)
        update_data = {}
        if 'morning' in data:
            update_data['morning'] = insert_stmt.inserted.morning
        if 'noon' in data:
            update_data['noon'] = insert_stmt.inserted.noon
        if 'afternoon' in data:
            update_data['afternoon'] = insert_stmt.inserted.afternoon
        if 'night' in data:
            update_data['night'] = insert_stmt.inserted.noon

        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
            **update_data
        )
        db.session.execute(on_duplicate_key_stmt)
        db.session.commit()
        return res_util.success()


class WorkTimeAnalyseApi(Resource):
    """工时统计"""

    @staticmethod
    @work_time_analyse_api.route('/get_sum_time/<int:_id>', methods=['GET'])
    def get_sum_time(_id):
        query_filter = [WorkerVO.belong == get_id_by_token()]
        date = request.args.getlist("date[]")
        if date:
            query_filter.extend([WorkerTimeVO.date >= date[0], WorkerTimeVO.date < date[1]])
        name = request.args.get("name")
        if name:
            query_filter.append(WorkerVO.name.contains(name))

        res = WorkerVO.query.outerjoin(
            WorkerTimeVO,
            and_(WorkerTimeVO.worker_id == WorkerVO.id)
        ).with_entities(
            WorkerVO.id,
            WorkerVO.name,
            WorkerVO.pay,
            func.sum(WorkerTimeVO.morning).label('morning'),
            func.sum(WorkerTimeVO.noon).label('noon'),
            func.sum(WorkerTimeVO.afternoon).label('afternoon'),
            func.sum(WorkerTimeVO.night).label('night'),
            func.sum(WorkerTimeVO.hours).label('hours'),
        ).filter(
            *query_filter
        ).group_by(
            WorkerVO.id
        ).all()
        data = db_util.row_to_dic(res)
        for item in data:
            item["days"] = (item.get("morning") * 4.5 + item.get("noon") * 2 + item.get("afternoon") * 4.5 + item.get(
                "night") * 4.5) / 9
            item["money"] = item["days"] * item["pay"]
        return res_util.json_success(data)

    @staticmethod
    @work_time_analyse_api.route('/get_day_report/<int:_id>', methods=['GET'])
    def get_day_report(_id):
        # 日报模式

        return res_util.json_success()
