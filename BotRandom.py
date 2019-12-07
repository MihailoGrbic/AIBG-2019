from Bot import Bot
from Bot import actions
import random


class BotRandom(Bot):

    def play_single_turn(self, current_game_state):
        x = random.randint(0, 4)
        if x == 0:
            self.doAction(actions["UP"])
        if x == 1:
            self.doAction(actions["DOWN"])
        if x == 2:
            self.doAction(actions["LEFT"])
        if x == 3:
            self.doAction(actions["RIGHT"])
