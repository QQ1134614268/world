from flask import jsonify

from util import ResUtil
from db.db import db


def consume_money(userId, money):
    # with db.engine.begin() as conn:
    sql = "SELECT amount FROM wallet_t t WHERE t.userId = :userId  LOCK IN SHARE MODE"
    cursor = db.session.execute(sql, params={"userId": userId})
    amount = cursor.first()["amount"]
    if money > amount:
        db.session.commit();
        return jsonify(ResUtil.fail("余额不足"))
    db.session.execute("update wallet_t set amount = amount - :money where userId = :userId",
                       params={"userId": userId, "money": money})
    db.session.commit();
    return jsonify(ResUtil.success("操作成功"))


def add_money(userId, money):
    db.session.execute("update wallet_t set amount = amount + :money where userId = :userId",
                       params={"userId": userId, "money": money})
    db.session.commit();
    return jsonify(ResUtil.success("操作成功"))
