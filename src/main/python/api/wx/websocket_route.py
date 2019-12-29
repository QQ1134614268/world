import json


# 字符串转函数  https://www.jb51.net/article/120311.htm
# 创建集合 字符串 找对应函数  类似注册路由

def login(json_data):
    # {func:"/user/login", #登录
    # args:{
    # id:111
    # }}
    pass
from util.LogUtil import  logger
from api.wx.gloable_v import user_id_socket
def chat(json_data):
    # 确定消息发送成功 or发送失败判-类似sessionid 是否是好友关系 是否在线 心跳维护
    to_id = json_data["to_id"] # 单聊or群聊

    msg = json_data["messsage"]
    socket=user_id_socket[to_id]
    socket.send(msg)
    response_str=socket.recive()
    if response_str:#确定消息发送成功
        # or发送失败判 - 类似sessionid
        logger.debug("接收返回消息"+response_str)


def upload_file(json_data):
    # {func:/file_api/upload_file, #发文件
    # args:{
    # to_id:1 ,
    # file: bbb
    # }}
    pass


def update_user_info(json_data):
    # {func:/user/update_user_info, #更改用户信息
    # args:{
    # name:1 ,
    # age:111,
    # sex:1,
    # }}
    pass


# 添加注解 todo
func_route_dic = {
    "/user/login": login,
    "/user/chat": chat,
    "/file_api/upload_file": upload_file,
    "/user/update_user_info": update_user_info,
}


def func_handler(data):
    data_json = json.dump(data)
    route, data = data_json["route"], data_json["data"]
    func_route_dic[route](data)
