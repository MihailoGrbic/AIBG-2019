import Bot
from Bot import actions
import random

class BotGrbic(Bot):

    def __init__(self, url, gameId, playerId):
        super(BotGrbic, self).__init__(url, gameId, playerId)

    def play_single_turn(self, current_game_state, current_map, self_info, other_info):
        x = random.randint(0, 4)
        if x == 0:
            self.doAction(actions["UP"])
        if x == 1:
            self.doAction(actions["DOWN"])
        if x == 2:
            self.doAction(actions["LEFT"])
        if x == 3:
            self.doAction(actions["RIGHT"])