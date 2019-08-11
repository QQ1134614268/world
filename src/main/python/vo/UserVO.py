# -- coding:UTF-8 --
"""
@author:huangran
"""
import json

from sqlalchemy import Column, String, Integer, Date, Boolean, BLOB

from vo.BaseModel import BaseTable


# 创建User模型
class UserVO(BaseTable):
    __tablename__ = 'user'  # 起表名
    username = Column(String(12), index=True)
    password = Column(String(128), default='123456')
    birthday = Column(Date)
    sex = Column(Boolean, default=True)
    email = Column(String(60), default='793390457@qq.com')
    icon = Column(BLOB(300), default=b'default.jpg')

    phone = Column(String(11))
    active = Column(Boolean, default=True)

    # sign ....

    def __str__(self):
        return self.username

    # def __init__(self, username, password, email):
    #     self.username = username
    #     self.password = password
    #     self.email = email

    @staticmethod
    def get_password(password):
        return password

    def __str__(self):
        return "Users(id='%s')" % self.id


class AnnouncementVO(BaseTable):
    __tablename__ = 'announcement'  # 起表名
    userid = Column(Integer, index=True)
    title = Column(String(128), index=True)
    content = Column(String(150), default='123456')
    images = Column(String(70), default='/')


class MessageVO(BaseTable):
    __tablename__ = 'message'  # 起表名
    content = Column(String(150), default='123456')
    image = Column(String(70), default='default.jpg')
    announcement_id = Column(Integer)


# class InnerVO(BaseTable):
#     inner = Column(String(150), default='123456')
#
#
# class ComplexVO(BaseTable):
#     __tablename__ = 'complex'  # 起表名
#     content = Column(String(150), default='123456')
#     images = Column(String(70), default='default.jpg')


class RecordVO(BaseTable):
    __tablename__ = 'record'  # 起表名
    user_id = Column(Integer)
    content = Column(String(150), default='123456')
    image = Column(String(70), default='default.jpg')
    video = Column(String(70), default='default.jpg')


class CommentVO(BaseTable):
    __tablename__ = 'comment'  # 起表名
    record_id = Column(String(150), default='123456')
    content = Column(String(150), default='123456')


class TestVO:
    id = 0
    content = 1


if __name__ == '__main__':
    u = TestVO()
    u.content = 1
    u2 = TestVO()
    u2.content = 1
    u.id = u2
    print(json.dumps(u, default=lambda obj: obj.__dict__))
