from db.db import db
from vo.TestVO import Test_Parent_1_to_N_VO, Test_Child_1_to_N_VO, Test_Parent_N_N_VO, \
    Test_Child_N_N_VO


def test_vo_1_n():
    session = db.session
    # 一对多
    parent = Test_Parent_1_to_N_VO(name='morgan', full_name='morganlions')
    parent.children = Test_Child_1_to_N_VO(name='child 1 name', full_name='child 1 full name')
    session.add(parent)
    session.commit()
    # 如果parent 已经存在
    parent = session.query(Test_Parent_1_to_N_VO).filter(Test_Parent_1_to_N_VO.name == 'Morgan')
    children = [
        Test_Child_1_to_N_VO(name='child 2', full_name='child 2 full name', parent_obj=parent),
        Test_Child_1_to_N_VO(name='child 3', full_name='child 3 full name', parent_obj=parent),
    ]
    session.add_all(children)
    session.commit()
    # 查询
    parent = session.query(Test_Parent_1_to_N_VO).get(1)
    print(parent.children)
    # 一对多查询
    parent = session.query(Test_Parent_1_to_N_VO).filter(
        Test_Parent_1_to_N_VO.children.any(Test_Child_1_to_N_VO.name == u'child 1')).first()
    print(parent)


def test_vo_n_n():
    # 多对多
    session = db.session
    parent = Test_Parent_N_N_VO(name='Morgan', full_name='MorganLions')
    parent.children = [Test_Child_N_N_VO(name='child name', full_name='child full name')]
    # 提交数据
    session.add(parent)
    session.commit()
    # 如果是双向关系也可以这样添加
    child = Test_Child_N_N_VO(name='child name', full_name='child full name')
    child.parents = [Test_Parent_N_N_VO(name='Morgan', full_name='Morgan Lions')]
    session.add(child)
    session.commit()
    # 找出数据在添加
    parent = session.query(Test_Parent_N_N_VO).filter(Test_Parent_N_N_VO.name == 'Morgan').one()
    parent.children = [Test_Child_N_N_VO(name='child name', full_name='child full name')]
    session.commit()
    # 删除多对多中间关系，不删除实体，这里我们对应的是children
    # 1清除parent 中的 children 数据
    # session=Session()
    parent = session.query(Test_Parent_N_N_VO).filter(Test_Parent_N_N_VO.name == 'Morgan').one()
    parent.children = []
    session.commit()
    # 2删除两个表对应的关系
    children = session.query(Test_Child_N_N_VO).filter(Test_Child_N_N_VO.name == 'child 1').one()
    parent.children.remove(children)
    session.commit()
    # 删除实体，不删除关系
    #  1:创建要实验的数据
    parent = session.query(Test_Parent_N_N_VO).filter(Test_Parent_N_N_VO.name == 'Morgan').one()
    children = Test_Child_N_N_VO(name='child 5')
    parent.children = [children]
    session.commit()
    # 2: 删除实体
    children = session.query(Test_Child_N_N_VO).filter(Test_Child_N_N_VO.name == 'child 5').one()
    session.delete(children)
    session.commit()

    # 单条数据查询
    parent = session.query(Test_Parent_N_N_VO).get(1)
    # 找到儿子
    print(parent.children)
    children = session.query(Test_Child_N_N_VO).get(1)
    # 找到父亲
    print(children.parent)
    # 多条数据查询
    parent = session.query(Test_Parent_N_N_VO).order_by(Test_Parent_N_N_VO.id)
    count = parent.count()  # 计数
    page = 1
    limit = 10
    parent = parent.offset(page).limit(limit)
    result = []
    for p in parent.all():
        arg = {}
        arg['id'] = p.id
        arg['name'] = p.name
        arg['full_name'] = p.full_name
        arg['children'] = {c.name: c.full_name for c in p.children}
        result.append(arg)
    print(result)
    # def column_dict(self, params=None, operation=None, relation=None):
    #     '''
    #     sql查询返回字典
    #     :param params: 需要显示的字段
    #     :param operation:操作方法
    #                     {'one':func1 'two': func2 , 'param':'提示术语'}
    #                     {'one':func1 'two': 'param':'提示术语'}
    #                     {'one':func1 'two': func2 }
    #                     param 作为第二个函数的参数,也可以作为单独的提示
    #     :param relation
    #     :return:
    #     '''
    #     model_dict = dict(self.__dict__)
    #     del model_dict['_sa_instance_state']
    #     if params:
    #         keys = [k for k in model_dict.keys()]
    #         for key in keys:
    #             if key not in params:
    #                 del model_dict[key]
    #     if relation:
    #         for r in relation:
    #             rel = eval('self.{0}'.format(r))
    #             result = [self.change_str(operation, x.column_dict()) for x in rel]
    #             model_dict['{0}'.format(r)] = result
    #     if operation:
    #         model_dict = self.change_str(operation, model_dict)
    #         if isinstance(model_dict, str):
    #             return False, 'model_dict', 0
    #     return model_dict
    # Base.column_dict = column_dict
    #
    # @staticmethod
    # def change_str(operation, model_dict):
    #     '''
    #     改变输出类型
    #     :param operation:
    #     :param model_dict:
    #     :return:
    #     '''
    #
    #     for key, funcs in operation.items():
    #         method = model_dict[key]
    #         func = funcs.get('one')
    #         second_func = funcs.get('two')
    #         param = funcs.get('param')
    #         if param and func and second_func:
    #             model_dict[key] = func(method) if method else second_func(param)
    #         elif second_func is None and func and param:
    #             model_dict[key] = func(method) if method else param
    #         elif param is None and func and second_func:
    #             model_dict[key] = func(method) if method else second_func()
    #         else:
    #             return '操作函数设置错误'
    #     return model_dict
    # 调用
    # parent = session.query(Test_Parent_N_N_VO)
    #
    # operation = {
    #  'name': {'one': func, 'param': '参数'},
    # }
    # relation = ['children']
    # result = [x.column_dict(operation=operation, relation=relation) for x in parent]
