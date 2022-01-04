# -*- coding:utf-8 -*-
"""
@Time: 2021/12/26
@Description:
"""
from io import BytesIO

from flask import make_response, send_file


def down_response(wb, filename):
    byte_ios = BytesIO()
    wb.save(byte_ios)
    byte_ios.seek(0)
    response = make_response(
        send_file(byte_ios, as_attachment=True, attachment_filename=filename, mimetype='application/octet-stream'))
    response.headers.add("Cache control", "no cache")
    return response
