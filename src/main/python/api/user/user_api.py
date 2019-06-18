"""
@author:huangran
"""
from flask import Blueprint, Response
from flask import jsonify, make_response, request, json

from db.db import db
from vo.user import UserVO
import jwt
import jwt
import time
import utity
from config import jwt_config
user = Blueprint("user", __name__, url_prefix='/user')


@user.route('/register', methods=['POST'])
def register(request):  # 用户注册
    """
        管理员添加新用户: add user
        :return:
        """
    # email = request.form.get('email')
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    user = UserVO(username=username, password=UserVO.set_password(password))
    if db.session.query_property({"username": username}):
        return user.query.save()


def login(request):
    """ todo
    用户名 密码  手机号/邮箱/身份证
       微信等 联合登陆
       依赖 微信"""
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    user = UserVO(username=username, password=UserVO.set_password(UserVO, password))
    if user is not None:
        payload = {
            "username": user.username,
            "userid": user.id,
            "timestamp": int(time.time()),
            # "exp": 1448333419,
        }
        return jwt_config.get_token(payload)

# @require_GET
# def logout(request):
#     print("logout")
#     auth.logout(request)
#     return HttpResponse("退出登陆")
#
#
# # 添加公告
# @require_POST
# def addAnnouncement(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     images = request.POST.get('images')
#     video = request.POST.get('video')
#     user = AnnouncementVO(title=title, content=content, images=images, video=video)
#     user.save()
#     return HttpResponse("操作成功")
#
#
# # 公告栏
# @require_GET
# def getAnnouncement(request):
#     announcementVOList = AnnouncementVO.objects.all().order_by('createTime')
#     from django.core import serializers
#     ret = serializers.serialize("json", announcementVOList, ensure_ascii=False)
#     return HttpResponse(ret)
#
#
# # 意见栏
# @require_POST
# def addSuggest(request):
#     content = request.POST.get('content')
#     images = request.POST.get('images')
#     video = request.POST.get('video')
#     print(content, '99999999999999999999')
#     user = MessageVO(content=content, images=images, video=video)
#     user.save()
#     return HttpResponse("操作成功")
#
#
# # 公告栏
# @require_GET
# def getSuggest(request):
#     list = MessageVO.objects.all().order_by('createTime')
#
#     return HttpResponse(ResultVO.success(list))
