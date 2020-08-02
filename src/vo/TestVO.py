from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, Integer

from config.mysql_db import BaseTable


# 一对多
class Test_Parent_1_to_N_VO(BaseTable):
    __tablename__ = 'test_parent_1_to_n_t'
    name = Column(String(64), nullable=False)
    full_name = Column(String(64))
    children = relationship("Test_Child_1_to_N_VO", backref="test_parent_1_to_n_t")
    # 默认返回的是列表，collection_class=set 加他返回的是集合，
    # collection_class=attribute_mapped_collection('name') 返回的是name 字典 值从属性中取
    # collection_class=mapped_collection(lambda children: children.name.lower() 这个可以自定义值
    # 在父表类中通过 relationship() 方法来引用子表的类集合


class Test_Child_1_to_N_VO(BaseTable):  # 多
    __tablename__ = 'test_child_1_to_n_t'
    name = Column(String(64), nullable=False)
    full_name = Column(String(64))
    parent_id = Column(Integer, ForeignKey('test_parent_1_to_n_t.id'))
    # 在子表类中通过 foreign key (外键)引用父表的参考字段


class Test_Parent_N_N_VO(BaseTable):
    __tablename__ = 'test_parent_n_n_t'
    name = Column(String(64), nullable=False, index=True)
    full_name = Column(String(64))
    children = relationship("Test_Child_N_N_VO", secondary=lambda: association_table, backref="parents")


class Test_Child_N_N_VO(BaseTable):
    __tablename__ = 'test_child_n_n_t'
    name = Column(String(64), nullable=False, index=True)
    full_name = Column(String(64))


# 多对多
association_table = Table('association_n_n_t', BaseTable.metadata,
                          Column('test_parent_n_n_t_id', Integer, ForeignKey('test_parent_n_n_t.id')),
                          Column('test_child_n_n_t_id', Integer, ForeignKey('test_child_n_n_t.id')))
