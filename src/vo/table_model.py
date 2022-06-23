# -*- coding:utf-8 -*-
"""
@Time: 2020/12/20
@Description: 
"""

from sqlalchemy import Column, Text, String, Integer, Boolean, DateTime, Sequence, UniqueConstraint, ForeignKey, text

from config.mysql_db import db
from util.password_util import get_sha256_salt_password
from util.unique_util import get_uuid


class BaseTable(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    # create_time = Column(DateTime, default=datetime.datetime.now, comment="创建时间", server_default="")
    # update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment="修改时间")
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')
    create_by = Column(Integer, default="-1", comment="创建者id")
    update_by = Column(Integer, default="-1", comment="修改者id")


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


class SystemLevelVO(BaseTable):
    __tablename__ = 'system_level_vo'
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
    username = Column(String(255), index=True, unique=True, nullable=False, comment="用户名")
    phone = Column(String(11), comment="手机号")
    avatar = Column(String(255), comment="头像path")

    email = Column(String(60), comment="email")
    userType = Column(Integer, default=1, comment="用户类型")

    describe = Column(String(255), comment="签名")
    id_card = Column(String(255), comment="身份证")
    tiktok_number = Column(String(255), comment="抖音号")
    video_number = Column(String(255), comment="视频号")
    wechat_number = Column(String(255), comment="微信号")
    role = Column(String(255), comment="角色")

    _password = Column('password', String(255), nullable=False, comment="密码hash")

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
    user_id = Column(String(128), comment="用户id")
    role = Column(String(128), ForeignKey(EnumConfig.code, onupdate='CASCADE'), comment="角色")


class RolePermissionVO(BaseTable):
    __tablename__ = 'role_permission_t'
    role = Column(String(128), ForeignKey(EnumConfig.code, onupdate='CASCADE'), comment="角色")
    permission = Column(String(128), ForeignKey(EnumConfig.code, onupdate='CASCADE'), comment="权限")


class AnnouncementVO(BaseTable):
    __tablename__ = 'announcement'
    user_id = Column(Integer, index=True, comment="用户id")
    title = Column(String(128), index=True, comment="标题")
    content = Column(String(150), default='123456', comment="内容")
    images = Column(String(70), default='/', comment="配图path")


class SuggestVO(BaseTable):
    __tablename__ = 'suggest_t'
    content = Column(String(150), comment="内容")
    image = Column(String(70), comment="配图path")
    announcement_id = Column(Integer, comment="反馈的公告id")


class UserCloudSpaceVO(BaseTable):
    __tablename__ = 'user_cloud_space'
    user_id = Column(Integer)
    file_name = Column(String(150), comment='文件原始名称')
    file_path = Column(String(150), comment='文件路径')


class LogVO(BaseTable):
    __tablename__ = 'log_t'
    # tag: 标签
    user_id = Column(Integer, index=True, comment="用户id")
    message = Column(Text, default='', comment="消息")
    tag = Column(Text, default='', comment="标签")
    is_read = Column(Boolean, default=False, comment="是否消费")
