from flask import Blueprint, request

from api.wx import websocket_route
from api.wx.gloable_v import user_id_socket
from service import UserService

socket_api = Blueprint("socket_api", __name__, url_prefix='/socket_api')


@socket_api.route('/websocket', methods=['POST'])
def socket():
    client_socket = request.environ.get('wsgi.websocket')
    userId= UserService.get_id_by_token()
    user_id_socket[userId] = client_socket
    while True:
        data = client_socket.recive()
        websocket_route.func_handler(data)
