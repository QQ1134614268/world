
from sqlalchemy import Column, String, Integer

from vo.BaseModel import BaseTable


class WalletVO(BaseTable):
    __tablename__ = 'wallet_t'
    userId = Column(String(70), default='default.jpg')
    amount = Column(Integer, default=0)
