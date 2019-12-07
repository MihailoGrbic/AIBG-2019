from Bot import Bot
from BotRunnaway import BotRunnaway
import GameState
import utils
from GameState import GameState
from BotResourceGather import BotResourceGatherer
import utils
import random


class Policy:
    def __init__(self, bot: Bot):
        self.bot = bot

    def should_execute(self, current_game_state: GameState):
        pass


class PolicyAlwaysAllow(Policy):
    def should_execute(self, current_game_state: GameState):
        print("PolicyAlwaysAllow " + str(True))
        return True


class PolicyIsBeginningAndNoSwordBuilding(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.turns_left > 3900  # and current_game_state.map.swordBuildings.empty


class PolicyIsEnemyCloseAndDangerous(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.health < current_game_state.other_info.health
        # and len(current_game_state.other_info.weapons) == 2


class PolicyRandom(Policy):
    def __init__(self, bot: Bot, prec: float):
        super().__init__(bot)
        self.prec = prec

    def should_execute(self, current_game_state: GameState):
        print("PolicyRandom " + str(random.random() < self.prec))
        return random.random() < self.prec


def sword_fortress_exists(current_game_state):
    return len(
        [b for b in current_game_state.self_info.player_info["buildings"] if b["itemType"] == "SWORD_FORTRESS"]) > 0


class BuildSwordFortress(Policy):
    def should_execute(self, current_game_state: GameState):
        print("BuildSwordFortress " + str(not sword_fortress_exists(current_game_state)))
        return not sword_fortress_exists(current_game_state)


class GetSword(Policy):
    def should_execute(self, current_game_state: GameState):
        md = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y),
                                [b for b in current_game_state.self_info.player_info["buildings"] if
                                 b["itemType"] == "SWORD_FORTRESS"])

        if md is not None:
            nearest_sword = current_game_state.map.tiles[md[1]][md[0]]["item"]
            two_swords_in = max(0, 20 - nearest_sword["numWeapons"] * 10 - nearest_sword["timeSinceMakeWeapon"])
            one_sword_in = max(0, 10 - nearest_sword["numWeapons"] * 10 - nearest_sword["timeSinceMakeWeapon"])
        else:
            print("GetSword False")
            return False

        num_of_swords = 0
        if current_game_state.self_info.player_info["weapon1"] is not None:
            num_of_swords += 1
        if current_game_state.self_info.player_info["weapon2"] is not None:
            num_of_swords += 1

        go_for_two_swords = two_swords_in <= utils.dist(md[0], md[1], current_game_state.self_info.x,
                                                        current_game_state.self_info.y) - 1 \
                            and num_of_swords == 0

        take_one_sword = utils.dist(md[0], md[1], current_game_state.self_info.x, current_game_state.self_info.y) == 1 \
                         and one_sword_in == 0 \
                         and num_of_swords == 1

        ret_val = sword_fortress_exists(current_game_state) and (go_for_two_swords or take_one_sword)

        print("GetSword " + str(ret_val))

        return ret_val


class AttackWithSword(Policy):

    def __init__(self, bot: Bot, enable_peaceful: bool = True):
        super().__init__(bot)
        self.enable_peaceful = enable_peaceful

    def should_execute(self, current_game_state: GameState):

        if not utils.can_move(current_game_state.map, current_game_state.other_info,
                              (current_game_state.self_info.x, current_game_state.self_info.y)) \
                and utils.dist(current_game_state.other_info.x, current_game_state.other_info.y,
                               current_game_state.self_info.x, current_game_state.self_info.y) == 1:
            return True

        if self.enable_peaceful and current_game_state.state_of_mind["Peaceful"]:
            return False

        md = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y),
                                [b for b in current_game_state.self_info.player_info["buildings"] if
                                 b["itemType"] == "SWORD_FORTRESS"])

        num_of_swords = 0
        if current_game_state.self_info.player_info["weapon1"] is not None:
            num_of_swords += 1
        if current_game_state.self_info.player_info["weapon2"] is not None:
            num_of_swords += 1

        ret_val = num_of_swords == 2 or (num_of_swords == 1 and (md is None 
                                        or utils.dist(md[0], md[1], current_game_state.self_info.x, 
                                        current_game_state.self_info.y) > 1))

        print("AttackWithSword " + str(ret_val))

        return ret_val


class GetReadyForBattle(Policy):
    def should_execute(self, current_game_state: GameState):
        ret_val = current_game_state.self_info.player_info["weapon1"] is not None \
                  and current_game_state.self_info.player_info["weapon2"] is not None \
                  and utils.dist(current_game_state.self_info.player_info['x'],
                                 current_game_state.self_info.player_info['y'],
                                 current_game_state.other_info.player_info['x'],
                                 current_game_state.other_info.player_info['y']) == 2

        print("GetReadyForBattle " + str(ret_val))

        return ret_val


class GatherResource(Policy):
    def __init__(self, resource: str, amount: int = 3):
        super().__init__(BotResourceGatherer(resource))
        self.resource = resource
        self.amount = amount

    def should_execute(self, current_game_state: GameState):
        ret_val = current_game_state.self_info.player_info["resources"][self.resource] < self.amount

        print("GatherResource " + str(ret_val))

        return ret_val


class PolicyPussy(Policy):

    def __init__(self, bot: Bot, hp_run, dist_run):
        super().__init__(BotRunnaway())
        self.hp_run = hp_run
        self.dist_run = dist_run

    def should_execute(self, current_game_state: GameState):

        # other_player_can_kill = (current_game_state.other_info.player_info['weapon1'] is not None and
        #             'swings' in current_game_state.other_info.player_info['weapon1'] and
        #             current_game_state.other_info.player_info['weapon1']['swings'] * 10 > \
        #             current_game_state.self_info.player_info['health'])

        ret_value = current_game_state.self_info.player_info['health'] < self.hp_run and \
                    current_game_state.other_info.player_info['health'] > current_game_state.self_info.player_info['health'] \
                     and \
                    utils.dist(current_game_state.self_info.player_info['x'],
                               current_game_state.self_info.player_info['y'],
                               current_game_state.other_info.player_info['x'],
                               current_game_state.other_info.player_info['y']) <= self.dist_run
        print("PolicyPussy " + str(ret_value))

        return ret_value
