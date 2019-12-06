from Client import *
from GameState import GameState
from Map import Map
from PlayerInfo import PlayerInfo

actions = {

    # moving

    "DOWN": "s",
    "UP": "w",
    "LEFT": "a",
    "RIGHT": "d",

    # taking resources

    "TAKE_DOWN": "trs",
    "TAKE_UP": "trw",
    "TAKE_LEFT": "tra",
    "TAKE_RIGHT": "trd",

    # leave resource

    "LEAVE_WOOD": "lw",
    "LEAVE_STONE": "lw",
    "LEAVE_METAL": "lw",

    # sword attack

    "SWORD_DOWN": "sas",
    "SWORD_UP": "saw",
    "SWORD_LEFT": "saa",
    "SWORD_RIGHT": "sad",

    # arrow attack

    "ARROW_DOWN": "aas",
    "ARROW_UP": "aaw",
    "ARROW_LEFT": "aaa",
    "ARROW_RIGHT": "aad"
}


class Bot(object):
    def __init__(self, url, gameId, playerId):
        self.url = url
        self.gameId = gameId
        self.playerId = playerId
        self.current_game_state = None
        self.current_map = None
        self.self_info = None
        self.other_info = None

    def update_data(self, res):
        self.current_game_state = GameState(res)
        self.current_map = Map(res)
        self.self_info = PlayerInfo(res, me=True)
        self.other_info = PlayerInfo(res, me=False)

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.update_data(res)

    # treba da se proveri dal radi
    def doAction(self, a):
        res = get('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, a))
        print('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, a))
        self.update_data(res)

    def game(self):
        while True:
            self.play_single_turn(self.current_game_state, self.current_map, self.self_info, self.other_info)

    # ovo se override-uje za taktiku
    # GameState current_game_state
    # Map current_map
    # PlayerInfo self_info
    # PlayerInfo other_info
    def play_single_turn(self, current_game_state, current_map, self_info, other_info):
        while True:
            self.doAction(actions["DOWN"])
