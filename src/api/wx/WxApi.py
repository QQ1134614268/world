from flask import Blueprint

from api.wx.socket import socketio
from flask_socketio import send, emit
from flask_socketio import join_room, leave_room


wx_api = Blueprint("wx_api", __name__, url_prefix='/wx_api')


# 监听消息
@socketio.on('message', namespace="/wechat")
def message(message):
    print(' message: ' + message['data'])


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_sustom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


def my_function_handler(data):
    pass


socketio.on_event('my event', my_function_handler, namespace='/test')


# socketio 给客户端发送消息
@socketio.on('message')
def handle_message(message):
    send(message, namespace='/chat')


@socketio.on('message')
def handle_my_sustom_event(json):
    emit('my response', json, namespace='/chat')

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('my event')
def handle_my_custom_event(data):
    emit('my response', data, broadcast=True)

def ack():
    print('message was received!')


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, callback=ack)


# https://www.cnblogs.com/minsons/p/8251780.html
# 当没有指定名称空间时，将使用名称为“/”的默认全局名称空间。
# 对于装饰器语法不方便的情况，可以使用on_event方法：
# def my_function_handler(data):
#       pass
# socketio.on_event('my event', my_function_handler, namespace='/test')

@socketio.on('socket_login', namespace="/wechat")
def socket_login(message):
    print('socket_login' + message['data'])
    socketio.emit("response", {'age': 18}, namespace="/wechat")


@socketio.on('event2', namespace="/wechat")
def handle_my_custom_event(arg1, arg2, arg3):
    print('event2 args: ' + str(arg1) + "--" + str(arg2) + "--" + str(arg3))


@socketio.on('event3', namespace="/wechat")
def handle_my_custom_event(json):
    print('event3: ' + str(json))
    return 'one', 2


@socketio.on('connect', namespace='/chat')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')


def ack():
    print('message was received!')


@socketio.on('event')
def handle_my_custom_event(json):
    socketio.emit('my response', json, callback=ack)


# 这些事件的消息数据可以是字符串，字节，整数或JSON  dict
@socketio.on('json', namespace="/wechat")
def handle_json(json):
    print('received json: ')

    print(type(json))


# @socketio.on('message', namespace="/wechat")
# def message(message):
#     print(' message: ' + message['data'])



@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)
