# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/27 22:11
"""

from sqlalchemy import Column, String, Integer

from vo.BaseModel import BaseTable


class UserCloudSpaceVO(BaseTable):
    __tablename__ = 'user_cloud_space'
    user_id = Column(Integer)
    file_name = Column(String(150), default='xxx.txt')
    file_path = Column(String(150), default='/xxx/xxx.txt')
