import unittest

from app import app
from config.mysql_db import db
from vo.member_model import GoodsVO
from vo.table_model import UserVO, EnumConfig


class InitDbTest(unittest.TestCase):
    """ """

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_enum(self):
        with app.app_context():
            data = {
                "BAIDU_NET_ADDRESS": "https://www.baidu.com",
                "QQ_NET_ADDRESS": "https://www.qq.com",
            }
            for key, value in data.items():
                vo = EnumConfig(code=key, value=value, group_code="CONFIG_TYPE")
                db.session.add(vo)

            group_codes = {
                "FOOD_TYPE": "FOOD_TYPE",
                "COLOR_TYPE": "COLOR_TYPE",
                "GROUP_CODE_TYPE": "GROUP_CODE_TYPE"
            }

            for key, value in group_codes.items():
                vo = EnumConfig(code=key, value=value, group_code="GROUP_CODE_TYPE")
                db.session.add(vo)

            review_enum = {
                "1": "通过",
                "2": "未通过",
                "3": "待审核",
                "4": "待评审",
            }
            for key, value in review_enum.items():
                vo = EnumConfig(value=key, label=value, group_code="REVIEW_ENUM")
                db.session.add(vo)
            db.session.commit()

    def test_config(self):
        with app.app_context():
            food_types = ["主食", "小炒", "饮料"]
            for s in food_types:
                vo = EnumConfig(value=s, group_code="FOOD_TYPE")
                db.session.add(vo)
            db.session.commit()

    def test_food(self):
        with app.app_context():
            food_types = db.session.query(EnumConfig).filter(EnumConfig.group_code == "FOOD_TYPE").all()
            for s in food_types:
                for i in range(4):
                    vo = GoodsVO(name=f'{s.value}-{i}', price=i, describe="本店必选,热卖", images="", type=s.id)
                db.session.add(vo)
            db.session.commit()

    def test_user(self):
        ...
        vo = UserVO()
        db.session.add(vo)


if __name__ == '__main__':
    unittest.main()

# def sqlalchemy_context(app):
#     def add_context(func):
#         @wraps(func)
#         def do_job(*args, **kwargs):
#             app.app_context().push()
#             result = func(*args, **kwargs)
#             return result
#
#         return do_job
#
#     return add_context
#
#
# @sqlalchemy_context(app)
# def init_primary_key():
#     Model.query.filter_by()
