from flask import Blueprint, jsonify, request

from api.apply.member import WalletService, WalletVO
from api.apply.member.UserVO import MemberUserVO
from util import ResUtil
from db.db import db
from api.user import UserService

store_api = Blueprint("store_api", __name__, url_prefix='/store_api')


@store_api.route('/add_member', methods=['POST'])
def add_member():
    """
    用户注册
    ---
    tags:
      - store_api
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          添加会员
        required: true
        schema:
          id: member_user
          required:
            - phone
            - password
          properties:
            phone:
              description: 手机号
              type: string
              example: 18829040560
            password:
              description: 密码
              type: string
              example: abc123
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    phone = data.get('phone', '')
    store_id = UserService.get_id_by_token()
    if not phone:
        return jsonify(ResUtil.fail("手机号不能为空"))
    password = data.get('password', '')
    exist = MemberUserVO.query.filter_by(phone=phone).first()
    if exist:
        # db.session.query(MemberUserVO).filter(MemberUserVO.phone == phone).update({"password": password})
        return jsonify(ResUtil.fail("用户名已经存在"))
    vo = MemberUserVO(store_id=store_id, phone=phone, password=MemberUserVO.get_password(password))
    db.session.add(vo)
    db.session.commit()

    vo = WalletVO(userId=vo.id)
    db.session.add(vo)
    db.session.commit()
    return jsonify(ResUtil.success("添加vip成功"))


@store_api.route('/consume', methods=['POST'])
def consume():
    """
    消费
    ---
    tags:
      - member_api
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          会员消费
        required: true
        schema:
          id: member_user
          required:
            - amount
            - phone
          properties:
            amount:
              description: 金额
              type: float
              example: 1.0
            phone:
              description: 手机号
              type: float
              example: 18829400560
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    amount = data.get('amount')
    phone = data.get('phone')
    if not amount:
        return jsonify(ResUtil.fail("消费金额不能为空"))
    vo = MemberUserVO.query.filter_by(phone=phone).first()
    if not vo:
        return jsonify(ResUtil.fail("该会员不存在"))
    return WalletService.consume_money(vo.id, amount)


@store_api.route('/invest', methods=['POST'])
def invest():
    """
    会员充值
    ---
    tags:
      - member_api
    consumes:
      - application/json
    produces: ["application/json"]
    parameters:
      - in: body
        name: body
        description:
          会员充值
        required: true
        schema:
          id: member_user
          required:
            - amount
            - phone
          properties:
            amount:
              description: 金额
              type: float
              example: 1.0
            phone:
              description: 手机号
              type: float
              example: 18829400560
    responses:
      500:
        description: server error
      200:
        description: success
    """
    data = request.get_json()
    amount = data.get('amount')
    phone = data.get('phone')
    if not amount:
        return jsonify(ResUtil.fail("充值金额不能为空"))
    vo = MemberUserVO.query.filter_by(phone=phone).first()
    if not vo:
        return jsonify(ResUtil.fail("该会员不存在"))
    return WalletService.consume_money(vo.id, amount)
