# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""

from sqlalchemy import Column, Integer, String, Float, Enum, Text

from config.enum_conf import ReviewEnum
from service.user_service import get_id_by_token
from util.dev_util import get_comment
from vo.table_model import BaseTable


class InvitationCodeVO(BaseTable):
    __tablename__ = 'invitation_code_t'
    user_id = Column(Integer, comment='用户id')
    code = Column(String(255), comment='邀请码')
    invitation_user_id = Column(Integer, comment='邀请id')


class WorksVO(BaseTable):
    __tablename__ = 'works_t'
    user_id = Column(Integer, index=True, comment='用户id')
    describe = Column(String(255), comment='描述介绍')
    file = Column(String(255), comment='视频path')
    start = Column(Integer, default=0, comment='点赞数')
    thumbnail = Column(String(128), comment='封面图片path')
    state = Column(Enum(ReviewEnum), default=ReviewEnum.NONE.name, comment=get_comment(ReviewEnum))


class TargetVO(BaseTable):
    __tablename__ = 'target_t'
    user_id = Column(Integer, index=True, default=get_id_by_token, comment='用户 id')
    title = Column(String(255), comment='标题')
    content = Column(Text, comment='内容')
    price = Column(Float(precision="14,2"), comment="价格")
    state = Column(Enum(ReviewEnum), default=ReviewEnum.NONE.name, comment=get_comment(ReviewEnum))
