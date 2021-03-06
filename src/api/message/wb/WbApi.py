from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal

from api.message.wb.BlogVO import BlogVO, BlogCommentVO
from db.db import db
from api.user import UserService
from util import ResUtil

wb_api = Blueprint("wb_api", __name__, url_prefix='/api/wb_api')


@wb_api.route('/add_blog', methods=['POST'])
def add_blog():
    """
    发表博客
    ---
    tags:
      - wb_api
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          发表博客
        required: true
        schema:
          id: blog
          required:
            - content
          properties:
            content:
              description: 内容
              type: string
              example: 天气晴
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    content = data.get('content', '')
    user_id = UserService.get_id_by_token()
    vo = BlogVO(content=content, user_id=user_id)
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("发表成功"))


@wb_api.route('/add_comment', methods=['POST'])
def add_comment():
    """
    发表博客
    ---
    tags:
      - wb_api
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          发表博客
        required: true
        schema:
          id: comment
          required:
            - content
            - blog_id
          properties:
            comment:
              description: 评论
              type: string
              example: 天气晴
            blog_id:
              description: 评论博客id
              type: integer
              example: 1
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    comment = data.get('comment', '')
    blog_id = data.get('blog_id', '')
    user_id = UserService.get_id_by_token()
    print(user_id)
    vo = BlogCommentVO(comment=comment, blog_id=blog_id, user_id=user_id)
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("评论成功"))


blog_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'content': fields.String,
    'up_files': fields.String,
    'comments': {
        "comment": fields.String
    }
}


@wb_api.route('/get_user_blog_by_page', methods=['GET'])
def get_user_blog():
    """
    获取用户的博客
    ---
    tags:
      - wb_api
    responses:
      500:
        description: server error
      200:
        description: success
    """

    data = request.get_json()
    user_id = data.get('user_id', '')
    page_index = data.get('page_index', 0)
    page_size = data.get('page_size', 10)
    vo = BlogVO.query.fielt(user_id=user_id).order_by(BlogVO.create_time).paginate(int(page_index), int(page_size),
                                                                                   False)
    db.session.add(vo)
    db.session.commit()
    blog_list = [marshal(vo, blog_fields) for vo in blog_fields]
    return jsonify(ResUtil.success(blog_list))
