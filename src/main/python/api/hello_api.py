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

hello_api = Blueprint("hello", __name__, url_prefix='/hello')

# jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json。
# send_file
# make_response
# response
@hello_api.route('/hello', methods=["GET"])
def hello():
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    ---
    tags:
      - hello
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
        description: server error
      200:
        description: success
    """
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
    file = zipfile.ZipInfo("告警.csv")
    with zipfile.ZipFile(byte_io, mode='w') as zipf:
        zipf.writestr(file, result_csv)
    byte_io.seek(0)
    return send_file(byte_io, mimetype='application/octet-stream', as_attachment=True,
                     attachment_filename="告警.zip")


@hello_api.route('/test_download_pandas')
def test_download_pandas():
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


if __name__ == '__main__':
    JsonUtils().__test__()
