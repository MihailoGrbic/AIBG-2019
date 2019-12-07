from Bot import Bot
from BotWalker import BotWalker
from GameState import GameState
from Bot import actions
import utils


class BotGetWeapon(Bot):

    def __init__(self):
        self.bot_walker = BotWalker()

    def play_single_turn(self, current_game_state: GameState):
        md = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y),
                                [b for b in current_game_state.map.items if
                                 b["itemType"] == "SWORD_FORTRESS" and b["id"] == current_game_state.playerId])
        if utils.dist(md[0], md[1], current_game_state.self_info.x, current_game_state.self_info.y) == 1:
            if md[0] == current_game_state.self_info.x + 1:
                return actions["TAKE_WEAPON_RIGHT"]
            if md[0] == current_game_state.self_info.x - 1:
                return actions["TAKE_WEAPON_LEFT"]
            if md[1] == current_game_state.self_info.y + 1:
                return actions["TAKE_WEAPON_DOWN"]
            if md[1] == current_game_state.self_info.y - 1:
                return actions["TAKE_WEAPON_UP"]
        elif md is not None:
            self.bot_walker.x_sel = md[0]
            self.bot_walker.y_sel = md[1]
            return self.bot_walker.play_single_turn(current_game_state)
        print("E, sjebao si se")
