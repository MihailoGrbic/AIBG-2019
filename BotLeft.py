from Bot import Bot
from Bot import actions
import random


class BotLeft(Bot):

    def __init__(self, url, gameId, playerId):
        super(BotLeft, self).__init__(url, gameId, playerId)

    def play_single_turn(self, current_game_state, current_map, self_info, other_info):
        self.doAction(actions["LEFT"])
