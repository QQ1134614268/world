import json
import unittest

from app import app


class HelloTest(unittest.TestCase):
    """为hello_api逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_hello(self):
        """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
        response = app.test_client().get('/api/hello_api/hello', data={})
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')
        # self.assertIn('errcode', json_dict, '数据格式返回错误')

    # def test_error_username_password(self):
    #     """测试用户名和密码错误的情况[当登录名和密码错误的时候，返回 errcode = -1]"""
    #     response = app.test_client().post('/login', data={"username": "aaaaa", "password": "12343"})
    #     json_data = response.data
    #     json_dict = json.loads(json_data)
    #     self.assertIn('errcode', json_dict, '数据格式返回错误')
    #     self.assertEqual(json_dict['errcode'], -1, '状态码返回错误')


if __name__ == '__main__':
    unittest.main()
