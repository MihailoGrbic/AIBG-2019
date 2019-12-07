from Bot import Bot
from BotRandom import BotRandom
from Policy import *
from GamePlay import GamePlay

class GamePlaySingleBot(GamePlay):

    def __init__(self, url, gameId, playerId, bot : Bot):
        super().__init__(url, gameId, playerId)
        self.bot = bot


    def get_policy_list(self):
        return [
            PolicyAlwaysAllow(self.bot)
        ]

    def play_single_turn(self, current_game_state):
        command = input("Your move, bitch: ")
        self.doAction(command)