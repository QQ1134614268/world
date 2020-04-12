# -*- coding:utf-8 -*-
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String

from vo.BaseModel import BaseTable


class Attention(BaseTable):
    __tablename__ = 'attention_t'
    userId = Column(Integer, ForeignKey('user.id'), index=True)
    attentionUserId = Column(Integer, index=True)
    # cate = db.Column(db.Enum(
    #     '最爱', '风景', '人物', '动物', '游记', '卡通', '生活', '其他'
    # ), server_default='最爱', nullable=False)
    group = Column(String(150), index=True)
