# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from datetime import datetime
from io import BytesIO

import openpyxl
from flask import request, make_response, send_file, Blueprint
from flask_restful import Resource
from openpyxl import Workbook
from sqlalchemy import and_, insert, func

import service
from config.conf import DATE_FORMAT
from config.enum_conf import DateType
from config.mysql_db import db
from service import worker_service
from util import res_util, time_util, db_util
from vo.table_model import WorkerVO, WorkerTimeVO

# from sqlalchemy.dialects.mysql import insert

header_dic = {
    "name": "姓名",
    "id_card_number": "身份证",
    "phone": "电话",
    "sex": "性别",
    "birthday": "生日",
    "start_time": "入职日期",
    "pay": "薪资",
}

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
            val["belong"] = service.token_service.get_id_by_token()
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
        vos = WorkerVO.query.filter(WorkerVO.belong == service.token_service.get_id_by_token()).all()
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
        data["belong"] = service.token_service.get_id_by_token()
        vo = WorkerVO(**data)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        page = request.args.get("currentPage", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        user_id = service.token_service.get_id_by_token()
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
        WorkerVO.query.filter(id=_id).update(**data)
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
        return worker_service.add_worker_time(data)

    def get(self, _id):
        date = request.args.get("date", time_util.getLocalTimeStr(DATE_FORMAT), str)
        name = request.args.get("name")
        page = request.args.get("currentPage", 1, int)
        page_size = request.args.get("pageSize", 15, int)
        user_id = service.token_service.get_id_by_token()

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
        return worker_service.update_worker_time(data)


class WorkTimeAnalyseApi(Resource):
    """工时统计"""

    @staticmethod
    @work_time_analyse_api.route('/get_sum_time/<int:_id>', methods=['GET'])
    def get_sum_time(_id):
        date_str = request.args.get("date", time_util.getLocalTimeStr(DATE_FORMAT))
        name = request.args.get("name")
        date_type = request.args.get("dateType", "date")
        date = datetime.strptime(date_str, DATE_FORMAT)
        end_day = date + DateType[date_type].value
        user_id = service.token_service.get_id_by_token()
        query_filter = [WorkerVO.belong == user_id,
                        WorkerTimeVO.date >= date_str,
                        WorkerTimeVO.date <= end_day]
        if name:
            query_filter.append(WorkerVO.name.contains(name))
        res = WorkerVO.query.outerjoin(
            WorkerTimeVO,
            and_(WorkerTimeVO.worker_id == WorkerVO.id)
        ).with_entities(
            WorkerVO.id,
            WorkerVO.name,
            func.sum(WorkerTimeVO.morning),
            func.sum(WorkerTimeVO.noon),
            func.sum(WorkerTimeVO.afternoon),
            func.sum(WorkerTimeVO.night),
            func.sum(WorkerTimeVO.hours),
        ).filter(
            *query_filter
        ).group_by(
            WorkerVO.id
        ).all()
        return res_util.json_success(db_util.row_to_dic(res))
