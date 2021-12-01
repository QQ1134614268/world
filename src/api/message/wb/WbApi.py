from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal

import service.token_service
from config.mysql_db import db
from util import res_util
from vo.table_model import BlogVO, BlogCommentVO

wb_api = Blueprint("wb_api", __name__, url_prefix='/api/wb_api')


@wb_api.route('/add_blog', methods=['POST'])
def add_blog():
    data = request.get_json()
    content = data.get('content', '')
    user_id = service.token_service.get_id_by_token()
    vo = BlogVO(content=content, user_id=user_id)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("发表成功"))


@wb_api.route('/add_comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = data.get('comment', '')
    blog_id = data.get('blog_id', '')
    user_id = service.token_service.get_id_by_token()
    print(user_id)
    vo = BlogCommentVO(comment=comment, blog_id=blog_id, user_id=user_id)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("评论成功"))


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
    data = request.get_json()
    user_id = data.get('user_id', '')
    page_index = data.get('page_index', 0)
    page_size = data.get('page_size', 10)
    vo = BlogVO.query.fielt(user_id=user_id).order_by(BlogVO.create_time).paginate(int(page_index), int(page_size),
                                                                                   False)
    db.session.add(vo)
    db.session.commit()
    blog_list = [marshal(vo, blog_fields) for vo in blog_fields]
    return jsonify(res_util.success(blog_list))
