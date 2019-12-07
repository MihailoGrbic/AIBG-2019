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
            Policy.AttackWithSword(BotAttackWithSword(priority_buildings=True)),
            Policy.GetSword(BotGetWeapon()),
            Policy.BuildSwordFortress(self.x),
            Policy.Random(BotRandom())
            
        ]

    def play_single_turn(self, current_game_state: GameState):
        return self.get_child_bot(current_game_state).play_single_turn(current_game_state)
