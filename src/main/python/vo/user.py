"""
@author:huangran
"""

from db.db import db


# 创建User模型
class UserVO(db.Model):
    __tablename__ = 'user'  # 起表名
    id = db.Column(db.Integer, primary_key=True, comment="主键")  # TODO 注释
    username = db.Column(db.String(12), index=True)
    password = db.Column(db.String(128), default='123456')
    birthday = db.Column(db.Date)
    sex = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(60), default='793390457@qq.com')
    icon = db.Column(db.String(70), default='default.jpg')

    phone = db.Column(db.String(11))
    active = db.Column(db.Boolean, default=True)

    # sign ....

    def __str__(self):
        return self.username

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @staticmethod
    def get_password(password):
        return password

    def __str__(self):
        return "Users(id='%s')" % self.id


class AnnouncementVO(db.Model):
    __tablename__ = 'announcement'  # 起表名
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    title = db.Column(db.String(128), index=True)
    content = db.Column(db.String(150), default='123456')
    createTime = db.Column(db.DateTime)
    images = db.Column(db.String(70), default='default.jpg')


class MessageVO(db.Model):
    __tablename__ = 'announcement'  # 起表名
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    content = db.Column(db.String(150), default='123456')
    createTime = db.Column(db.DateTime)
    images = db.Column(db.String(70), default='default.jpg')


class InnerVO(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    inner = db.Column(db.String(150), default='123456')


class ComplexVO(db.Model):
    __tablename__ = 'complex'  # 起表名
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    content = db.Column(db.String(150), default='123456')
    createTime = db.Column(db.DateTime)
    images = db.Column(db.String(70), default='default.jpg')


class RecordVO(db.Model):
    __tablename__ = 'record'  # 起表名
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    content = db.Column(db.String(150), default='123456')
    images = db.Column(db.String(70), default='default.jpg')
    video = db.Column(db.BLOB(70), default='default.jpg')
    createTime = db.Column(db.DateTime)


class CommentVO(db.Model):
    __tablename__ = 'comment'  # 起表名
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    content = db.Column(db.String(150), default='123456')
    createTime = db.Column(db.DateTime)
