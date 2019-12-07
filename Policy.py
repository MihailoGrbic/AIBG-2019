from Bot import Bot
import GameState
from GameState import GameState


class Policy:
    def __init__(self, bot: Bot):
        self.bot = bot

    def should_execute(self, current_game_state : GameState):
        pass

class PolicyAlwaysAllow(Policy):
    def should_execute(self, current_game_state : GameState):
        return True

class PolicyIsBeginningAndNoSwordBuilding(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.turns_left > 3900 # and current_game_state.map.swordBuildings.empty

class PolicyIsEnemyCloseAndDangerous(Policy):
    def should_execute(self, current_game_state : GameState):
        return current_game_state.self_info.health < current_game_state.other_info.health
            # and len(current_game_state.other_info.weapons) == 2


def sword_fortress_exists(current_game_state):
    return len([b for b in current_game_state.map.items if
                b["itemType"] == "SWORD_FORTRESS" and b["id"] == current_game_state.playerId]) > 0


class BuildSwordFortress(Policy):
    def should_execute(self, current_game_state: GameState):
        return not sword_fortress_exists(current_game_state) \
               or (current_game_state.self_info.player_info["weapon1"] is None
                   or current_game_state.self_info.player_info["weapon2"] is None)


class GetSword(Policy):
    def should_execute(self, current_game_state: GameState):
        return sword_fortress_exists(current_game_state) \
               and current_game_state.self_info.player_info["weapon1"] is None \
               and current_game_state.self_info.player_info["weapon2"] is None


class AttackWithSword(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.player_info["weapon1"] is not None \
               and current_game_state.self_info.player_info["weapon2"] is not None
