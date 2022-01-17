# -*- coding:utf-8 -*-
"""
@Time: 2021/12/26
@Description:
"""
from flask import make_response, send_file


def down_response(byte_ios, filename):
    response = make_response(
        send_file(byte_ios, as_attachment=True, attachment_filename=filename, mimetype='application/octet-stream'))
    response.headers.add("Cache-Control", "no-store")
    return response
