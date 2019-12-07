from Bot import Bot
from Policy import Policy
from BotWalker import BotWalker


class BotGetWeapon(Bot):

    def play_single_turn(self, current_game_state):
        bot = BotWalker(self.url, self.gameId, self.playerId, 10, 10)
        bot.play_single_turn(current_game_state)
