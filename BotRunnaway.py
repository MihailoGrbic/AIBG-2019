from Bot import Bot
from Bot import actions
from GameState import GameState
import utils


def field_available(x,y,currgs):
    if (x < 0 or y < 0):
        return False

    for it in currgs.map.items:
        if(it['x']==x and it['y']==y):
            return False

    return True

class BotRunnaway(Bot):
    def __init__(self, build_type: str):
        self.build_type = build_type

    def play_single_turn(self, current_game_state: GameState):

        x2 = current_game_state.other_info.player_info['x']
        y2 = current_game_state.other_info.player_info['y']

        x1 = current_game_state.self_info.player_info['x']
        y1 = current_game_state.self_info.player_info['y']

        if(x1 - x2 < 0):

            if(field_available(x1-1,y1,current_game_state)):

                return actions['LEFT']

            elif(field_available(x1,y1-1,current_game_state)):

                return actions['UP']

            else:
                return actions['DOWN']

        if (x1 - x2 > 0):

            if (field_available(x1 + 1, y1, current_game_state)):

                return actions['RIGHT']

            elif (field_available(x1, y1 - 1, current_game_state)):

                return actions['UP']

            else:
                return actions['DOWN']

        if (y1 - y2 < 0):

            if (field_available(x1, y1 -1, current_game_state)):

                return actions['UP']

            elif (field_available(x1-1, y1, current_game_state)):

                return actions['LEFT']

            else:
                return actions['RIGHT']


        if (y2 - y1 < 0):

            if (field_available(x1, y1+1, current_game_state)):

                return actions['DOWN']

            elif (field_available(x1-1, y1, current_game_state)):

                return actions['LEFT']

            else:
                return actions['RIGHT']
