# -*- coding:utf-8 -*-
"""
@Time: 2020/12/20
@Description: 
"""
import datetime

from sqlalchemy import Column, Text, String, Integer, Boolean, DateTime, Sequence, UniqueConstraint, ForeignKey

from config.mysql_db import db
from util.password_util import get_sha256_salt_password
from util.unique_util import get_uuid


class BaseTable(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    # create_user = db.Column(db.Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)
    # update_user = db.Column(db.Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)


class EnumConfig(BaseTable):
    """
    用户配置表,系统枚举,配置表

    场景:
        1. 枚举,常量 (系统,用户配置) ,,
        2. 下拉菜单,类似list
        3. 省市区级联下拉菜单

    code(value)    group_code   parent_code
    深圳            市           -1
    北京            市           -1
    深圳/龙华        区           深圳
    北京/朝阳        区           北京
    """
    __tablename__ = 'enum_config'
    create_by = Column(Integer, server_default="-1", comment="创建者id")
    parent_code = Column(String(255), Sequence('sort_seq'), comment="父级code", server_default='-1', default='-1')

    # 没父子级, 标识字段; eg: 深圳/龙华 北京/朝阳 都是区级
    group_code = Column(String(255), comment="分组code")

    # 生成唯一
    code = Column(String(255), comment="枚举key值, 唯一(相当于自带路径)", default=get_uuid, nullable=False, unique=True)

    value = Column(String(255), comment="枚举value数据", nullable=False)
    # value_type = Column(String(255), comment="配置值类型", nullable=False)
    comment = Column(String(255), comment="备注")
    sort = Column(Integer, comment="排序字段")

    # 分组下 唯一
    UniqueConstraint(parent_code, value)


class UserVO(BaseTable):
    __tablename__ = 'user'
    username = Column(String(255), index=True, unique=True, nullable=False)
    phone = Column(String(11))
    avatar = Column(String(255))

    email = Column(String(60))
    userType = Column(Integer, default=1)

    describe = Column(String(255))
    id_card = Column(String(255))  # 身份证
    business_license = Column(String(255))  # 营业执照
    brand = Column(String(255))  # 商标
    resume = Column(String(255))  # 简历
    tiktok_number = Column(String(255))  # 抖音号
    video_number = Column(String(255))  # 视频号
    wechat_number = Column(String(255))  # 微信号
    role = Column(String(255))

    _password = db.Column('password', db.String(255), nullable=False)

    # 设置访问密码的方法,并用装饰器@property设置为属性,调用时不用加括号
    @property
    def password(self):
        return self._password

    # 设置加密的方法,传入密码,对类属性进行操作
    @password.setter
    def password(self, value):
        self._password = get_sha256_salt_password(value)

    # 设置验证密码的方法
    def check_password(self, user_pwd):
        if user_pwd is not None and self._password == get_sha256_salt_password(user_pwd):
            return True
        return False


class UserRoleVO(BaseTable):
    __tablename__ = 'user_role_t'
    user_id = Column(String(128))
    role = Column(String(128), ForeignKey(EnumConfig.code, onupdate='CASCADE'))


class RolePermissionVO(BaseTable):
    __tablename__ = 'role_permission_t'
    role = Column(String(128), ForeignKey(EnumConfig.code, onupdate='CASCADE'))
    permission = Column(String(128), ForeignKey(EnumConfig.code, onupdate='CASCADE'))


class AnnouncementVO(BaseTable):
    __tablename__ = 'announcement'
    userid = Column(Integer, index=True)
    title = Column(String(128), index=True)
    content = Column(String(150), default='123456')
    images = Column(String(70), default='/')


class SuggestVO(BaseTable):
    __tablename__ = 'suggest_t'
    content = Column(String(150), default='123456')
    image = Column(String(70), default='default.jpg')
    announcement_id = Column(Integer)


class UserCloudSpaceVO(BaseTable):
    __tablename__ = 'user_cloud_space'
    user_id = Column(Integer)
    file_name = Column(String(150), comment='xxx.txt')
    file_path = Column(String(150), comment='/xxx/xxx.txt')


class LogVO(BaseTable):
    __tablename__ = 'log_t'
    # tag: 标签
    userId = Column(Integer, index=True)
    message = Column(Text, default='')
    tag = Column(Text, default='')
    is_read = Column(Boolean, default=False)
