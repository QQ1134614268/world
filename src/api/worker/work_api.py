# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
from io import BytesIO

from flask import request, Blueprint
from flask_restful import Resource, reqparse
from sqlalchemy import and_, func, asc, desc
from sqlalchemy.dialects.mysql import insert

from config.conf import DATE_FORMAT
from config.mysql_db import db
from service.user_service import get_id_by_token
from util import res_util, db_util, time_util
from util.db_util import row_to_dic
from util.dowmload_util import down_response
from util.excel_util import ExcelHandler, check_excel_type
from vo.value_object import WorkerExcelVO
from vo.worker_model import WorkerVO, WorkerTimeVO

work_time_analyse_api = Blueprint("WorkTimeAnalyseApi", __name__, url_prefix='/api/work_api/WorkTimeAnalyseApi')


class WorkerExcelApi(Resource):
    """工人"""

    def post(self):
        file = request.files.get("file")
        check_excel_type(file.filename)
        data = ExcelHandler.from_file(file, WorkerExcelVO)
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
        try:
            db.session.execute(on_duplicate_key_stmt)
            db.session.commit()
            return res_util.success()
        except:
            return res_util.fail("请检查Excel内容")

    def get(self):
        vos = WorkerVO.query.filter(WorkerVO.belong == get_id_by_token()).all()
        wb = ExcelHandler.to_file(vos, WorkerExcelVO)
        byte_ios = BytesIO()
        wb.save(byte_ios)
        byte_ios.seek(0)
        filename = "名单.xlsx"
        return down_response(byte_ios, filename)


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
        query = WorkerVO.query.filter(*query_build)
        if request.args.get("sortBy"):
            if request.args.get("order") == "descending":
                query = query.order_by(asc(request.args.get("sortBy")))
            if request.args.get("order") == "ascending":
                query = query.order_by(desc(request.args.get("sortBy")))
        vos = query.paginate(page=page, per_page=page_size)
        return res_util.success(vos)

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
        # parse = reqparse.RequestParser()
        # parse.add_argument('stack_list', action='append', required=True)
        # args = parse.parse_args()

        data = request.get_json()
        if "name" in data:
            data.pop("name")  # todo vue修改
        vo = WorkerTimeVO(**data)
        db.session.add(vo)
        db.session.commit()
        return res_util.success(vo.id)

    def get(self, _id):
        name = request.args.get("name")
        user_id = get_id_by_token()
        query_filter = [WorkerVO.belong == user_id]
        if name:
            query_filter.append(WorkerVO.name.contains(name))
        join_filter = [WorkerTimeVO.worker_id == WorkerVO.id]
        start_date = request.args.get("startDate")
        if start_date:
            query_filter.append(WorkerTimeVO.date >= start_date)
        date = request.args.get("date")
        if date:
            join_filter.append(WorkerTimeVO.date == date)
        end_date = request.args.get("endDate")
        if end_date:
            query_filter.append(WorkerTimeVO.date <= end_date)
        res = WorkerVO.query.outerjoin(
            WorkerTimeVO,
            and_(*join_filter)
        ).with_entities(
            WorkerTimeVO.id,
            WorkerVO.id.label("worker_id"),
            WorkerVO.name,
            WorkerTimeVO.date,
            WorkerTimeVO.morning,
            WorkerTimeVO.morning_area,
            WorkerTimeVO.morning_content,
            WorkerTimeVO.noon,
            WorkerTimeVO.noon_area,
            WorkerTimeVO.noon_content,
            WorkerTimeVO.afternoon,
            WorkerTimeVO.afternoon_area,
            WorkerTimeVO.afternoon_content,
            WorkerTimeVO.night,
            WorkerTimeVO.night_area,
            WorkerTimeVO.night_content,
        ).filter(*query_filter).order_by(
            WorkerTimeVO.date).all()
        return res_util.success(res)

    def put(self, _id):
        data = request.get_json()
        if "name" in data:
            data.pop("name")  # todo vue修改
        WorkerTimeVO.query.filter(WorkerTimeVO.id)
        insert_stmt = insert(WorkerTimeVO).values(data)
        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(data)
        db.session.execute(on_duplicate_key_stmt)
        db.session.commit()
        return res_util.success()


class WorkTimeAnalyseApi(Resource):
    """工时统计"""

    @staticmethod
    @work_time_analyse_api.route('/get_sum_time/<int:_id>', methods=['GET'])
    def get_sum_time(_id):
        query_filter = [WorkerVO.belong == get_id_by_token()]
        if request.args.get("startDate"):
            query_filter.append(WorkerTimeVO.date >= request.args.get("startDate"))
        if request.args.get("endDate"):
            query_filter.append(WorkerTimeVO.date <= request.args.get("endDate"))
        if request.args.get("name"):
            query_filter.append(WorkerVO.name.contains(request.args.get("name")))
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
        ).filter(
            *query_filter
        ).group_by(
            WorkerVO.id
        ).all()
        data = db_util.row_to_dic(res)
        for item in data:
            item["days"] = (item.get("morning", 0) + item.get("noon", 0) + item.get("afternoon", 0) + item.get("night",
                                                                                                               0)) / 9
            item["money"] = item["days"] * item["pay"]
        return res_util.success(data)

    @staticmethod
    @work_time_analyse_api.route('/get_day_report/<int:_id>', methods=['GET'])
    def get_day_report(_id):
        # 日报模式
        user_id = get_id_by_token()
        query_filter = [WorkerVO.belong == user_id, WorkerTimeVO.date == time_util.get_now_str(DATE_FORMAT)]
        join_filter = [WorkerTimeVO.worker_id == WorkerVO.id]
        res = WorkerVO.query.outerjoin(
            WorkerTimeVO,
            and_(*join_filter)
        ).with_entities(
            WorkerVO.id,
            WorkerVO.name,
            WorkerTimeVO.date,
            WorkerTimeVO.morning,
            WorkerTimeVO.morning_area,
            WorkerTimeVO.morning_content,
            WorkerTimeVO.noon,
            WorkerTimeVO.noon_area,
            WorkerTimeVO.noon_content,
            WorkerTimeVO.afternoon,
            WorkerTimeVO.afternoon_area,
            WorkerTimeVO.afternoon_content,
            WorkerTimeVO.night,
            WorkerTimeVO.night_area,
            WorkerTimeVO.night_content,
        ).filter(*query_filter).order_by(
            WorkerVO.name,
        ).all()
        ret = []
        for item in row_to_dic(res):
            ret.append({
                "area": item["morning_area"] or '',
                "time": "上午",
                "content": item["morning_content"],
                "name": item["name"],
            })
            ret.append({
                "area": item["noon_area"] or '',
                "time": "中午",
                "content": item["noon_content"],
                "name": item["name"],
            })
            ret.append({
                "area": item["afternoon_area"] or '',
                "time": "下午",
                "content": item["afternoon_area"],
                "name": item["name"],
            })
            ret.append({
                "area": item["night_area"] or '',
                "time": "晚上",
                "content": item["night_content"],
                "name": item["name"],
            })

        ret = sorted(ret, key=lambda x: x["area"])
        return res_util.success(ret)
