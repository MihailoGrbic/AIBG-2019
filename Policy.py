from Bot import Bot
import GameState
import utils
from GameState import GameState
from BotResourceGather import BotResourceGatherer
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
    return len([b for b in current_game_state.self_info.player_info["buildings"] if b["itemType"] == "SWORD_FORTRESS"]) > 0


class BuildSwordFortress(Policy):
    def should_execute(self, current_game_state: GameState):
        return not sword_fortress_exists(current_game_state)


class GetSword(Policy):
    def should_execute(self, current_game_state: GameState):
        md = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y),
                                [b for b in current_game_state.self_info.player_info["buildings"] if
                                 b["itemType"] == "SWORD_FORTRESS"])

        if md is not None:
            nearest_sword = current_game_state.map.tiles[md[1]][md[0]]["item"]
            two_swords_in = max(0, 20 - nearest_sword["numWeapons"] * 10 - nearest_sword["timeSinceMakeWeapon"])

        return sword_fortress_exists(current_game_state) \
            and two_swords_in <= utils.dist(md[0], md[1], current_game_state.self_info.x, current_game_state.self_info.y) - 1 \
            and ((current_game_state.self_info.player_info["weapon1"] is None \
            and current_game_state.self_info.player_info["weapon2"] is None) \
            or utils.dist(md[0], md[1], current_game_state.self_info.x, current_game_state.self_info.y) == 1)


class AttackWithSword(Policy):
    def should_execute(self, current_game_state: GameState):
        md = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y),
                                [b for b in current_game_state.self_info.player_info["buildings"] if
                                 b["itemType"] == "SWORD_FORTRESS"])

        num_of_swords = 0
        if current_game_state.self_info.player_info["weapon1"] is not None: num_of_swords += 1 
        if current_game_state.self_info.player_info["weapon2"] is not None: num_of_swords += 1 

        return num_of_swords == 2 or (num_of_swords == 1 and md is not None \
        and utils.dist(md[0], md[1], current_game_state.self_info.x, current_game_state.self_info.y) > 1)



class Random(Policy):
    def should_execute(self, current_game_state: GameState):
        return True


class GetReadyForBattle(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.player_info["weapon1"] is not None \
               and current_game_state.self_info.player_info["weapon2"] is not None \
               and utils.dist(current_game_state.self_info.player_info['x'],
                              current_game_state.self_info.player_info['y'],
                              current_game_state.other_info.player_info['x'],
                              current_game_state.other_info.player_info['y']) == 2


class GatherResource(Policy):
    def __init__(self, resource: str, amount: int = 3):
        super().__init__(BotResourceGatherer(resource))
        self.resource = resource
        self.amount = amount

    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.player_info["resources"][self.resource] < self.amount
