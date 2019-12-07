from Client import *
from GameState import GameState
from Map import Map
from PlayerInfo import PlayerInfo
import pprint
from InteligenceUtil import *

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
    "ARROW_RIGHT": "aad",

    # house

    "HOUSE_DOWN": "bhs",
    "HOUSE_UP": "bhw",
    "HOUSE_LEFT": "bha",
    "HOUSE_RIGHT": "bhd",

    # fort

    "FORT_DOWN": "bfs",
    "FORT_UP": "bfw",
    "FORT_LEFT": "bfa",
    "FORT_RIGHT": "bfd",

    # shield fort

    "SHIELD_FORT_DOWN": "bshfs",
    "SHIELD_FORT_UP": "bshfw",
    "SHIELD_FORT_LEFT": "bshfa",
    "SHIELD_FORT_RIGHT": "bshfd",

    # sword fort

    "SWORD_FORT_DOWN": "bsfs",
    "SWORD_FORT_UP": "bsfw",
    "SWORD_FORT_LEFT": "bsfa",
    "SWORD_FORT_RIGHT": "bsfd",

    # arrow fort

    "ARROW_FORT_DOWN": "bafs",
    "ARROW_FORT_UP": "bafw",
    "ARROW_FORT_LEFT": "bafa",
    "ARROW_FORT_RIGHT": "bafd",

    # drop shield

    "DROP_SHIELD": "dsh",

    # pick up your weapons and fight

    "TAKE_WEAPON_DOWN": "tws",
    "TAKE_WEAPON_UP": "tww",
    "TAKE_WEAPON_LEFT": "twa",
    "TAKE_WEAPON_RIGHT": "twd"
}


class Bot(object):
    def __init__(self, url, gameId, playerId, random=False):
        self.url = url
        self.gameId = gameId

        self.playerId = playerId
        self.policy_list = None
        self.current_game_state = None
        self.current_map = None
        self.self_info = None
        self.other_info = None

    def get_policy_list(self):
        return self.policy_list

    def get_child_bot(self, args):
        for policy in self.policy_list:
            if policy.should_execute(args):
                return policy.bot

    def update_data(self, res):
        if not res['success']:
            print("Nesto tu nije u reeeedu!")

        res = res['result']

        self.current_game_state = GameState(res)
        self.current_map = Map(res)
        self.self_info = PlayerInfo(res, player1=res['player1']['id'] == self.playerId)
        self.other_info = PlayerInfo(res, player1=res['player1']['id'] != self.playerId)

    def connect_random(self):
        res = get(self.url + '/train/random?playerId=' + str(self.playerId))
        self.update_data(res)
        self.gameId = int(res['result']['id'])
        print("Random game id: " + str(self.gameId))

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.update_data(res)
        print(res)

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
