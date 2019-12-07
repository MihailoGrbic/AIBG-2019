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
from BotRunnaway import BotRunnaway


class BotBuildSwordAndAttackWithRunaway(Bot):

    def __init__(self, pussyRating : int):
        self.x = BotBuild()
        self.pussyRating = pussyRating

    def get_policy_list(self):
        return [
            Policy.PolicyPussy(BotRunnaway(), 20, 3),
            Policy.AttackWithSword(BotAttackWithSword(self.pussyRating, priority_buildings=True, should_use_ultra_aggressive=True)),
            Policy.GetSword(BotGetWeapon()),
            # Policy.BuildSwordFortress(self.x),
            BotBuilder.StarterPolicy(),
            Policy.PolicyAlwaysAllow(BotBuilder.BotBuilder())
        ]

    def play_single_turn(self, current_game_state: GameState):
        print(current_game_state.self_info.player_info["buildings"])
        print()
        print(current_game_state.other_info.player_info["buildings"])
        return self.get_child_bot(current_game_state).play_single_turn(current_game_state)
