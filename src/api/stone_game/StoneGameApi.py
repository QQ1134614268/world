# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/27 21:20
"""
from flask import Blueprint

from .GameSquare import Game

stone_game_api = Blueprint("stone_game_api", __name__, url_prefix='/api/stone_game_api')

game = Game()
