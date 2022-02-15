from flask import Blueprint, request

import service.user_service
from config.mongodb import mongoDB
from util import res_util

customize_api = Blueprint("customize_api", __name__, url_prefix='/api/customize_api')


@customize_api.route('/addModel', methods=['POST'])
def add_model():
    """
    {
        # path: /userId/菜品 # 有mongo提供 _id 做标识
        "name": "小葱拌豆腐",
        "image": "/userId/小葱拌豆腐.jpg",
        "price": 10,
        "unit": "$",
        "peiliao": "小葱,豆腐",
        "benefit": 0.8,
        "assess": ["很好吃","很多"],

        userId: 1,

        # create_time= ""
        # update_time=""
        # "_id"=
    }
    :return:
    """
    data = request.get_json()
    data["userId"] = service.user_service.get_id_by_token()
    collection = mongoDB.models
    collection.insert_one(data)
    return res_util.success()


@customize_api.route('/getModel', methods=['POST'])
def get_model():
    collection = mongoDB.models
    res = list(collection.find({
        "userId": service.user_service.get_id_by_token()
    }))
    for i in res:
        i["_id"] = str(i["_id"])
    return res_util.success(res)


@customize_api.route('/model_eval', methods=['POST'])
def model_eval():
    """
    TODO 或者客户端计算,服务端保存计算方法
    用户输入模型,进行计算 +-*/ ()
    :return:
    """
    pass
    return res_util.success("model_eval")
