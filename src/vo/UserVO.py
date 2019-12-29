# -- coding:UTF-8 --
from sqlalchemy import Column, String, Integer, Date, Boolean, BLOB

from vo.BaseModel import BaseTable


# 创建User模型
class UserVO(BaseTable):
    __tablename__ = 'user'
    username = Column(String(12), index=True)
    password = Column(String(128), default='123456')
    birthday = Column(Date)
    sex = Column(Boolean, default=True)
    email = Column(String(60), default='793390457@qq.com')
    icon = Column(BLOB(300), default=b'default.jpg')

    phone = Column(String(11))
    active = Column(Boolean, default=True)

    def __str__(self):
        return "Users(id='%s')" % self.id


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
