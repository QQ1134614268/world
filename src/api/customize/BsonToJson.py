# import datetime
# import json
#
# from mongoengine.base import BaseDocument
#
# # 使json能够转化datetime对象
# class DateEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             retu
#             rn obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, datetime.date):
#             return obj.strftime("%Y-%m-%d")
#         else:
#             return json.JSONEncoder.default(self, obj)
#
#
# # 将 MongoDB 的 document转化为json形式
# def convertMongoToJson(o):
#     def convert(dic_data):
#         # 对于引用的Id和该条数据的Id，这里都是ObjectId类型的
#         from bson import ObjectId
#         # 字典遍历
#         for key, value in dic_data.items():
#             # 如果是列表，则递归将值清洗
#             if isinstance(value, list):
#                 for l in value:
#                     convert(l)
#             else:
#                 if isinstance(value, ObjectId):
#                     dic_data[key] = str(dic_data.pop(key))
#         return dic_data
#
#     ret = {}
#     # 判断其是否为Document
#     if isinstance(o, BaseDocument):
#         """
#         转化为son形式，son的说明，摘自官方
#         SON data.
#         A subclass of dict that maintains ordering of keys and provides a
#         few extra niceties for dealing with SON. SON provides an API
#         similar to collections.OrderedDict from Python 2.7+.
#         """
#         data = o.to_mongo()
#         # 转化为字典
#         data = data.to_dict()
#         ret = convert(data)
#     # 将数据转化为json格式， 因json不能直接处理datetime类型的数据，故需要区分处理
#     ret = json.dumps(ret, cls=DateEncoder)
#     return ret