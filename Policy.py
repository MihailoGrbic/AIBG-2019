from Bot import Bot
import GameState
from GameState import GameState
import utils

class Policy:
    def __init__(self, bot: Bot):
        self.bot = bot

    def should_execute(self, current_game_state: GameState):
        pass


class PolicyAlwaysAllow(Policy):
    def should_execute(self, current_game_state: GameState):
        return True


class PolicyIsBeginningAndNoSwordBuilding(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.turns_left > 3900  # and current_game_state.map.swordBuildings.empty


class PolicyIsEnemyCloseAndDangerous(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.health < current_game_state.other_info.health
        # and len(current_game_state.other_info.weapons) == 2


def sword_fortress_exists(current_game_state):
    return len([b for b in current_game_state.map.items if
                b["itemType"] == "SWORD_FORTRESS" and b["id"] == current_game_state.playerId]) > 0


class BuildSwordFortress(Policy):
    def should_execute(self, current_game_state: GameState):
        return not sword_fortress_exists(current_game_state)


class GetSword(Policy):
    def should_execute(self, current_game_state: GameState):
        md = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y),
                        [b for b in current_game_state.self_info.player_info["buildings"] if
                        b["itemType"] == "SWORD_FORTRESS" and b["id"] == current_game_state.playerId])

        return sword_fortress_exists(current_game_state) \
                and ((current_game_state.self_info.player_info["weapon1"] is None \
                and current_game_state.self_info.player_info["weapon2"] is None) \
                or utils.dist(md[0], md[1], current_game_state.self_info.x, current_game_state.self_info.y) == 1)


class AttackWithSword(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.player_info["weapon1"] is not None \
               or current_game_state.self_info.player_info["weapon2"] is not None


class Random(Policy):
    def should_execute(self, current_game_state: GameState):
        return True
