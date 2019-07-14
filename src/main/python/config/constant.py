"""
@author:huangran
"""

# from flask import Flask, Response, jsonify
#
# class MyResponse(Response):
#     @classmethod
#     def force_type(cls, response, environ=None):
#         if isinstance(response, (list, dict)):
#             response = jsonify(response)
#         return super(Response, cls).force_type(response, environ)
#
# app = Flask(__name__)
# app.response_class = MyResponse
#
# @app.route('/')
# def root():
#     t = {
#         'a': 1,
#         'b': 2,
#         'c': [3, 4, 5]
#     }
#     return t
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run()