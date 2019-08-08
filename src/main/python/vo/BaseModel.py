# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/6 18:50
# @Author  : huangran
"""
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from db.db import db
from util.DateUtils import get_utc_now
from sqlalchemy import Sequence
from sqlalchemy import Table      # 使用Table专门生成第三方表模型
from sqlalchemy.orm import relationship

class BaseTable(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=get_utc_now())
    status = Column(Integer)


class UserTest(BaseTable):
    __tablename__ = 'user_test'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))


# 第三方表--附属部门

# 简单来说, relationship函数是sqlalchemy对关系之间提供的一种便利的调用方式, relationship的返回值赋给的变量名为正向调用的属性名，绑定给当前表模型类中，而backref参数则是指定反向调用的属性名，绑定给关联的表模型类中，如下部门表中Department.staffs就为正向，Staff.main_dep就为反向。

# aux_dep_table = Table('staff_aux_dep', BaseModel.metadata,
#         Column('id', Integer(), primary_key=True, autoincrement=True),
#         Column('dep_id', Integer(), ForeignKey('dep.id', ondelete='CASCADE')),
#         Column('staff_id', Integer(), ForeignKey('staff.id', ondelete='CASCADE'))
# )

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')  # 关联数据库
# DBSession = sessionmaker(engine)                  # 创建DBSession类
# session = DBSession()                               # 创建session对象
#
# BaseModel.metadata.create_all(engine)         　# 数据库生成表
