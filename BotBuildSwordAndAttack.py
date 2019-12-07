from Bot import Bot
from Bot import actions
from BotBuild import BotBuild
from BotAttackWithSword import BotAttackWithSword
from BotGetWeapon import BotGetWeapon
from GameState import GameState
from BotRandom import BotRandom
import Policy
import utils


class BotBuildSwordAndAttack(Bot):

    def __init__(self):
        self.x = BotBuild()

    def get_policy_list(self):
        return [
            Policy.BuildSwordFortress(self.x),
            Policy.GetSword(BotGetWeapon()),
            Policy.AttackWithSword(BotAttackWithSword()),
            Policy.Random(BotRandom())
        ]

    def get_child_bot(self, current_game_state):
        for policy in self.get_policy_list():
            if policy.should_execute(current_game_state):
                return policy.bot
        return None

    def play_single_turn(self, current_game_state: GameState):
        return self.get_child_bot(current_game_state).play_single_turn(current_game_state)
