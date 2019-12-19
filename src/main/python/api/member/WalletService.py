from flask import jsonify

from config import res
from db.db import db


# flask 默认使用事物?????????
def consume_money(userId, money):
    # with db.engine.begin() as conn:
    sql = "SELECT amount FROM wallet_t t WHERE t.userId = :userId  LOCK IN SHARE MODE"
    cursor = db.session.execute(sql, params={"userId": userId})
    amount = cursor.first()["amount"]
    if money > amount:
        db.session.commit();
        return jsonify(res.fail("余额不足"))
    db.session.execute("update wallet_t set amount = amount - :money where userId = :userId",
                       params={"userId": userId, "money": money})
    db.session.commit();
    return jsonify(res.success("操作成功"))


# update
#
# 案例: todo
#
# # 原生sql update tb_book set name = "围城" where id = 1;
# 方法一:
# book = BookInfo.query.get(1)
# book.name = "围城"
# db.session.add(book)
# db.session.commit()
# 方法二 升级版:
# # django.db update 传入是 命名参数 SQLAlchemy update 传入是字典
# BookInfo.query.filter_by(name="人间失格").update({(name:"西游记"}))
# db.session.commit()

def add_money(userId, money):
    db.session.execute("update wallet_t set amount = amount + :money where userId = :userId",
                       params={"userId": userId, "money": money})
    db.session.commit();
    return jsonify(res.success("操作成功"))
