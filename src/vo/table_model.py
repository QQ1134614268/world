# -*- coding:utf-8 -*-
"""
@Time: 2020/12/20
@Description: 
"""
import datetime

from flask_restful import fields
from sqlalchemy import Column, Text, String, JSON, Integer, Float, Boolean, ForeignKey, Date, BLOB, DateTime, Sequence, \
    Time, Enum, UniqueConstraint
from sqlalchemy.orm import relationship

from config.mysql_db import db
from service.token_service import get_id_by_token


class BaseTable(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    # create_user = db.Column(db.Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)
    # update_user = db.Column(db.Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)


class BaseTable2(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    # create_user = db.Column(db.Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)
    # update_user = db.Column(db.Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)


class EnumConfig(BaseTable):
    """
    # 状态迁移--临时计算,唯一字段, eg:用户状态,系统状态,目标状态

    用户修改枚举表,
    用户配置表
    系统枚举,配置表

    校验用户权限

    场景:

        1. 枚举,常量 (系统,用户配置) ,,
        2. 下拉菜单,类似list
        3. 省市区级联下拉菜单

    树形结构????
    二维结构,目录与文件同级?? 深圳市,广东省, 市级, 直辖市, 人口????
    """
    __tablename__ = 'enum_config'
    code = Column(String(255), unique=True, comment="枚举key值")  # code唯一 or 联合唯一?? 用户code随机生成
    value = Column(String(255), comment="枚举value数据")
    # value: shenzhen,code:shenzhen_city,
    group_code = Column(String(255), unique=True, comment="分组code")  # group_code也有树形结构?,唯一
    parent_id = Column(Integer, Sequence('sort_seq'), comment="父级id", server_default='0')

    comment = Column(String(255), comment="备注")
    # cfg_value_type=Column(String(255)) 配置值类型，比如integer（整数）、html（HTML）等bool（是否），不同的值类型可以通过不同的表单来显示和编辑
    sort = Column(Integer, comment="排序字段")
    create_by = Column(String(255), server_default='SYSTEM', comment="创建者")


class UserVO(BaseTable):
    __tablename__ = 'user'
    username = Column(String(12), index=True)
    password = Column(String(128))  # todo 加密
    phone = Column(String(11))
    avatar = Column(Integer, default=1)

    email = Column(String(60))
    userType = Column(Integer, default=1)

    # avatar = Column(String(255), default="default_avatar.png")
    # username = Column(String(255), unique=True)
    # password = Column(String(255))
    # phone = Column(String(255))  # 手机号
    #
    # describe = Column(String(255))
    # id_card = Column(String(255))  # 身份证
    # business_license = Column(String(255))  # 营业执照
    # brand = Column(String(255))  # 商标
    # resume = Column(String(255))  # 简历
    # tiktok_number = Column(String(255))  # 抖音号
    # video_number = Column(String(255))  # 视频号
    # wechat_number = Column(String(255))  # 微信号
    # role = Column(String(255))


class VideoUserVO(BaseTable2):
    __tablename__ = 'video_user_t'
    avatar = Column(String(255), default="default_avatar.png")
    username = Column(String(255), unique=True)
    password = Column(String(255))
    describe = Column(String(255))
    id_card = Column(String(255))  # 身份证
    business_license = Column(String(255))  # 营业执照
    brand = Column(String(255))  # 商标
    resume = Column(String(255))  # 简历
    phone = Column(String(255))  # 手机号
    tiktok_number = Column(String(255))  # 抖音号
    video_number = Column(String(255))  # 视频号
    wechat_number = Column(String(255))  # 微信号
    role = Column(String(255))

    @staticmethod
    def get_video_user_field():
        return {
            'id': fields.Integer,
            'avatar': fields.String,
            "username": fields.String,
            "describe": fields.String,
            "id_card": fields.String,
            "business_license": fields.String,
            "brand": fields.String,
            "resume": fields.String,
            "phone": fields.String,
            "tiktok_number": fields.String,
            "video_number": fields.String,
            "wechat_number": fields.String,
            "role": fields.String,
        }


class UserInfoVO(BaseTable):
    __tablename__ = 'user_info'
    userId = Column(Integer, ForeignKey("user.id"), index=True)
    birthday = Column(Date)
    sex = Column(Boolean, default=True)
    email = Column(String(60))
    icon = Column(BLOB(300))
    weChatId = Column(String(60))
    idCard = Column(String(60))
    home = Column(String(60))
    motto = Column(String(60))


class AnnouncementVO(BaseTable):
    __tablename__ = 'announcement'
    userid = Column(Integer, index=True)
    title = Column(String(128), index=True)
    content = Column(String(150), default='123456')
    images = Column(String(70), default='/')


class MessageVO(BaseTable):
    __tablename__ = 'message'
    content = Column(String(150), default='123456')
    image = Column(String(70), default='default.jpg')
    announcement_id = Column(Integer)


class RecordVO(BaseTable):
    __tablename__ = 'record'
    user_id = Column(Integer)
    content = Column(String(150), default='123456')
    image = Column(String(70), default='default.jpg')
    video = Column(String(70), default='default.jpg')


class CommentVO(BaseTable):
    __tablename__ = 'comment'
    record_id = Column(String(150), default='123456')
    content = Column(String(150), default='123456')


class Attention(BaseTable):
    __tablename__ = 'attention_t'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    # attentionUserId = 一个user对象
    attentionUserId = Column(Integer, ForeignKey('user.id'), index=True)
    user = relationship('UserVO', backref='attention_t', foreign_keys=[userId])  # lazy='dynamic'
    attentionUser = relationship('UserVO', backref='attention_t2', foreign_keys=[attentionUserId])  # lazy='dynamic'
    # cate = db.Column(db.Enum(
    #     '最爱', '风景', '人物', '动物', '游记', '卡通', '生活', '其他'
    # ), server_default='最爱', nullable=False)
    group = Column(String(150), index=True)


class AuthVO(BaseTable):
    __tablename__ = 'auth'
    user_id = Column(Integer)
    path = Column(String(150), default='/')


class BlogVO(BaseTable):
    __tablename__ = 'blog_t'
    user_id = Column(Integer)
    content = Column(String(256))
    up_files = Column(String(1024))
    comments = db.relationship('BlogCommentVO', backref='b_c', lazy='dynamic')


class BlogCommentVO(BaseTable):
    __tablename__ = 'blog_comment_t'
    user_id = Column(Integer)
    blog_id = Column(db.Integer, db.ForeignKey('blog_t.id'))
    comment = Column(String(256))


class WorkerTime(BaseTable):
    __tablename__ = 'worker_time_t2'
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(32))

    morning_start = Column(Time)
    morning_end = Column(Time)
    noon_start = Column(Time)
    noon_end = Column(Time)
    afternoon_start = Column(Time)
    afternoon_end = Column(Time)
    evening_start = Column(Time)
    evening_end = Column(Time)

    date = Column(Date)

    json_data = Column(JSON)
    json_data2 = Column(JSON)

    note = Column(String(255), server_default="123")


class PersonSpeech(BaseTable):
    __tablename__ = 'person_speech_t'
    userId = Column(Integer)
    title = Column(String(256))
    content = Column(Text)
    group = Column(String(256))  # 分组 家人 朋友  陌生人...


class Comment(BaseTable):
    __tablename__ = 'message_comment_t'
    personSpeechId = Column(Integer, ForeignKey('person_speech_t.id'))
    content = Column(String(256))


class StoreVO(BaseTable):
    __tablename__ = 'store_t'
    name = Column(String(256), index=True)
    password = Column(String(128), default='123456')
    store_name = Column(Integer, index=True)
    phone = Column(String(11), index=True)
    user_id = Column(Integer, index=True)


class StoreMemberTable(BaseTable):
    __tablename__ = 'store_member_t'
    store_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)


class WalletVO(BaseTable):
    __tablename__ = 'wallet_t'
    user_id = Column(Integer)
    store_id = Column(Integer, index=True)
    money = Column(Float, default=0)


class WorkerVO(BaseTable):
    __tablename__ = 'worker_t'
    belong = Column(Integer)
    name = Column(String(255))
    birthday = Column(DateTime)
    id_card_number = Column(String(255))  # , unique=True
    sex = Column(Enum('男', '女'))
    pay = Column(String(255))
    start_time = Column(DateTime)
    phone = Column(String(11))


class WorkerTimeVO(BaseTable):
    __tablename__ = 'worker_time_t'
    __table_args__ = (UniqueConstraint('worker_id', 'date'),)
    worker_id = Column(Integer, ForeignKey(WorkerVO.id, ondelete='CASCADE'), index=True)
    morning = Column(Float, default=0)
    noon = Column(Float, default=0)
    afternoon = Column(Float, default=0)
    night = Column(Float, default=0)
    hours = Column(Float)
    date = Column(DateTime)
    worker = relationship(WorkerVO, backref='time', foreign_keys=[worker_id])


class UserCloudSpaceVO(BaseTable):
    __tablename__ = 'user_cloud_space'
    user_id = Column(Integer)
    file_name = Column(String(150), default='xxx.txt')
    file_path = Column(String(150), default='/xxx/xxx.txt')


class GoodsVO(BaseTable2):
    __tablename__ = 'goods_t'
    name = Column(String(256), default='123456')
    price = Column(Float)
    duration = Column(Float, default='123456')
    describe = Column(String(256), default='123456')
    images = Column(String(256), default='123456')
    store_id = Column(Integer, ForeignKey(StoreVO.id, ondelete='CASCADE'), index=True)


class OrderVO(BaseTable2):
    __tablename__ = 'order_t'
    goods_id = Column(Integer, ForeignKey(GoodsVO.id, ondelete='CASCADE'), index=True)
    user_id = Column(Integer, ForeignKey(UserVO.id, ondelete='CASCADE'), index=True)
    num = Column(Integer)


class WorksVO(BaseTable2):
    __tablename__ = 'works_t'
    user_id = Column(Integer, ForeignKey(VideoUserVO.id, ondelete='CASCADE'), index=True)
    describe = Column(String(255))
    file = Column(String(255))
    start = Column(Integer, default=0)
    thumbnail = Column(String(255))

    def to_json(self):
        dict2 = self.__dict__
        if "_sa_instance_state" in dict2:
            del dict2["_sa_instance_state"]
        return dict2


class TargetVO(BaseTable2):
    __tablename__ = 'target_t'
    user_id = Column(Integer, ForeignKey(VideoUserVO.id, ondelete='CASCADE'), index=True, default=get_id_by_token)
    title = Column(String(255))
    content = Column(String(1000))
    price = Column(Float)

    def to_json(self):
        dict2 = self.__dict__
        if "_sa_instance_state" in dict2:
            del dict2["_sa_instance_state"]
        return dict2


class InvitationCodeVO(BaseTable2):
    __tablename__ = 'invitation_code_t'
    user_id = Column(Integer)
    code = Column(String(255))
    invitation_user_id = Column(Integer)


class ProveVO(BaseTable):
    __tablename__ = 'prove_vo'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    parent_id = Column(Integer, default=0)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)
    #     name = Column(Text, default='')
    #     describe = Column(String(255), default='')
    #     data = Column(JSON)
    #     public = Column(Integer)
    #
    #     sort = Column(Integer)
    #     wight = Column(Float)
    #
    #     deleted = Column(Boolean, default=False)
    #
    #     parent_id = Column(Integer, default=0)
    #     user_id = Column(Integer)


class StoryVO(BaseTable):
    __tablename__ = 'story_vo'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    parent_id = Column(Integer)
    value = Column(Text, default='')
    sort = Column(Integer)
    wight = Column(Integer, default=1)
