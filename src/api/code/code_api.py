import jinja2
from flask import Blueprint, request

from api.code.code_model import JsForm, MysqlDb, MysqlTables, MysqlColumns
from config.mysql_db import db
from util import res_util

code_blueprint_api = Blueprint("code_blueprint_api", __name__, url_prefix='/api/code_api')


class CodeApi:
    """code"""

    @staticmethod
    @code_blueprint_api.route('/get_dbs', methods=['GET'])
    def get_dbs():
        vos = db.session.query(MysqlDb).all()
        return res_util.success(vos)

    @staticmethod
    @code_blueprint_api.route('/get_tables', methods=['GET'])
    def get_tables():
        table_schema = request.args.get("table_schema")
        query = db.session.query(MysqlTables)
        if table_schema:
            query.filter(MysqlTables.TABLE_SCHEMA == table_schema)
        vos = query.all()
        # vos = query.with_entities(
        #     MysqlTables.TABLE_NAME,
        #     MysqlTables.TABLE_SCHEMA,
        #     MysqlTables.TABLE_COMMENT
        # ).distinct().all()
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
    @code_blueprint_api.route('/get_table_tree', methods=['GET'])
    def get_table_tree():
        vos = db.session.query(MysqlTables).filter(MysqlTables.TABLE_SCHEMA == "world").all()
        cols = db.session.query(MysqlColumns).filter(MysqlColumns.TABLE_SCHEMA == "world").all()
        for vo in vos:
            vo.children = [col for col in cols if col.TABLE_NAME == vo.TABLE_NAME]
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

    @staticmethod
    def to_file(data_dic, path, resource_dir, template_file):
        template_loader = jinja2.FileSystemLoader(searchpath=resource_dir)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_file)
        output_text = template.render(data_dic)
        with open(path, "w", encoding="utf-8") as f:
            f.write(output_text)
