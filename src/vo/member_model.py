# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, String, Integer, Float

from config.mysql_db import db
from util.password_util import get_sha256_salt_password
from vo.table_model import BaseTable


class StoreVO(BaseTable):
    __tablename__ = 'store_t'
    name = Column(String(256), index=True)
    store_name = Column(Integer, index=True)
    phone = Column(String(11), index=True)
    user_id = Column(Integer, index=True)

    _password = db.Column('password', db.String(255), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = get_sha256_salt_password(value)

    def check_password(self, user_pwd):
        if user_pwd is not None and self._password == get_sha256_salt_password(user_pwd):
            return True
        return False


class StoreMemberTable(BaseTable):
    __tablename__ = 'store_member_t'
    store_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)


class WalletVO(BaseTable):
    __tablename__ = 'wallet_t'
    user_id = Column(Integer)
    store_id = Column(Integer, index=True)
    money = Column(Float, default=0)


class GoodsVO(BaseTable):
    __tablename__ = 'goods_t'
    name = Column(String(256), default='123456')
    price = Column(Float)
    duration = Column(Float, default='123456')
    describe = Column(String(256), default='123456')
    images = Column(String(256), default='123456')
    store_id = Column(Integer, index=True)


class OrderVO(BaseTable):
    __tablename__ = 'order_t'
    goods_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    num = Column(Integer)