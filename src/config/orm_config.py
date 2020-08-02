# -*- coding:utf-8 -*-
"""
@Time: 2020/8/2
@Description: 
"""
from flask_restful import fields

from config.conf import DATE_TIME_FORMAT


class DateTime(fields.DateTime):
    def __init__(self, dt_format=DATE_TIME_FORMAT, **kwargs):
        super(DateTime, self).__init__(**kwargs)
        self.dt_format = dt_format

    def format(self, value):
        return value.strftime(DATE_TIME_FORMAT)
