"""
@author:huangran
"""

from db.db import db
#创建User模型
class UserVO(db.Model):
    __tablename__ = 'user' #起表名
    id = db.Column(db.Integer,primary_key=True) #主键
    username = db.Column(db.String(12),index=True)
    password = db.Column(db.String(128),default='123456')
    birthday = db.Column(db.Date)
    sex = db.Column(db.Boolean,default=True)
    email = db.Column(db.String(60),default='793390457@qq.com')
    icon = db.Column(db.String(70),default='default.jpg')

    phone=db.Column(db.String(11))
    active = db.Column(db.Boolean, default=True)
    # sign ....

    def __str__(self):
        return self.username

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Users(id='%s')" % self.id

    # def set_password(self, password):
    #     return generate_password_hash(password)
    #
    # def check_password(self, hash, password):
    #     return check_password_hash(hash, password)

    # def get(self, id):
    #     return self.query.filter_by(id=id).first()
    #
    # def add(self, user):
    #     db.session.add(user)
    #     return session_commit()
    #
    # def update(self):
    #     return session_commit()
    #
    # def delete(self, id):
    #     self.query.filter_by(id=id).delete()
    #     return session_commit()