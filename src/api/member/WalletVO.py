from sqlalchemy import Column, Integer, Float

from vo.BaseModel import BaseTable


class WalletVO(BaseTable):
    __tablename__ = 'wallet_t'
    userId = Column(Integer)
    amount = Column(Float, default=0)
