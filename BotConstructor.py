from Bot import Bot
from Bot import actions
from GameState import GameState
from BotRandom import BotRandom
from BotWalker import BotWalker
import utils


class BotConstructor(Bot):

    def __init__(self, build_type: str):
        self.build_type = build_type
        self.fallback = BotRandom()
        self.walker = BotWalker()

    def play_single_turn(self, current_game_state: GameState):
        cur_pos = (current_game_state.self_info.x, current_game_state.self_info.y)
        if self.build_type == "HOUSE":
            pathpath = utils.find_path_to(current_game_state.self_info, current_game_state.other_info, current_game_state.map, 0, 0)
            for diff in [(-1, 0, 'a'), (1, 0, 'd'), (0, 1, 's'), (0, -1, 'w')]:
                if utils.move_available(current_game_state.map, current_game_state.other_info, cur_pos[0] + diff[0],
                                        cur_pos[1] + diff[1]) and not diff[2] == pathpath[0]:
                    return actions["HOUSE_"] + diff[2]

            # no place for house!
            return pathpath[0]
        else:
            if self.build_type == "FORTRESS":
                nearest_sub = utils.find_nearest_by_type(current_game_state.map, cur_pos, "HOUSE")
            else:
                nearest_sub = utils.find_nearest_by_type(current_game_state.map, cur_pos, "FORTRESS")
            if nearest_sub is not None:
                if utils.dist(nearest_sub[0], nearest_sub[1], cur_pos[0], cur_pos[1]) == 1:
                    return actions[self.build_type + "_"] + utils.direction(nearest_sub, cur_pos)
                else:
                    self.walker.x_sel = nearest_sub[0]
                    self.walker.y_sel = nearest_sub[1]
                    return self.walker.play_single_turn(current_game_state)
        print("[BotConstructor] Sjebao si uslove")
        return self.fallback.play_single_turn(current_game_state)
