# -*- coding:utf-8 -*-
"""
@Time: 2021/3/31
@Description:
"""

from functools import wraps

import service.token_service
from service import user_service
from util.log_util import logger
from vo.table_model import UserVO


class Permission:  # 权限常量
    FOLLOW = 0x01  # 关注用户
    COMMENT = 0x02  # 发表评论
    WRITE_ARTICLES = 0x04  # 写文章
    MODERATE_COMMENTS = 0x08  # 管理他们发表的评价
    ADMINISTER = 0x80  # 管理员权限


class Role:  # 权限常量
    FOLLOW = 0x01  # 关注用户
    COMMENT = 0x02  # 发表评论
    WRITE_ARTICLES = 0x04  # 写文章
    MODERATE_COMMENTS = 0x08  # 管理他们发表的评价
    ADMINISTER = 0x80  # 管理员权限


# class Role(db.Model):
#     __tablename__ = "roles"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), unique=True)
#     default = db.Column(db.Boolean, default=False, index=True)
#     permissions = db.Column(db.Integer)
#     users = db.relationship("User", backref="role", lazy="dynamic")

def get_curr_user():
    user_id = service.token_service.get_id_by_token()
    user_vo = UserVO.query.filter(UserVO.id == user_id).one()
    return user_vo


def get_curr_user_role():
    user_id = get_curr_user()
    user_vo = UserVO.query.filter(UserVO.id == user_id).one()


def get_curr_user_permission():
    user_id = get_curr_user()
    user_vo = UserVO.query.filter(UserVO.id == user_id).one()


def permission_required(permission):
    '''定义装饰器@permission_required(permission)'''

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if permission not in get_curr_user_permission():
                raise Exception("无权限")
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    '''定义装饰器@admin_required'''
    return permission_required(Permission.ADMINISTER)(f)


def own_resource():
    pass


def set_model_user_id(model):
    try:
        model.user_id = service.token_service.get_id_by_token()
    except Exception as e:
        logger.exception(str(e))
