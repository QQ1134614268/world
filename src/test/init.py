"""
@author:huangran
"""

import json
import unittest

from src.main.python.app import app
from src.test.BuildData import create_data


class InitTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_register(self):
        data = {
            "email": create_data("string", 10),
            "password": "123456",
            "username": "root"
        }
        url = '/user/register'
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json')

        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')

    def test_register1(self):
        data = {
            "email": create_data("string", 10),
            "password": "123456",
            "username": "test"
        }
        url = '/user/register'
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json')

        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')

    def test_register2(self):
        data = {
            "email": create_data("string", 10),
            "password": "123456",
            "username": "zero"
        }
        url = '/user/register'
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json')

        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')
    def test_register3(self):
        data = {
            "email": create_data("string", 10),
            "password": "123456",
            "username": "wg"
        }
        url = '/user/register'
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json')

        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')
if __name__ == '__main__':
    unittest.main()
