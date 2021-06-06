# -*- coding:utf-8 -*-
"""
@Time: 2021/6/6
@Description: todo 无限进化 : 领域 协议 拓展
"""


class Rule:
    @property
    def attr_num(self):
        """
        todo 使用二分 分类,类似cnn 数字识别
        :return:
        """
        return 2

    @property
    def method_number(self):
        """
        todo 根据attr 排列组合所有结果
        :return:
        """
        return 9


class Condition:
    pass


class IHumanApi:
    """
    掌控(随心所欲)  时间上,效率

    eg:树形,子节点个数约束

    所有结果,关键节点,权重
    """

    def __init__(self):
        self.test_attr = 1
        self.check_method()

    # def __new__(cls, *args, **kwargs):
    #     pass

    def get_method(self):
        print(IHumanApi.__dict__)
        print(object.__dict__)
        print(self.__dict__)
        print(dir(self))
        print(dir(object))
        self_list = [i for i in dir(self) if i not in dir(object)]
        print(self_list)
        return self_list

    def check_method(self):
        print("check_method")
        assert len(self.get_method()) < 9, 123


class Test(IHumanApi):
    pass


if __name__ == '__main__':
    m = IHumanApi()
    m.get_method()
    Test()
