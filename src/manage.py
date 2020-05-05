# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 16:42

"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from db.db import db

# 主文件中导入app初始化manage
# db = SQLAlchemy()
# 导入需要迁移的数据库模型
# 让python支持命令行工作
manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

# 建表类导入到这里或者 在app中有引用
# from vo import XX
'''

E:/python/world/venv/Scripts/python.exe manage.py db init
E:/python/world/venv/Scripts/python.exe manage.py db migrate
E:/python/world/venv/Scripts/python.exe manage.py db upgrade

'''
#
if __name__ == '__main__':
    manager.run()
