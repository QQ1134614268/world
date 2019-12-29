from sqlalchemy import Column, Integer, String

from db.db import db
from vo.BaseModel import BaseTable


class BlogVO(BaseTable):
    __tablename__ = 'blog_t'
    user_id = Column(Integer)
    content = Column(String(256))
    up_files = Column(String(1024))
    # todo   backref='b_c'
    comments = db.relationship('BlogCommentVO', backref='b_c', lazy='dynamic')


class BlogCommentVO(BaseTable):
    __tablename__ = 'blog_comment_t'
    user_id = Column(Integer)
    blog_id = Column(db.Integer, db.ForeignKey('blog_t.id'))
    comment = Column(String(256))
