# -*- coding:utf-8 -*-
"""
@Time: 2021/2/3
@Description: 
"""
import os

root_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src")
os.chdir(root_dir)
py_path = os.path.join(os.path.dirname(root_dir), "venv/Scripts/flask")
order2 = "{} {}".format(py_path, "db upgrade")
os.system(order2)
