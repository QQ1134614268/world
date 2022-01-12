# -*- coding:utf-8 -*-
"""
@Time: 2021/3/31
@Description:
"""
from functools import wraps

from service import user_service
from util.log_util import logger
from vo.table_model import UserVO, UserRoleVO, RolePermissionVO


def get_curr_user():
    user_id = user_service.get_id_by_token()
    user_vo = UserVO.query.filter(UserVO.id == user_id).one()
    return user_vo


def get_curr_user_role():
    user_id = get_curr_user()
    user_vo = UserVO.query.filter(UserVO.id == user_id).one()


def get_curr_user_permission():
    user_id = get_curr_user()
    user_vo = UserVO.query.filter(UserVO.id == user_id).one()
    return user_vo


def has_permission(permission):
    user_id = get_curr_user()
    db_permission = UserVO.query.outerjoin(
        UserRoleVO, UserVO.id == UserRoleVO.user_id
    ).outjoin(
        RolePermissionVO, UserRoleVO, id == RolePermissionVO.role_id
    ).filter(UserVO.id == user_id, RolePermissionVO.id == permission).first()
    if db_permission:
        return True
    return False


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # if not has_permission(permission):
            #     raise WorldException("无权限")
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def own_resource(func):
    ...
    # @wraps(func)
    # def decorated_function(*args, **kwargs):
    #     if permission not in get_curr_user_permission():
    #         raise WorldException("无权限")
    #     return func(*args, **kwargs)
    #
    # return decorated_function


def set_model_user_id(model):
    try:
        model.user_id = user_service.get_id_by_token()
    except Exception as e:
        logger.exception(str(e))
