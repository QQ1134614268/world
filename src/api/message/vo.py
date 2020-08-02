from sqlalchemy import Column, Integer, String, ForeignKey, Text

from config.mysql_db import BaseTable


class   PersonSpeech(BaseTable):
    __tablename__ = 'person_speech_t'
    userId = Column(Integer)
    title = Column(String(256))
    content = Column(Text)
    group = Column(String(256))  # 分组 家人 朋友  陌生人...


class Comment(BaseTable):
    __tablename__ = 'message_comment_t'
    personSpeechId = Column(Integer,ForeignKey('person_speech_t.id'))
    content = Column(String(256))
