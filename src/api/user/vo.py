# -*- coding:utf-8 -*-
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from config.mysql_db import BaseTable


# from vo.UserVO import UserVO
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
