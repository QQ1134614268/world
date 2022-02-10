import json
import unittest

from app import app
from util.dev_util import create_data


class UserApiTest(unittest.TestCase):
    """为 user_api 逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_register(self):
        data = {
            "username": create_data("string", 10),
            "password": create_data("string", 10),
            "email": create_data("string", 10)
        }
        url = '/user/register'
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json')
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')

    def test_get_verify_code(self):
        url = "/user/get_verify_code"
        response = app.test_client().get(url, data={})
        json_data = response.data
        self.assertNotEqual(json_data, None, '有异常')

    def test_login(self):
        url = "/user/login"
        data = {
            "code": "zero",
            "password": "123456",
            "username": "root"
        }
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json')
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')


if __name__ == '__main__':
    unittest.main()
