import json
import unittest

from app import app


class WbApiTest(unittest.TestCase):
    """ """

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_add_blog(self):
        url = "/wb_api/add_blog"
        data = {
            "content": "天气晴",
        }
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json',
                                          headers={
                                              "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoicm9vdCIsImlkIjoxLCJ0aW1lc3RhbXAiOjE1NzcxMTc1NDJ9.-FKeKaMO9RIyAramv5HgGHAxxVfOEIiBSvpcSLfRp_w"})
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')

    def test_add_comment(self):
        url = "/wb_api/add_comment"
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidGVzdCIsImlkIjozLCJ0aW1lc3RhbXAiOjE1NzcxMjI1MjJ9.KuC6nIgkUoxtqJXYuOOm8vtGYgRvzwynE0QvL0eZ83Y"
        data = {
            "comment": "水天一线",
            "blog_id": 1,
        }
        response = app.test_client().post(url, data=json.dumps(data), content_type='application/json',
                                          headers={"token": token})
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 1, '有异常')


if __name__ == '__main__':
    unittest.main()
