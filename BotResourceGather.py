from Bot import Bot
from Bot import actions
from BotBuild import BotBuild
from BotAttackWithSword import BotAttackWithSword
from BotGetWeapon import BotGetWeapon
from GameState import GameState
from BotRandom import BotRandom
from BotWalker import BotWalker
import Policy
import utils


class BotResourceGatherer(Bot):

    def __init__(self, resource: str):
        self.resource = resource
        self.walker = BotWalker()

    def play_single_turn(self, current_game_state: GameState):
        self_pos = (current_game_state.self_info.x, current_game_state.self_info.y)
        closest_resource = utils.find_nearest_by_type(current_game_state.map, (self_pos[0], self_pos[1]), self.resource)
        if current_game_state.self_info.get_space_left() == 0:
            if self.resource == "METAL_SHOP":
                if current_game_state.self_info.get_resource("STONE") > 0:
                    return actions["LEAVE_STONE"]
                else:
                    return actions["LEAVE_WOOD"]
            if self.resource == "STONE_SHOP":
                if current_game_state.self_info.get_resource("METAL") > 0:
                    return actions["LEAVE_METAL"]
                else:
                    return actions["LEAVE_WOOD"]
            if self.resource == "WOOD_SHOP":
                if current_game_state.self_info.get_resource("METAL") > 0:
                    return actions["LEAVE_METAL"]
                else:
                    return actions["LEAVE_STONE"]
        if utils.dist(closest_resource[0], closest_resource[1], self_pos[0], self_pos[1]) == 1:
            return actions["TAKE_"] + utils.direction((closest_resource[0], closest_resource[1]),
                                                      (self_pos[0], self_pos[1]))
        else:
            self.walker.x_sel = closest_resource[0]
            self.walker.y_sel = closest_resource[1]
            return self.walker.play_single_turn(current_game_state)
