# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 16:42
# @Author  : huangran
"""
# !/usr/bin/env python
# https://www.cnblogs.com/caicairui/p/7821586.html
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# 主文件中导入app初始化manage
from app import app
# db = SQLAlchemy()
# 导入需要迁移的数据库模型
from db.db import db
# from vo.user import UserVO, AnnouncementVO, RecordVO, MessageVO, CommentVO
# from api.area.AreaVO import AreaVO, AreaMemberRelationVO
# from api.organization.OrganizationVO import OrganizationVO,OrganizationMemberRelationVO


# 让python支持命令行工作
manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


# D:/dev/python3.7/python.exe manage.py db init
# D:/dev/python3.7/python.exe manage.py db migrate
# D:/dev/python3.7/python.exe E:/python/world/src/main/python/vo/user.py db upgrade
if __name__ == '__main__':
    manager.run()

