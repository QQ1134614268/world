from flask import Blueprint, jsonify, request

from db.mongodb import db
from service import UserService
from util import ResUtil

customize_api = Blueprint("customize_api", __name__, url_prefix='/customize_api')


@customize_api.route('/addModel', methods=['POST'])
def addModel():
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
    data["userId"] = UserService.get_id_by_token()
    collection = db.models
    collection.insert_one(data)
    return jsonify(ResUtil.success("success"))


@customize_api.route('/getModel', methods=['POST'])
def getModel():
    collection = db.models
    res = list(collection.find({"userId": UserService.get_id_by_token()}))
    for i in res:
        i["_id"] = str(i["_id"])
    return jsonify(ResUtil.success(res))


@customize_api.route('/model_eval', methods=['POST'])
def model_eval():
    """
    TODO 或者客户端计算,服务端保存计算方法
    用户输入模型,进行计算 +-*/ ()
    :return:
    """
    pass
    return jsonify(ResUtil.success("model_eval"))
