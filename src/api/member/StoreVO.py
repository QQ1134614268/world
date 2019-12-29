from sqlalchemy import Column, String, Integer

from vo.BaseModel import BaseTable


# 商户
class StoreVO(BaseTable):
    __tablename__ = 'store_t'
    name = Column(String(256), index=True)
    password = Column(String(128), default='123456')
    store_name = Column(Integer, index=True)
    phone = Column(String(11), index=True)
