# -*- coding:utf-8 -*-
"""
@Time: 2021/3/31
@Description:
"""
from functools import wraps

from config.exception import WorldException
from config.log_conf import logger
from service import user_service
from vo.table_model import UserRoleVO, RolePermissionVO


def _has_permission(permission):
    user_id = user_service.get_id_by_token()
    db_permission = UserRoleVO.query.outerjoin(
        RolePermissionVO, UserRoleVO.role == RolePermissionVO.role
    ).filter(
        UserRoleVO.user_id == user_id, RolePermissionVO.permission == permission
    ).with_entities(
        RolePermissionVO.permission
    ).scalar()
    if db_permission:
        return True
    return False


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not _has_permission(permission):
                raise WorldException("无权限")
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
    # return decorated_function


def set_model_user_id(model):
    try:
        model.user_id = user_service.get_id_by_token()
    except Exception as e:
        logger.exception(str(e))
