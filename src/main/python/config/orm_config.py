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


@app.route("/")
def index():
    db.Query.first()
    all=db.Query.all()
    print(all,000)
    for i in all:
        print(i)
    return "index page222"
class Time(db.Model):

    # users表示表名，名称自定义
    __tablename__ = "time"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    time = db.DateTime(db.String(128))
    def __repr__(self):
        return "User = %s" % self.name

if __name__ == '__main__':
    # 创建表
    db.create_all()
    ro1 = Role(name="admin")

    # 插入一条数据
    db.session.add(ro1)
    db.session.commit()

    ro2 = Role(name="user")
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com',
               password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com',
               password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com',
               password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com',
               password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com',
               password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com',
               password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com',
               password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com',
               password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com',
               password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com',
                password='235523', role_id=ro2.id)

    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()  # 必须提交，数据才能生效
    app.run()



