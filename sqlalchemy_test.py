# -*- coding:utf-8 -*-
"""
@Time: 2020/9/12
@Description: 
"""
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://wg:123456@localhost:3306/test')
Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    username = Column(String(20))


User.query.all()
vo = session.query(User).filter(User.id == 1).first()
print(vo.id)
