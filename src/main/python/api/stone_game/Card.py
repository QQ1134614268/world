# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/27 0:44
"""


class Card:
    def __init__(self):
        self.name = "Card"
        self.magicPoint = 0  # 魔力值
        self.attack = 0  # 攻击力
        self.healthPoint = 0  # 血量
        self.attack_times = 0  # 血量

    def cardDie(self):
        if self.healthPoint <= 0:  # 血量
            return True

    def bearAttack(self, attack):
        self.healthPoint -= attack

    def skill(self):
        pass


class SpaceCard(Card):
    def __init__(self):
        super().__init__()
        self.name = "SpaceCard"
        self.magicPoint = 0  # 魔力值
        self.attack = 1  #
        self.healthPoint = 1

    def skill(self):
        pass


class LittleRabbitCard(Card):
    def __init__(self):
        super().__init__()
        self.name = "LittleRabbitCard"
        self.magicPoint = 1  # 魔力值
        self.attack = 1  # 攻击力
        self.healthPoint = 2

    def skill(self):
        pass


class LittleAppleCard(Card):
    def __init__(self):
        super().__init__()
        self.name = "LittleAppleCard"
        self.magicPoint = 1  # 魔力值
        self.attack = 2  # 攻击力
        self.healthPoint = 1

    def skill(self):
        pass


class H_2_2_3_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "LittleAppleCard"
        self.magicPoint = 2  # 魔力值
        self.attack = 2  # 攻击力
        self.healthPoint = 3

    def skill(self):
        pass


class H_2_3_2_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_3_2_Card"
        self.magicPoint = 2  # 魔力值
        self.attack = 3  # 攻击力
        self.healthPoint = 2

    def skill(self):
        pass


class H_2_2_3_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_2_3_Card"
        self.magicPoint = 2  # 魔力值
        self.attack = 2  # 攻击力
        self.healthPoint = 3

    def skill(self):
        pass


class H_3_3_4_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_2_3_Card"
        self.magicPoint = 3  # 魔力值
        self.attack = 3  # 攻击力
        self.healthPoint = 4

    def skill(self):
        pass


class H_3_4_3_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_2_3_Card"
        self.magicPoint = 3  # 魔力值
        self.attack = 4  # 攻击力
        self.healthPoint = 3

    def skill(self):
        pass


class H_4_4_5_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_2_3_Card"
        self.magicPoint = 4  # 魔力值
        self.attack = 4  # 攻击力
        self.healthPoint = 5

    def skill(self):
        pass


class H_4_5_4_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_2_3_Card"
        self.magicPoint = 4  # 魔力值
        self.attack = 5  # 攻击力
        self.healthPoint = 4

    def skill(self):
        pass


class H_5_5_5_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_2_3_Card"
        self.magicPoint = 5  # 魔力值
        self.attack = 5  # 攻击力
        self.healthPoint = 5

    def skill(self):
        pass


class H_5_5_6_Card(Card):
    def __init__(self):
        super().__init__()
        self.name = "H_2_2_3_Card"
        self.magicPoint = 5
        self.attack = 5
        self.healthPoint = 6

    def skill(self):
        pass
