# encoding: utf-8
import asyncio
import os
import zipfile
from io import BytesIO
from threading import Thread

import pandas
import time
from flask import Blueprint, send_file
from flask import Response
from flask import request
from time import sleep

from config.dir_conf import RESOURCE_DIR
from service.auth_service import permission_required
from util import res_util
from util.log_util import logger
from util.time_util import get_now_str
from util.verification_code_util import get_verify_code

hello_api = Blueprint("hello", __name__, url_prefix='/api/hello_api')


# jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json。
# send_file
# make_response
# response
@hello_api.route('/hello', methods=["GET"])
def hello():
    # parse = reqparse.RequestParser()
    # parse.add_argument('department_id', help='部门id不正确', type=int, required=True)
    # parse.add_argument('type', help='类型不正确', type=int, required=True)
    # args = parse.parse_args()
    from app import app
    logger.info(app.config["DEBUG"])
    return res_util.success("hello world!")


@hello_api.route('/test_sleep', methods=["GET"])
def test_sleep():
    start = get_now_str()
    time.sleep(5)
    return res_util.success(f'sleep test;I slept from {start} to {get_now_str()} ')


@hello_api.route('/exception', methods=["GET"])
def exception():
    result = 1 / 0
    return res_util.success(result)


@hello_api.route('/download_excel', methods=['GET'])
def download_excel():
    filename = RESOURCE_DIR + "/excel_download_test.xlsx"
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    byte_array_buffer = buf
    file_name = "excel下载测试.xlsx"
    return send_file(byte_array_buffer, as_attachment=True, attachment_filename=file_name)


@hello_api.route('/test_download_bytes_io', methods=['GET'])
def test_download_bytes_io():
    bytes_io = BytesIO()
    bytes_io.write(b'jJust some letters.')
    bytes_io.seek(0)
    return send_file(bytes_io, as_attachment=True, attachment_filename='a_file.txt')


@hello_api.route('/test_download_zip', methods=['GET'])
def test_download_zip():
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
    return send_file(byte_io, as_attachment=True, attachment_filename="告警.zip")


@hello_api.route('/test_download_pandas', methods=['GET'])
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
    # send_file(file, as_attachment=True,  attachment_filename="告警.zip")
    return Response(result_csv, mimetype="text/csv;charset=utf-8",
                    headers={"Content-disposition": "attachment;filename=" + filename})


@hello_api.route('/post_json', methods=['POST'])
def post_json():
    data = request.get_json()
    name = data.get("name", None)
    age = data.get("age", None)
    return res_util.success({"name": name, "age": age})


@hello_api.route('/post_form_data', methods=['POST'])
def post_form_data():
    name = request.form["name"]
    file1 = request.files["file1"]
    file2 = request.files["file2"]
    return res_util.success({"name": name, "file_name1": file1.filename, "file_name2": file2.filename, })


@hello_api.route('/test_thread', methods=['GET'])
def test_thread():
    start = get_now_str()
    print("开始", get_now_str())

    def task_a(a, b=1):
        print("任务 part1", get_now_str(), a, b)
        sleep(5)
        print("任务 part2", get_now_str(), a, b)

    args = (1,)
    kwargs = {'b': 2}
    thr = Thread(target=task_a, args=args, kwargs=kwargs)
    thr.start()
    print("结束", get_now_str())
    return res_util.success("开始{},结束{},异步任务时长5秒".format(start, get_now_str()))


@hello_api.route('/test_asyncio', methods=['GET'])
def test_asyncio():
    # 携程不能提前返回, 只能多个任务节省时间, gather(task1,task2,task3,task4,)
    start = get_now_str()
    print("开始", get_now_str())

    async def test_asyncio_sleep():
        await asyncio.sleep(5)

    asyncio.run(test_asyncio_sleep())
    print("结束", get_now_str())
    return res_util.success("开始{},结束{},异步任务时长5秒".format(start, get_now_str()))


@hello_api.route('/test_base64_img/<int:_id>', methods=['GET'])
def test_base64_img(_id=None):
    _, img_byte = get_verify_code(True)
    return str(img_byte, encoding='utf-8')


@hello_api.route('/permission_required', methods=['GET'])
@permission_required("ADMIN")
def test_permission_required():
    return "hello"
