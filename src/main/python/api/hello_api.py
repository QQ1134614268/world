# encoding: utf-8
"""
@author:huangran
"""
from utity import date_utity
from config import log
from flask import Blueprint, send_file, jsonify, make_response
import time
from config import res
import io
from config import file_config
import pandas
from io import BytesIO
from flask import Response
import datetime

hello_api = Blueprint("hello", __name__, url_prefix='/hello')


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
      - hello
    responses:
      500:
        description: server error
      200:
        description: success
    """
    log.info("hello")
    return make_response(jsonify(res.success("hello world!")), 200)


@hello_api.route('/sleep', methods=["GET"])
def sleep():
    """
    This is test API
    sleep 测试单线程
    ---
    tags:
      - hello
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
    return make_response(jsonify(res.success('thread test;I slept from ' + str(start) + " to " + str(end))), 200)


@hello_api.route('/exception', methods=["GET"])
def exception():
    """
    This is test API
    exception 测试异常
    ---
    tags:
      - hello
    responses:
      500:
        description: server error
      200:
        description: success
    """
    result = 1 / 0
    return make_response(jsonify(res.success(result)), 200)


@hello_api.route('/download_excel', methods=['GET'])
def download_excel():
    from app import RESOURCE_DIR  # todo 放头部报错  因为 循环引入
    byte_array_buffer = file_config.read_into_buffer(RESOURCE_DIR + "/excel_download_test.xlsx")
    # with open(RESOURCE_DIR + "/excel_download_test.xlsx", "rb") as f:  # todo f.readlines() hit
    #     data = f.read()
    file_name = "excel下载测试.xlsx"  # todo excel 和压缩文件
    return send_file(byte_array_buffer, as_attachment=True,
                     attachment_filename=file_name.encode(encoding='utf_8', errors="ignore").decode('utf_8'),
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


@hello_api.route('/download_excel_file', methods=['GET'])
def download_excel_file():
    response = make_response(send_file("E:\\python\\world\\src\main\\resource\\Book1.xlsx"))
    response.headers["Content-Disposition"] = "attachment; filename=myfiles.xls;"
    return response


@hello_api.route('/test_download_buffer')
def test_download_buffer():
    buffer = BytesIO()
    buffer.write(b'jJust some letters.')
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, attachment_filename='a_file.txt', mimetype='text/csv')


@hello_api.route('/test_download_zip')
def test_download_zip():
    """
     This is test API
     下载zip文件
     ---
     tags:
       - hello
     responses:
       500:
         description: server error
       200:
         description: success
     """
    import zipfile

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
    byte_io = io.BytesIO()
    with zipfile.ZipFile(byte_io, mode='w') as zipf:
        zipf.writestr("告警.csv".encode(encoding="utf_8").decode(encoding="utf_8"), result_csv)
    byte_io.seek(0)
    return send_file(byte_io, mimetype='application/octet-stream', as_attachment=True,
                     attachment_filename="告警.zip")


@hello_api.route('/test_download_pandas')
def test_download_pandas():
    """
     This is test API
     pandas 导出csv
     ---
     tags:
       - hello
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


import json


class User():
    id = None
    city_name = ""


class JsonUtils:

    def json2obj(self, jsonObj, obj):
        keys = jsonObj.keys()
        for key in keys:
            if hasattr(obj, key):
                setattr(obj, key, jsonObj[key])
        return obj

    def jsonStr2obj(self, jsonstr, obj):
        objdict = json.loads(jsonstr)
        return self.json2obj(objdict, obj)

    def jsonobj2Str(self, jsonobj):
        jsonstr = json.dumps(jsonobj, ensure_ascii=False)
        return jsonstr

    def obj2json(self, city):
        dict = city.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def obj2jsonStr(self, city):
        obj_json = self.obj2json(city)
        jsonstr = json.dumps(obj_json, ensure_ascii=False)
        return jsonstr

    def __test__(self):
        cityjson = {
            "city_name": "%s你好",
            "id": "1212",
        }
        utils = JsonUtils()
        obj = utils.json2obj(cityjson, User())
        print(utils.obj2jsonStr(obj))


from flask import request, abort


@hello_api.route('/rectextbyurl', methods=['POST'])
def rec_text_byurl():
    """
    传入json数据
    ---
    tags:
      - hello_api
    parameters:
      - in: body
        name: body
        description: body sample {"name":"the url of the image","id":1}
        required: true
        schema:
            type: string
    responses:
       500:
         description: server error
       200:
         description: success
    """
    data = request.get_json()
    print(data["name"])
    print(data["id"])

    return jsonify(data)


@hello_api.route('/rectext', methods=['POST'])
def rec_text():
    """
    上传文件流
    ---
    tags:
      - hello_api
    consumes: [
          "multipart/form-data"
        ]
    parameters:
      - in: formData
        name: file
        type: file
        required: true
        description: upload a image file
    """
    if "file" not in request.files:
        abort(400)
    filebytes = request.files["file"]

    return "1"


@hello_api.route('/test', methods=['POST'])
def test():
    """
    上传多个文件，以及其他form参数
    ---
    tags:
      - hello_api
    consumes: ["multipart/form-data"]
    produces: ["application/json"]
    parameters:
      - in: formData
        name: file
        type: file
        required: true
        description: upload a image file
      - in: formData
        name: file1
        type: file
        required: false
        description: upload a image file11
      - in: formData
        name: body
        description: body sample {"imgurl":"the url of the image"}
        required: true
        type: string
    """
    if 'file' not in request.files:
        print("no file")
        abort(400)
    # bb = request.files.to_dict()
    filebytes = request.files["file"]
    print(filebytes.filename)
    aa = request.form["body"]
    print(aa)
    return aa


@hello_api.route('/api/<string:language>/', methods=['GET'])
def index(language):
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    ---
    tags:
      - hello_api
    parameters:
      - name: language
        in: path
        type: string
        required: true
        description: The language name
      - name: size
        in: query
        type: integer
        description: size of awesomeness
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
        schema:
          id: awesome
          properties:
            language:
              type: string
              description: The language name
              default: Lua
            features:
              type: array
              description: The awesomeness list
              items:
                type: string
              default: ["perfect", "simple", "lovely"]

    """

    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic",
        "simple", "powerful", "amazing",
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    import random
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )


@hello_api.route('/post_json', methods=['POST'])
def post_json():
    """
    Example endpoint return a list of colors by palette
    This is using docstring for specifications
    ---
    tags:
      - a
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
        description: Which palette to filter?
    operationId: get_colors
    consumes:
      - application/json
    produces:
      - application/json
    security:
      colors_auth:
        - 'write:colors'
        - 'read:colors'
    schemes: ['http', 'https']
    deprecated: false
    externalDocs:
      description: Project repository
      url: http://github.com/rochacbruno/flasgger
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    return


@hello_api.route('/post_json_ee', methods=['POST'])
def post_json_ee():
    """
    Film creation endpoint
    ---
    tags:
      - a
    summary: Creates a new Film
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        description:
          Film object that needs to be persisted to the database
        required: true
        schema:
          $ref: '#/definitions/Film'
    responses:
      200:
        description: Successful operation
      400:
        description: Invalid input
    """
    return


@hello_api.route('/post_json_f', methods=['POST'])
def post_json_f():
    """
    Film creation endpoint
    ---
    tags:
      - a
    summary: Creates a new Film
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        description:
          Film object that needs to be persisted to the database
        required: true
        schema:
          id: Film
          required:
            - title
            - director
            - distributor
            - release_date
            - running_time
          properties:
            title:
              description: Film's title
              type: string
              example: Interstellar
            director:
              description: Films's director
              type: string
              example: Christopher Nolan
            distributor:
              description: Films's distributor
              type: string
              example: Warner Bros. Pictures
            release_date:
              description: Films's release date
              type: string
              example: October 26, 2014
            running_time:
              description: Films's running time
              type: string
              example: 169 minutes
            running_time2:
              description: Films's running time
              type: string
              example: 169 minutes
    responses:
      200:
        description: Successful operation
      400:
        description: Invalid input
    """
    return


if __name__ == '__main__':
    JsonUtils().__test__()
