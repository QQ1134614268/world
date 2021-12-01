# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/27 0:26
"""


class Hero:
    def __init__(self):
        self.healthPoint = 30  # 血量
        self.attack = 0  # 攻击力
        self.defence = 0  # 护甲
        self.magicPoint = 0  # 魔力值

    def skill(self):
        pass

    def underFire(self, attack):
        if self.defence >= attack:
            self.defence -= attack
        else:
            self.defence = 0
            self.healthPoint = self.healthPoint + self.defence - attack

    def addDefence(self, defence):
        self.defence += defence

    def addHealthPoint(self, health_point):
        self.healthPoint += health_point

    def heroDie(self):
        if self.healthPoint <= 0:
            return True


class PriestHero(Hero):
    def __init__(self):
        super().__init__()

    def skill(self):
        self.healthPoint += 2


class MagesHero(Hero):
    def __init__(self):
        super().__init__()

    def skill(self):
        self.attack = 1
