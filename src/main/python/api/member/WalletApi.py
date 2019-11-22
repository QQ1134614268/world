


def consume_money(money):

    pass

def add_money(money):
    pass


def consume_money2(money):
    sql="SELECT * FROM wallet_t t WHERE t.pro_id = ? LOCK IN SHARE MODE"
    with transaction.atomic():
        models.Userinfo.objects.create(username="python001", email="python001@qq.com")
        models.Group.objects.create(title="python002")

    pass


def add_money2(money):
    pass
from functools import wraps
from contextlib import ContextDecorator

'''
示例程序:
创建一个新用户，同时将新用户关联到一家公司下，
这需要两步数据库操作，但是这应该是一个事务，
要么都完成，要么都未完成
注意：即使只有一步，也需要如下操作
flush和commit区别:
    > flush: 写数据库，但不提交，也就是事务未结束
    > commit: 是先调用flush写数据库，然后提交，结束事务，并开始新的事务

def create_user(name, phone):
    data = {
        'name': name,
        'phone': phone,
    }
    user = User(name)
    db.session.add(user)
    db.session.flush()
    return user

def create_user_and_company_mapping(user_id, commpany_id):
    data = {
        'user_id': user_id,
        'company_id': company_id,
    }
    mapping = UserCompanyMapping(**data)
    db.session.add(mapping)
    db.session.flush()
    return mapping

class CreateUser(Api):

    def post(self, params):
        name = params['name']
        phone = params['phone']
        company_id = params['company_id']
        # 这里用with语句将两个操作封闭成一个原子操作
        with atomic(db):
            user = create_user(name, phone)
            create_user_and_company_mapping(user.id, company_id)
        # 注意：即使只有一步创建用户的操作也需要这样写
        with atomic(db)
            user = create_user(name, phone)
'''


def atomic(db):
    '''
    '''
    if callable(db):
        return Atomic(db)(db)
    else:
        return Atomic(db)


class Atomic(ContextDecorator):

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        pass

    def __exit__(self, exc_typ, exc_val, tb):
        if exc_typ:
            self.db.session.rollback()
        else:
            self.db.session.commit()