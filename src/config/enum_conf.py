# -*- coding:utf-8 -*-
"""
@Time: 2021/1/31
@Description: 
"""
from enum import Enum, unique


class ExceptionCode(Enum):
    # 成功
    SUCCESS = 1

    # 失败, 一般参数问题, 反馈用户
    FAIL = 2

    # 未登录
    NO_LOGIN_FAIL = 8

    # 程序异常, 反馈eg: 服务器发生异常
    EXCEPTION = 4


@unique
class Role(Enum):  # 权限常量
    ADMIN = "管理员"
    NORMAL_ROLE = "普通用户"
    NO_REGISTER = "非注册用户"
    LIMITED_ROLE = "受限用户"


class Permission(Enum):
    INVITATION_CODE = "邀请码权限"

    # @classmethod
    # def _missing_(cls, value):
    #     return Permission.INVITATION_CODE


# 用户分类(层级菜单(新浪微博,个人与公司)) 普通用户(vip,好友,同学,亲人,同事,商业伙伴,反馈者),公司(我的公司,伙伴公司),组织,团体, 陌生(其他,非通过,类似邮件消息)
class UserType(Enum):
    normal = 1
    company = 2
    organization = 4
    group = 8
    strange = 16


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
