from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal

from api.wb.BlogVO import BlogVO, BlogCommentVO
from config import res
from db.db import db
from global_variable import UPLOAD_FILE_PATH
from service import UserService
from util.UpLoadFileUtil import get_file_name_by_uuid

wb_api = Blueprint("wb_api", __name__, url_prefix='/wb_api')


user_id_socket={}


@wb_api.route('/websocket_login', methods=['POST'])
def socket():
    client_socket = request.environ.get('wsgi.websocket')
    from service import UserService
    userId= UserService.get_id_by_token()
    user_id_socket[userId] = client_socket
    to = request.form.get('to')
    while 1:
        client_socket.recive()
        user_id_socket.get(to).send()
