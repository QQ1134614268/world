# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer
from sqlalchemy import Float
from sqlalchemy import JSON

from config.mysql_db import BaseTable


class ExistVO(BaseTable):
    __tablename__ = 'exist_t'
    path = Column(String(255))
    name = Column(String(255))
    data = Column(JSON)
    # userId = Column(Integer)
    # amount = Column(Float, default=0)


# 商户
class StoreVO(BaseTable):
    __tablename__ = 'store_t'
    name = Column(String(256), index=True)
    password = Column(String(128), default='123456')
    store_name = Column(Integer, index=True)
    phone = Column(String(11), index=True)
    user_id = Column(Integer, index=True)


class StoreMemberTable(BaseTable):
    __tablename__ = 'store_member_t'
    store_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)


class WalletVO(BaseTable):
    __tablename__ = 'wallet_t'
    user_id = Column(Integer)
    store_id = Column(Integer, index=True)
    money = Column(Float, default=0)
