from Bot import Bot
import utils
from PlayerInfo import PlayerInfo


class BotWalker(Bot):

    def __init__(self, url, gameId, playerId, random=False, x=-1, y=-1):
        super().__init__(url, gameId, playerId, random)
        self.x_sel = x
        self.y_sel = y

    def play_single_turn(self, current_game_state, current_map, self_info: PlayerInfo, other_info: PlayerInfo):
        path = utils.find_path_to(self_info, current_map, self.x_sel, self.y_sel)
        self.doAction(path[0])