# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import Column, String, Integer, Float, JSON

from config.enum_conf import StoreMemberType, OrderStatus
from config.env_default import world_env
from util import encrypt_util
from util.dev_util import get_comment
from vo.table_model import BaseTable


class GoodsVO(BaseTable):
    __tablename__ = 'goods_t'
    type_id = Column(String(256), comment="分类")
    name = Column(String(256), comment="商品名")
    price = Column(Float(precision="14,2"), nullable=False, comment="价格")
    duration = Column(Float(precision="14,2"), comment="折扣?")
    describe = Column(String(256), comment="介绍")
    image = Column(String(256))
    store_id = Column(Integer, index=True)


class OrderVO(BaseTable):
    __tablename__ = 'order_t'
    user_id = Column(Integer, index=True, comment="用户id")
    store_id = Column(Integer, index=True, comment="店铺id")
    total_price = Column(Float(precision="14,2"), comment="总价")
    status = Column(String(255), default=OrderStatus.UN_PAYMENT.name, comment=get_comment(OrderStatus))  # 状态
    order_code = Column(String(256), index=True, comment="订单编号")  # 单一后台?  平台
    table_id = Column(String(255), comment="下单桌号")
    info_list = []


class OrderInfoVO(BaseTable):
    __tablename__ = 'order_info_t'
    order_id = Column(Integer, index=True, comment="订单id")  # 单一后台?  平台
    goods_id = Column(Integer, index=True, comment="商品id")
    image = Column(String(256), comment="商品图片path")
    name = Column(String(256), comment="商品名")
    describe = Column(String(256), comment="介绍")
    num = Column(Integer, comment="数量")
    price = Column(Float(precision="14,2"), comment="价格(每个)")
    cooker_status = Column(String(256), comment="是否做完菜")


class StoreVO(BaseTable):
    __tablename__ = 'store_t'
    name = Column(String(256), index=True, comment="姓名")
    store_name = Column(Integer, index=True, comment="店铺名")
    phone = Column(String(11), index=True, comment="手机号")
    user_id = Column(Integer, index=True, comment="用户id")

    _password = Column('password', String(255), nullable=False, comment="密码hash")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = encrypt_util.SHA256Util.sha256_salt(value, world_env.public_key)

    def check_password(self, pwd):
        if pwd is not None and self._password == encrypt_util.SHA256Util.sha256_salt(pwd, world_env.public_key):
            return True
        return False


class StoreMemberTable(BaseTable):
    __tablename__ = 'store_member_t'
    store_id = Column(Integer, index=True, comment="店铺id")
    user_id = Column(Integer, index=True, comment="用户id")
    user_type = Column(String(256), index=True, default=StoreMemberType.NormalVip.name,
                       comment=get_comment(StoreMemberType))


class WalletVO(BaseTable):
    __tablename__ = 'wallet_t'
    user_id = Column(Integer, comment="用户id")
    store_id = Column(Integer, index=True, comment="店铺id")
    money = Column(Float(precision="14,2"), comment="余额", default=0)


class QrCodeVO(BaseTable):
    __tablename__ = 'qr_code_t'
    url_dic = Column(JSON, comment="url参数")
    url = Column(String(255), comment="网址")
    img_path = Column(String(255), comment="二维码中间头像")
    img_width = Column(String(255), comment="二维码中间头像的宽度")
    img_height = Column(String(255), comment="二维码中间头像的高度")
