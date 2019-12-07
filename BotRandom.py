from Bot import Bot
from Bot import actions
import random
from utils import move_available


class BotRandom(Bot):

    def play_single_turn(self, current_game_state):
        x, y = current_game_state.self_info.x, current_game_state.self_info.y

        r = random.randint(0, 3)
        if r == 0:
            if move_available(current_game_state.map, current_game_state.other_info, x, y-1):
                return actions["UP"]
            else:
                r += 1
        if r == 1:
            if move_available(current_game_state.map, current_game_state.other_info, x, y+1):
                return actions["DOWN"]
            else:
                r += 1
        if r == 2:
            if move_available(current_game_state.map, current_game_state.other_info, x-1, y):
                return actions["LEFT"]
            else:
                r += 1
        if r == 3:
            if move_available(current_game_state.map, current_game_state.other_info, x+1, y):
                return actions["RIGHT"]
            else:
                r = 0
        if r == 0:
            if move_available(current_game_state.map, current_game_state.other_info, x, y-1):
                return actions["UP"]
            else:
                r += 1
        if r == 1:
            if move_available(current_game_state.map, current_game_state.other_info, x, y+1):
                return actions["DOWN"]
            else:
                r += 1
        if r == 2:
            if move_available(current_game_state.map, current_game_state.other_info, x-1, y):
                return actions["LEFT"]
            else:
                r += 1
