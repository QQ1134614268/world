from sqlalchemy import Column, String, Integer

from vo.BaseModel import BaseTable


# 创建User模型
class MemberUserVO(BaseTable):
    __tablename__ = 'member_user_t'
    store_id = Column(Integer, index=True)
    phone = Column(String(11), index=True)
    password = Column(String(128), default='123456')

    name = Column(String(256), index=True)
