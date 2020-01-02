# from flask_socketio import SocketIO
#
# from flask_socketio import join_room, leave_room
# from flask_socketio import send, emit
#
#
# socketio = SocketIO()
#
#
# # 监听消息
# @socketio.on('message', namespace="/wechat")
# def message(message):
#     print(' message: ' + message)
#
#
# @socketio.on('my event')
# def handle_my_sustom_event(arg1, arg2, arg3):
#     print('received args: ' + arg1 + arg2 + arg3)
#
#
# def my_function_handler():
#     pass
#
#
# socketio.on_event('my event', my_function_handler, namespace='/test')
#
#
# # socketio 给客户端发送消息
# @socketio.on('message')
# def handle_message(message):
#     send(message,  json=True, namespace='/chat')
#
#
# @socketio.on('message')
# def handle_my_sustom_event(json):
#     emit('my response', json, namespace='/chat')
#
#
# @socketio.on('my event')
# def handle_my_custom_event(data):
#     emit('my response', data, broadcast=True)
#
#
# def ack():
#     print('message was received!')
#
#
# @socketio.on('my event')
# def handle_my_custom_event(json):
#     emit('my response', json, callback=ack)
#
# # 聊天室
# @socketio.on('join')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     send(username + ' has entered the room.', room=room)
#
#
# @socketio.on('leave')
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)
