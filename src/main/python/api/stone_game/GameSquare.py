# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/27 1:02
"""
import random

from .Card import *
from .HeroCard import MagesHero


class BlueRole:
    def __init__(self):
        self.magicPoint = 0
        self.hero = MagesHero()
        self.handDepository = []
        self.sleepCardList = []
        self.activeCardList = []
        self.cardDepository = [SpaceCard(), LittleRabbitCard(), LittleAppleCard(), H_2_2_3_Card(), H_2_3_2_Card(),
                               H_2_2_3_Card(), H_3_3_4_Card(), H_3_4_3_Card(), H_4_4_5_Card(), H_4_5_4_Card(),
                               H_5_5_5_Card(), H_5_5_6_Card(), ]
        self.cardDepository = random.shuffle(self.cardDepository)
        self.isOver = True

    def getCard(self):
        if self.cardDepository:
            card = self.cardDepository.pop(0)
            self.handDepository.append(card)

    def showCard(self, index):
        card = self.handDepository.pop(0)
        self.sleepCardList.append(card)


class RedRole:
    def __init__(self):  # hero cardDepository
        self.magicPoint = 0
        self.hero = MagesHero()
        self.handDepository = []
        self.sleepCardList = []
        self.activeCardList = []
        self.cardDepository = [SpaceCard(), LittleRabbitCard(), LittleAppleCard(), H_2_2_3_Card(), H_2_3_2_Card(),
                               H_2_2_3_Card(), H_3_3_4_Card(), H_3_4_3_Card(), H_4_4_5_Card(), H_4_5_4_Card(),
                               H_5_5_5_Card(), H_5_5_6_Card(), ]
        self.cardDepository = random.shuffle(self.cardDepository)
        self.isOver = True

    def getCard(self):
        if self.cardDepository:
            card = self.cardDepository.pop(0)
            self.handDepository.append(card)

    def showCard(self, index):
        if self.cardDepository:
            card = self.cardDepository.pop(0)
            self.handDepository.append(card)


class Game:

    def __init__(self):
        self.blueHero = BlueRole()
        self.redRole = RedRole()
        self.turn = True

    def gameStart(self):
        #  todo 循环回合
        while True:
            # turn
            if self.turn:
                break
            if self.turn:
                break
            if self.gameTurn():
                self.turn = not self.turn

    def gameTurn(self):
        # todo
        return True

    def gameOver(self):
        if self.blueHero.hero.heroDie():
            return "B_hero winner"

        if self.redRole.hero.heroDie():
            return "A_hero winner"

    def attackCard(self, start_card_list, start_card, bear_card, bear_card_list):
        start_card.bearAttack(bear_card.attack)
        bear_card.bearAttack(start_card.attack)
        if start_card.cardDie:
            start_card_list.pop(start_card)
        if bear_card.cardDie:
            bear_card_list.pop(bear_card)

    def attackHero(self, start_card, hero):
        hero.addHealthPoint(-start_card)
        if hero.heroDie():
            return True

    def heroAttackCard(self, hero, start_card):
        pass
