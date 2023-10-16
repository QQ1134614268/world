from flask import Blueprint, request

from api.code.model import MysqlTables, JsForm, MysqlColumns
from config.mysql_db import db
from util import res_util

code_blueprint_api = Blueprint("code_blueprint_api", __name__, url_prefix='/api/code_api/code_blueprint_api')


class CodeApi:
    """code"""

    @staticmethod
    @code_blueprint_api.route('/get_tables', methods=['GET'])
    def get_tables():
        table_schema = request.args.get("table_schema")
        query = db.session.query(MysqlTables)
        if table_schema:
            query.filter(MysqlTables.TABLE_SCHEMA == table_schema)
        vos = query.with_entities(
            MysqlTables.TABLE_NAME,
            MysqlTables.TABLE_SCHEMA,
            MysqlTables.TABLE_COMMENT
        ).distinct().all()
        # vos = UserVO.query.filter().distinct().all()
        return res_util.success(vos)

    @staticmethod
    @code_blueprint_api.route('/get_table_cols', methods=['GET'])
    def get_table_cols():
        table_schema = request.args.get("table_schema")
        table_name = request.args.get("tableName")
        vos = db.session.query(MysqlColumns).filter(
            MysqlColumns.TABLE_SCHEMA == table_schema,
            MysqlColumns.TABLE_NAME == table_name
        ).all()

        return res_util.success(vos)

    @staticmethod
    @code_blueprint_api.route('/get_data', methods=['GET'])
    def get_data():
        # todo
        table_schema = request.args.get("table_schema")
        table_name = request.args.get("table_name")
        vos = db.session.query(JsForm).filter(
            JsForm.TABLE_SCHEMA == table_schema,
            JsForm.TABLE_NAME == table_name
        ).all()
        return res_util.success(vos)
