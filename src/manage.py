# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/3 16:42

E:/python/world/venv/Scripts/python.exe manage.py db init
E:/python/world/venv/Scripts/python.exe manage.py db migrate
E:/python/world/venv/Scripts/python.exe manage.py db upgrade

"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from config.mysql_db import db

manager = Manager(app)
# 使用migrate绑定app和db
migrate = Migrate(app, db)
# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

# 建表类导入到这里或者 在app中有引用
# from vo import XX
if __name__ == '__main__':
    manager.run()
