# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, String, Integer, Float

from config.enum_conf import StoreMemberType, OrderStatus
from util.dev_util import get_comment
from util.password_util import get_sha256_salt_password
from vo.table_model import BaseTable


class StoreVO(BaseTable):
    __tablename__ = 'store_t'
    name = Column(String(256), index=True)
    store_name = Column(Integer, index=True)
    phone = Column(String(11), index=True)
    user_id = Column(Integer, index=True)

    _password = Column('password', String(255), nullable=False)

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
    user_type = Column(String(256), index=True, default=StoreMemberType.NormalVip.name,
                       comment=get_comment(StoreMemberType))  # todo 客户, 店员(后厨,店长,管理员, 普通店员)


class WalletVO(BaseTable):
    __tablename__ = 'wallet_t'
    user_id = Column(Integer)
    store_id = Column(Integer, index=True)
    money = Column(Float(precision="14,2"), comment="余额", default=0)


class GoodsVO(BaseTable):
    __tablename__ = 'goods_t'
    name = Column(String(256))
    price = Column(Float(precision="14,2"), nullable=False, comment="价格")  # todo
    duration = Column(Float(precision="14,2"), comment="折扣?")
    describe = Column(String(256), comment="介绍")
    images = Column(String(256))
    store_id = Column(Integer, index=True)
    label = Column(String(256), comment="分类")  # todo 树节点 详情:颜色,材料,气味等 用户自定义


class OrderVO(BaseTable):
    __tablename__ = 'order_t'
    order_code = Column(String(256), index=True, comment="订单编号")  # 单一后台?  平台
    store_id = Column(Integer, index=True)  # 单一后台?  平台
    goods_id = Column(Integer, index=True)
    goods_name = Column(String(256), index=True)
    user_id = Column(Integer, index=True)
    num = Column(Integer)
    status = Column(String(255), default=OrderStatus.UN_PAYMENT.name, comment=get_comment(OrderStatus))  # 状态
    total_price = Column(Float(precision="14,2"), comment="价格(每个)")  # todo price 仅扣费时
    # info = Column(String(256), comment="详情,size,冷热, ")  # todo 详情:颜色,材料,气味等
    table_id = Column(String(255), comment="下单桌号")
