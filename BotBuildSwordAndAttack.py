from Bot import Bot
from Bot import actions
from BotBuild import BotBuild
from BotAttackWithSword import BotAttackWithSword
from BotGetWeapon import BotGetWeapon
from GameState import GameState
from BotRandom import BotRandom
import BotBuilder
import Policy
import utils


class BotBuildSwordAndAttack(Bot):

    def __init__(self, pussyRating : int):
        self.x = BotBuild()
        self.pussyRating = pussyRating

    def get_policy_list(self):
        return [
            Policy.AttackWithSword(BotAttackWithSword(self.pussyRating, priority_buildings=True)),
            Policy.GetSword(BotGetWeapon()),
            # Policy.BuildSwordFortress(self.x),
            BotBuilder.StarterPolicy(),
            Policy.PolicyAlwaysAllow(BotBuilder.BotBuilder())
        ]

    def play_single_turn(self, current_game_state: GameState):
        return self.get_child_bot(current_game_state).play_single_turn(current_game_state)
