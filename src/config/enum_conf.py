# -*- coding:utf-8 -*-
"""
@Time: 2021/1/31
@Description: 
"""
from enum import Enum, unique


class ResponseCode(Enum):
    # 成功
    SUCCESS = 1
    # 失败, 一般参数问题, 反馈用户
    FAIL = 2

    # 失败, 返回一个json数据  一般是 list str
    JSON_DATA = 16

    # 未登录
    NO_LOGIN_FAIL = 8

    # 程序异常, 反馈eg: 服务器发生异常
    EXCEPTION = 4


@unique
class Role(Enum):
    ADMIN = "管理员"
    NORMAL_ROLE = "普通用户"
    NO_REGISTER = "非注册用户"
    LIMITED_ROLE = "受限用户"


class Permission(Enum):
    INVITATION_CODE = "邀请码权限"
    VIDEO_REVIEW = "video系统的审批权限"

    # @classmethod
    # def _missing_(cls, value):
    #     return Permission.INVITATION_CODE


class UserType(Enum):
    # 用户分类(层级菜单(新浪微博,个人与公司))
    # 普通用户(vip,好友,同学,亲人,同事,商业伙伴,反馈者),公司(我的公司,伙伴公司),组织,团体,
    # 陌生(其他,非通过,类似邮件消息)
    normal = 1
    company = 2
    organization = 4
    group = 8
    strange = 16


class ReviewEnum(Enum):
    APPROVE = "通过"
    NOT_APPROVE = "未通过"
    NONE = "待审核"
    NEXT = "待评审"


class FileServeDirEnum(Enum):
    AVATAR = "头像"


class SexEnum(Enum):
    MALE = "男性"
    FEMALE = "女性"


class StoreMemberType(Enum):
    NormalVip = "普通Vip"
    HighVip = "高级Vip"
    TopVip = "顶级Vip"
    Admin = "管理员"
    Kitchen = "厨师"
    NormalEmp = "店员"
    StoreAdmin = "店长"


class OrderStatus(Enum):
    PAYMENT_SUCCESS = "支付完成"
    UN_PAYMENT = "未支付"


class CookerStatus(Enum):
    PAYMENT_SUCCESS = ""
    UN_PAYMENT = "未支付"
