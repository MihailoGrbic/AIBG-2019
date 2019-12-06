from Bot import Bot
import utils
from PlayerInfo import PlayerInfo


class BotWalker(Bot):

    x_sel = -1
    y_sel = -1

    def play_single_turn(self, current_game_state, current_map, self_info: PlayerInfo, other_info: PlayerInfo):
        if self.x_sel == -1 or self.y_sel == -1 or (self.x_sel == self_info.x and self.y_sel == self_info.y) :
            self.x_sel = int(input("next x: "))
            self.y_sel = int(input("next y: "))
        path = utils.find_path_to(self_info, current_map, self.x_sel, self.y_sel)
        self.doAction(path[0])
