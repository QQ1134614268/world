# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/27 1:02
"""
import random

from .Card import *
from .HeroCard import MagesHero, PriestHero

cardDepository = [SpaceCard(), LittleRabbitCard(), LittleAppleCard(), H_2_2_3_Card(), H_2_3_2_Card(),
                  H_2_2_3_Card(), H_3_3_4_Card(), H_3_4_3_Card(), H_4_4_5_Card(), H_4_5_4_Card(),
                  H_5_5_5_Card(), H_5_5_6_Card(), ]


class Role:
    def __init__(self, hero=MagesHero(), cardDepository=cardDepository):
        self.magicPoint = 0
        self.hero = hero
        self.handDepository = []
        self.activeCardList = []
        self.cardDepository = cardDepository
        self.cardDepository = random.shuffle(self.cardDepository)
        self.isOver = True

    def getCard(self):
        if self.cardDepository:
            card = self.cardDepository.pop(0)
            self.handDepository.append(card)

    def showCard(self, index):
        card = self.handDepository.pop(0)
        self.sleepCardList.append(card)


class Game:

    def __init__(self):
        self.redRole = Role(PriestHero(), cardDepository)  # 红色方先手
        self.blueHero = Role(MagesHero(), cardDepository)
        self.turn = True

    def gameStart(self, first_index, last_index):
        while not self.gameOver():

            while self.turn:
                # 红色方

                break
            while self.turn:
                break

    def gameTurn(self):
        self.turn = not self.turn

    def gameOver(self):
        if self.blueHero.hero.heroDie():
            return "B_hero winner"

        if self.redRole.hero.heroDie():
            return "A_hero winner"
        return False

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
