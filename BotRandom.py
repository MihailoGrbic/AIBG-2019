from Bot import Bot
from Bot import actions
import random


class BotRandom(Bot):

    def play_single_turn(self, current_game_state):
        x = random.randint(0, 4)
        if x == 0:
            return actions["UP"]
        if x == 1:
            return actions["DOWN"]
        if x == 2:
            return actions["LEFT"]
        if x == 3:
            return actions["RIGHT"]
