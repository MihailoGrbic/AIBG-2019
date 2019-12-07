from Bot import Bot
from Bot import actions
from BotBuild import BotBuild
from BotAttackWithSword import BotAttackWithSword
from BotGetWeapon import BotGetWeapon
from GameState import GameState
from BotRandom import BotRandom
import Policy
import utils


class BotRandomize(Bot):

    def __init__(self, bot : Bot, proc : float):
        self.bot = bot
        self.proc = proc

    def get_policy_list(self):
        return [
            Policy.PolicyRandom(BotRandom(), self.proc),
            Policy.PolicyAlwaysAllow(self.bot)
        ]

    def play_single_turn(self, current_game_state: GameState):
        return self.get_child_bot(current_game_state).play_single_turn(current_game_state)
