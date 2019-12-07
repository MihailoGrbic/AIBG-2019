from Bot import Bot
from Bot import actions


class BotLeft(Bot):

    def play_single_turn(self, current_game_state):
        self.doAction(actions["LEFT"])
