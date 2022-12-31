# -*- coding:utf-8 -*-
"""
@Time: 2020/7/5
@Description: pass
"""
import traceback
from functools import reduce
from io import BytesIO

import jinja2
from flask import request, Blueprint, send_file
from flask_restful import Resource
from sqlalchemy import and_, func, asc, desc
from sqlalchemy.dialects.mysql import insert

from config.apscheduler_conf import scheduler
from config.conf import RESOURCE_DIR, world_env
from config.log_conf import logger
from config.mysql_db import db
from service import work_service
from service.user_service import get_id_by_token
from util import res_util, db_util, mail_util
from util.excel_util import ExcelHandler, check_excel_type
from vo.table_model import UserVO
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
        return send_file(byte_ios, as_attachment=True, attachment_filename=filename)


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
        user_id = get_id_by_token()
        ret = work_service.get_day_report(user_id)
        return res_util.success(ret)


class WorkerSchedule:
    @staticmethod
    @scheduler.task('cron', id='ana_worker_time', hour=22, minute=35)
    def ana_worker_time():
        with scheduler.app.app_context():
            logger.info("统计工时-开始")
            vos = UserVO.query.outerjoin(
                WorkerVO, UserVO.id == WorkerVO.belong
            ).filter(
                and_(UserVO.email.isnot(None), WorkerVO.id.isnot(None))
            ).distinct().all()
            # .with_entities( UserVO.id, UserVO.email)
            for vo in vos:
                UserVO.query.filter()
                try:
                    data = work_service.get_day_report(vo.id)
                    tmp = list(map(lambda x: x.get("hours"), data))
                    total = 0
                    if tmp:
                        total = reduce(lambda x, y: x + y, tmp)
                    data2 = {
                        "list": data,
                        "total": total
                    }

                    # 注意一点: 其中path需要为当前python文件所在目录的完整路径，get_template内部的参数为html模板相对于该python文件所在目录的路径(相对路径)。
                    template_loader = jinja2.FileSystemLoader(searchpath=RESOURCE_DIR)
                    template_env = jinja2.Environment(loader=template_loader)
                    template_file = "template_worker_time.tpl.html"
                    template = template_env.get_template(template_file)
                    output_text = template.render(data2)
                    mail_util.send_email(output_text, vo.email, subject="工时统计", mime_text_type="html")
                except Exception as e:
                    logger.exception(e)
                    message = traceback.format_exc()
                    mail_util.send_email(message, world_env.developer_mail)
            logger.info("统计工时-结束")
            return res_util.success()
