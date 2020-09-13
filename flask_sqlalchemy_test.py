# -*- coding:utf-8 -*-
"""
@Time: 2020/9/12
@Description: 
"""

import datetime

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, Integer, Enum, ForeignKey, UniqueConstraint, Float
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.orm import relationship

app = Flask(__name__)
api = Api(app)
# 跨域
CORS(app, supports_credentials=True)
DEBUG = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://wg:123456@localhost:3306/world'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = DEBUG
app.config["DEBUG"] = DEBUG
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
db = SQLAlchemy(app=app)


class BaseTable(db.Model):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class WorkerVO(BaseTable):
    __tablename__ = 'worker_t'
    belong = Column(Integer)
    name = Column(String(255))
    birthday = Column(DateTime)
    id_card_number = Column(String(255), unique=True)
    sex = Column(Enum('男', '女'))
    pay = Column(String(255))
    start_time = Column(DateTime)
    phone = Column(String(11))


class ProjectConfig(BaseTable):
    __tablename__ = 'project_config'
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))


class WorkerTimeVO(BaseTable):
    __tablename__ = 'worker_time_t'
    worker_id = Column(Integer, ForeignKey(WorkerVO.id, ondelete='CASCADE'), index=True)
    morning = Column(Float, default=0)
    noon = Column(Float, default=0)
    afternoon = Column(Float, default=0)
    night = Column(Float, default=0)
    hours = Column(Float)
    date = Column(DateTime)
    worker = relationship(WorkerVO, backref='time', foreign_keys=[worker_id])
    __table_args__ = (
        UniqueConstraint('worker_id', 'date'),
    )


if __name__ == '__main__':
    # vos = ProjectConfig.query.all()
    # print(list(vos))

    # db.session.add(ProjectConfig(name="name1"))
    # db.session.commit()

    # sql = insert(ProjectConfig).values(id=3, name='zs').on_duplicate_key_update(name='zs')
    # db.session.execute(sql)
    # db.session.commit()
    data = {"type": "上午", "date": "2020-09-13", "worker_ids": [1]}
    en = {
        "上午": {"morning": 4.5},
        "下午": {"morning": 4.5},
    }
    for i in data["worker_ids"]:
        sql = insert(WorkerTimeVO).values(worker_id=i, **en[data.get("type")],
                                          date=data["date"]).on_duplicate_key_update(
            **en[data.get("type")])
        db.session.execute(sql)
        db.session.commit()

    # insert().on_duplicate_key_update(
    #     [("name", "some name"), ("value", "some value")])
    #
    #
    # insert_stmt = insert(ProjectConfig).values(id='some_existing_id', data='inserted value')
    #
    # on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    #     data=insert_stmt.inserted.data,
    #     status='U'
    # )
    #
    # db.session.execute(on_duplicate_key_stmt)
