from flask import Blueprint, request

from api.message.socket import websocket_route
from api.message.socket.gloable_v import user_id_socket

socket_api = Blueprint("socket_api", __name__, url_prefix='/api/socket_api')


@socket_api.route('/websocket/<userId>', methods=['POST', "GET"])
def socket(userId):
    client_socket = request.environ.get('wsgi.websocket')
    user_id_socket[userId] = client_socket
    while True:
        data = client_socket.receive()
        websocket_route.func_handler(data)
