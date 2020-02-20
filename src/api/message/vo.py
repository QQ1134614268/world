from sqlalchemy import Column, Integer, String,ForeignKey

from vo.BaseModel import BaseTable


class PersonSpeech(BaseTable):
    __tablename__ = 'person_speech_t'
    userId = Column(Integer)
    content = Column(String(256))
    group = Column(String(256))  # 分组 家人 朋友  陌生人...


class Comment(BaseTable):
    __tablename__ = 'message_comment_t'
    personSpeechId = Column(Integer,ForeignKey('person_speech_t.id'))
    content = Column(String(256))
