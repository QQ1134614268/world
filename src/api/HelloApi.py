# encoding: utf-8
import datetime
import zipfile
from io import BytesIO

import pandas
from flask import Blueprint, send_file, jsonify, make_response
from flask import Response
from flask import request

from global_variable import RESOURCE_DIR
from service import HelloService
from util import FileConfig
from util import ResUtil
from util.LogUtil import logger

hello_api = Blueprint("hello", __name__, url_prefix='/api/hello_api')


# jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json。
# send_file
# make_response
# response
@hello_api.route('/hello', methods=["GET"])
def hello():
    """
    This is test API
    测试联通性
    ---
    tags:
        - hello_api
    responses:
      500:
        description: server error
      200:
        description: success
    """
    from app import app
    logger.info(app.config["DEBUG"])

    return jsonify(ResUtil.success("hello world!"))


@hello_api.route('/sleep', methods=["GET"])
def sleep():
    """
    This is test API
    sleep 测试单线程
    ---
    tags:
        - hello_api
    responses:
      500:
        description: server error
      200:
        description: success
    """
    start = datetime.datetime.utcnow()
    end = start + datetime.timedelta(seconds=30)
    while datetime.datetime.utcnow() < end:
        pass
    return jsonify(ResUtil.success('thread test;I slept from ' + str(start) + " to " + str(end)))


@hello_api.route('/exception', methods=["GET"])
def exception():
    """
    This is test API
    exception 测试异常
    ---
    tags:
        - hello_api
    responses:
      500:
        description: server error
      200:
        description: success
    """
    result = 1 / 0
    return jsonify(ResUtil.success(result))


@hello_api.route('/download_excel', methods=['GET'])
def download_excel():
    byte_array_buffer = FileConfig.read_into_buffer(RESOURCE_DIR + "/excel_download_test.xlsx")
    file_name = "excel下载测试.xlsx"
    return send_file(byte_array_buffer, as_attachment=True,
                     attachment_filename=file_name.encode(encoding='utf_8', errors="ignore").decode('utf_8'),
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


@hello_api.route('/download_excel_file', methods=['GET'])
def download_excel_file():
    response = make_response(send_file("E:\\python\\world\\resource\\Book1.xlsx"))
    response.headers["Content-Disposition"] = "attachment; filename=myfiles.xls;"
    return response


@hello_api.route('/test_download_buffer', methods=['GET'])
def test_download_buffer():
    buffer = BytesIO()
    buffer.write(b'jJust some letters.')
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, attachment_filename='a_file.txt', mimetype='text/csv')


@hello_api.route('/test_download_zip', methods=['GET'])
def test_download_zip():
    """
    This is test API
    下载zip文件
    ---
    tags:
       - hello_api
    responses:
      500:
        description: server error
      200:
        description: success
    """

    data = [{"name": 1, "age": 1, }, {"name": 1, "age": 1, }, {"name": 1, "age": 1, "sex": 2}, ]
    translate = {
        "name": "姓名",
        "age": "年龄",
    }
    column_headers = ["name", "age"]
    pandas_data = pandas.DataFrame(data)
    pandas_data = pandas_data[column_headers]
    new_columns = [translate[col] for col in pandas_data.columns]
    pandas_data.columns = new_columns
    result_csv = pandas_data.to_csv(encoding="utf_8_sig", index=False, mode="rw+")
    # io.StringIO io.BytesIO
    byte_io = BytesIO()
    with zipfile.ZipFile(byte_io, mode='w') as zipf:
        zipf.writestr("告警.csv".encode(encoding="utf_8").decode(encoding="utf_8"), result_csv)
    byte_io.seek(0)
    return send_file(byte_io, mimetype='application/octet-stream', as_attachment=True,
                     attachment_filename="告警.zip")


@hello_api.route('/test_download_pandas', methods=['GET'])
def test_download_pandas():
    """
    This is test API
    pandas 导出csv
    ---
    tags:
       - hello_api
    responses:
      500:
        description: server error
      200:
        description: success
     """
    data = [{"name": 1, "age": 1, }, {"name": 1, "age": 1, }, {"name": 1, "age": 1, "sex": 2}, ]
    translate = {
        "name": "姓名",
        "age": "年龄",
    }
    column_headers = ["name", "age"]
    pandas_data = pandas.DataFrame(data, columns=column_headers)
    pandas_data.rename(columns=translate, inplace=True)
    result_csv = pandas_data.to_csv(encoding="utf_8_sig", index=False, mode="rw+")
    filename = '导出.csv'.encode().decode('latin-1')
    filename = "attachment;filename=" + filename
    # send_file(file, mimetype='application/octet-stream', as_attachment=True,  attachment_filename="告警.zip")
    return Response(result_csv, mimetype="text/csv;charset=utf-8", headers={"Content-disposition": filename})


@hello_api.route('/post_json', methods=['POST'])
def post_json():
    """
    post_json
    ---
    tags:
        - hello_api
    summary: Creates a new User
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        description:
          User object that needs to be persisted to the database
        required: true
        schema:
          id: User
          required:
            - name
            - age
          properties:
            name:
              description: User's name
              type: string
              example: tom
            age:
              description: User's age
              type: string
              example: 11
    responses:
      200:
        description: Successful operation
      400:
        description: Invalid input
    """
    data = request.get_json()
    name = data.get("name", None)
    age = data.get("age", None)
    return jsonify(ResUtil.success({"name": name, "age": age}))


@hello_api.route('/post_formData', methods=['POST'])
def post_formData():
    """
    上传多个文件，以及其他form参数
    ---
    tags:
      - hello_api
    consumes: ["multipart/form-data"]
    produces: ["application/json"]
    parameters:
      - in: formData
        name: file_name1
        type: file
        required: true
        description: upload a image file
      - in: formData
        name: file_name2
        type: file
        required: false
        description: upload a image file11
      - in: formData
        name: name
        description: name
        required: true
        type: string
      - in: formData
        name: code
        description: code
        required: true
        type: string
    responses:
      500:
        description: server error
      200:
        description: success
    """
    name = request.form["name"]
    file1 = request.files["file1"]
    file2 = request.files["file2"]
    return jsonify(ResUtil.success({"name": name, "file_name1": file1.filename, "file_name2": file2.filename, }))


@hello_api.route('/test_vo_1_n', methods=["GET"])
def test_vo_1_n():
    """
    This is test API
    测试flask_sqlalchemy 一对多脚本
    ---
    tags:
        - hello_api
    responses:
      500:
        description: server error
      200:
        description: success
    """
    HelloService.test_vo_1_n()
    return jsonify(ResUtil.success("测试flask_sqlalchemy 一对多脚本"))


@hello_api.route('/test_vo_n_n', methods=["GET"])
def test_vo_n_n():
    """
    This is test API
    测试flask_sqlalchemy 多对多脚本
    ---
    tags:
        - hello_api
    responses:
      500:
        description: server error
      200:
        description: success
    """
    HelloService.test_vo_n_n()
    return jsonify(ResUtil.success("测试flask_sqlalchemy 一对多脚本"))


from global_variable import DATA_DIR
import os


@hello_api.route('/get_music', methods=["GET"])
def get_music():
    if request.args.get("music"):
        path = request.args.get("music")
        name = path[path.rindex("/"):-1]
        return send_file(os.path.join(DATA_DIR, "upload", path), mimetype='application/octet-stream',
                         as_attachment=True,
                         attachment_filename=name)
    music_list = ["wg/music/张卫 - 机器铃 砍菜刀.mp3", "wg/music/刘德华 - 忘情水(Live).mp3", "wg/music/大壮 - 为你我受冷风吹.mp3",
                  "wg/music/宇西 - 安和桥（Cover 宋冬野）.mp3", "wg/music/曾惜 - 讲真的.mp3", "wg/music/逃跑计划 - 夜空中最亮的星.mp3",
                  "wg/music/颜小健 - 一不小心.mp3", ]
    return jsonify(ResUtil.success(music_list))
