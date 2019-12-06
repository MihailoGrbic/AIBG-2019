from Client import *
import enum
import GameState
import Map
import PlayerInfo

class Action(enum.Enum):
    DOWN = "s"
    UP = "w"
    LEFT = "a"
    RIGHT = "d"
    # treba da se dodaju ostale akcije


class Bot(object):
    def __init__(self, url, gameId, playerId):
        self.url = url
        self.gameId = gameId
        self.playerId = playerId
        self.current_game_state = GameState
        self.current_map = Map
        self.self_info = PlayerInfo
        self.other_info = PlayerInfo

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.current_map.init_from_json(res['result']['map'])

    # treba da se proveri dal radi
    def doAction(self, a):
        res = get('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, a))

    def game(self):
        while True:
            # ovde fali logika da se apdejtuje gamestate i maps
            self.play_single_turn(self.current_game_state, self.current_map, self.self_info, self.other_info)

    # ovo se override-uje za taktiku
    # GameState current_game_state
    # Map current_map
    # PlayerInfo self_info
    # PlayerInfo other_info
    def play_single_turn(self, current_game_state, current_map, self_info, other_info):
        while True:
            self.doAction(Action.DOWN)
