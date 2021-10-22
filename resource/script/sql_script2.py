# -*- coding:utf-8 -*-
"""
@Time: 2021/2/3
@Description: 
"""
import os

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
os.chdir(root_dir)
py_path = os.path.join(os.path.dirname(root_dir), "venv/Scripts/python.exe")
file_path = os.path.join(root_dir, "manage.py")
order2 = "{} {} {}".format(py_path, file_path, "db upgrade")
os.system(order2)
