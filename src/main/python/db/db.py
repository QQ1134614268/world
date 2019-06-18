"""
@author:huangran
"""
# 导包
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化对象
app = Flask(__name__)

# 添加配置
class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://127.0.0.1:3306/theword"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # 会打印原生sql语句，便于观察

app.config.from_object(Config)

# 将数据库与对象连接
db = SQLAlchemy(app)

# 定义一个角色类
# 假设一人只能分饰一个角色，但是一个角色可以是多人，所以role是一对多的一
# 在一的一方用relationship来定义这种一对多的关系
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    # backref 固定写法，表示的是反推
    # 第一个参数表示要关联的类的模型
    # 第二个参数表示新增加的一个属性，属性的名字随意取
    us = db.relationship("User", backref="role")

    def __repr__(self):
        return "Role = %s" % self.name


class User(db.Model):

    # users表示表名，名称自定义
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(128))
    email = db.Column(db.String(128))
    # ForeignKey 在多的一方定义外键
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    #repr()方法显示一个可读字符串
    def __repr__(self):
        return "User = %s" % self.name



