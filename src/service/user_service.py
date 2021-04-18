# -- coding:UTF-8 --
from flask import jsonify
from flask_restful import fields, marshal

from config.mysql_db import db
from service.token_service import get_id_by_token
from util import res_util
from vo.table_model import UserVO, Attention

attentionFields = {
    'group': fields.String,
    "username": fields.String(attribute="attentionUser.username"),
    "attentionUserId": fields.String(attribute="attentionUser.id"),
}


def addAttention(userId, group):
    vo = Attention.query.filter_by(attentionUserId=userId).first()
    if vo:
        return jsonify(res_util.fail("已经关注"))
    vo = Attention(userId=get_id_by_token(), attentionUserId=userId, group=group)
    db.session.add(vo)
    db.session.commit()
    return jsonify(res_util.success("关注成功"))


def getAttentionList():
    """

    :rtype: list
    """
    vo_list = Attention.query.filter(Attention.userId == get_id_by_token()).all()
    message_list = [marshal(vo, attentionFields) for vo in vo_list]
    return message_list


def updateAttention(attentionId, group):
    Attention.query.filter_by(Attention.id == attentionId).update(dict(group=group))
    db.session.commit()
    return True


def deleteAttention(attentionId):
    vo = Attention(attentionId=attentionId)
    db.session.delete(vo)
    db.session.commit()
    return True


def getUserType():
    user = UserVO.query.filter_by(id=get_id_by_token()).first()
    return user.userType


if __name__ == '__main__':
    # info = {"username": "w&g", "userid": 1, "timestamp": int(time.time())}
    # token = jwt.encode(info, secret, algorithm='HS256')
    # print(type(token))
    # str_token = str(token, "utf_8")
    # print(str_token)
    # b_token = bytes(str_token, "utf_8")
    # print(b_token)
    # info2 = jwt.decode(b_token, secret, algorithms=['HS256'])
    # print(info2, type(info2))
    #
    # temp_user = {"username": "w&g", "userid": 1, "timestamp": int(time.time())}
    # jwt_token = str(get_payload(get_token(temp_user)))
    # print(jwt_token)

    # base64.b64encode( )
    # base64.b64decode( )
    # base64.encodestring()
    # base64.decodestring()
    # base64.decode()
    # base64.encode()
    pass
