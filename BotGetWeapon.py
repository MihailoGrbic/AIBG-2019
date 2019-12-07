from Bot import Bot
from BotWalker import BotWalker
from GameState import GameState
import utils


class BotGetWeapon(Bot):

    def __init__(self, url, gameId, playerId, random=False):
        super().__init__(url, gameId, playerId, random)
        self.bot_walker = BotWalker(self.url, self.gameId, self.playerId)

    def play_single_turn(self, current_game_state: GameState):
        md = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y),
                                [b for b in current_game_state.map.items if
                                 b["itemType"] == "SWORD_FORTRESS" and b["id"] == current_game_state.playerId])
        self.bot_walker.x_sel = md[0]
        self.bot_walker.y_sel = md[1]
        self.bot_walker.play_single_turn(current_game_state)
