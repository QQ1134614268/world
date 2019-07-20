# encoding: utf-8
"""
@author:huangran
"""
from utity import date_utity
from config import log
from flask import Blueprint, send_file,  jsonify, make_response
import time
from config import res
import io
from config import file_config

hello_api = Blueprint("hello", __name__, url_prefix='/hello')

# jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json。
# send_file
# make_response
# response
@hello_api.route('/hello', methods=["GET"])
def hello():
    log.info("hello")
    return make_response(jsonify(res.success("hello world!")), 200)


@hello_api.route('/sleep', methods=["GET"])
def sleep():
    start = date_utity.get_defalut_time_str()
    time.sleep(30)
    end = date_utity.get_defalut_time_str()
    return make_response(jsonify(res.success('thread test;I slept from ' + start + " to " + end)), 200)


@hello_api.route('/exception', methods=["GET"])
def exception():
    result = 1 / 0
    return make_response(jsonify(res.success(result)), 200)


@hello_api.route('/download_excel', methods=['GET'])
def download_excel():
    from app import RESOURCE_DIR  # todo 放头部报错
    data = file_config.read_into_buffer(RESOURCE_DIR + "/excel_download_test.xlsx")
    # with open(RESOURCE_DIR + "/excel_download_test.xlsx", "rb") as f:  # todo f.readlines() hit
    #     data = f.read()
    file_name = "excel下载测试.xlsx"  # todo excel 和压缩文件
    from io import BytesIO
    # res = make_response() res.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode(
    # encoding='utf_8',errors="ignore").decode('utf_8'))
    return send_file(data, as_attachment=True,
                     attachment_filename=file_name.encode(encoding='utf_8', errors="ignore").decode('utf_8'),
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


@hello_api.route('/test_download')
def test_download():
    import csv
    row = ['hello', 'world']
    proxy = io.StringIO()

    writer = csv.writer(proxy)
    writer.writerow(row)

    # Creating the byteIO object from the StringIO Object
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode('utf-8'))
    # seeking was necessary. Python 3.5.2, Flask 0.12.2
    mem.seek(0)
    # proxy.close()

    return send_file(
        proxy,
        as_attachment=True,
        attachment_filename='test.csv',
        mimetype='text/csv'
    )


# import pandas
# from io import BytesIO
#
#
# def trans_record_data_to_io(data, rename_dict, col_order):
#     """
#     将列表数据转为excel的io对象
#     rename_dict：{"col1": "列1", "col2": "列2"}
#     col_order: ["列1", "列2"]
#     """
#     file = BytesIO()
#     df = pandas.DataFrame(data)
#     df.rename(columns=rename_dict, inplace=True)
#     writer = pandas.ExcelWriter(file, engine='xlsxwriter')
#     df.to_excel(writer, index=False, columns=col_order)
#     writer.save()  # 这个save不会落盘
#     return file.getvalue()
#
#
# @bp.route('download', methods=['GET'])
# def download():
#     data = [{"col1": 1, "col2": 2}]
#     file_io_value = trans_record_data_to_io(data,
#                                             {"col1": "手机号", "col2": "姓名"},
#                                             ["姓名", "手机号"]
#                                             )
#     file_name = str(datetime.now())[:19] + ".xlsx"
#     return Response(
#         file_io_value, mimetype="application/octet-stream",
#         headers={"Content-Disposition": "attachment;filename={0}".format(file_name)}
#     )

# # 辅助函数
# from flask import url_for
#
#
# def replace_id_to_uri(task):
#     return dict(uri=url_for('get_task', task_id=task.id, _external=True),
#                 title=task.title,
#                 description=task.description,
#                 done=task.done)
#
#
# # 查询全部
# @app.route('/todo/api/v1.0/tasks/', methods=['GET'])
# def get_tasks():
#     tasks = Todo.query.all()
#     return jsonify({'tasks': list(map(replace_id_to_uri, tasks))})
#
#
# # 查询一个
# from flask import abort
#
#
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = Todo.query.filter_by(id=task_id).first()
#     if task is None:
#         abort(404)
#
#     return jsonify({'task': replace_id_to_uri(task)})
# # 添加
# from flask import request
#
#
# @app.route('/todo/api/v1.0/tasks/', methods=['POST'])
# def create_task():
#     # 没有数据，或者数据缺少 title 项，返回 400，表示请求无效
#     if not request.json or not 'title' in request.json:
#         abort(400)
#
#     task = Todo(request.json['title'], request.json.get('description', ""), False)
#
#     db.session.add(task)
#     db.session.commit()
#     return jsonify({'task': replace_id_to_uri(task)}), 201
#
#
# # 更新
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = Todo.query.filter_by(id=task_id).first()
#     if task is None:
#         abort(404)
#
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'description' in request.json and type(request.json['description']) is not unicode:
#         abort(400)
#     if 'done' in request.json and type(request.json['done']) is not bool:
#         abort(400)
#
#     task['title'] = request.json.get('title', task['title'])
#     task['description'] = request.json.get('description', task['description'])
#     task['done'] = request.json.get('done', task['done'])
#
#     # db.session.update(task)
#     db.session.commit()
#     return jsonify({'task': replace_id_to_uri(task)})
#
#
# # 删除
# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     task = Todo.query.filter_by(id=task_id).first()
#     if task is None:
#         abort(404)
#
#     db.session.delete(task)
#     db.session.commit()
#     return jsonify({'result': True})