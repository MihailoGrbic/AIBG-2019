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

    "TAKE_": "tr",
    "TAKE_DOWN": "trs",
    "TAKE_UP": "trw",
    "TAKE_LEFT": "tra",
    "TAKE_RIGHT": "trd",

    # leave resource

    "LEAVE_": "l",
    "LEAVE_WOOD": "lw",
    "LEAVE_STONE": "ls",
    "LEAVE_METAL": "lm",

    # sword attack

    "SWORD_": "sa",
    "SWORD_DOWN": "sas",
    "SWORD_UP": "saw",
    "SWORD_LEFT": "saa",
    "SWORD_RIGHT": "sad",

    # arrow attack

    "ARROW_": "aa",
    "ARROW_DOWN": "aas",
    "ARROW_UP": "aaw",
    "ARROW_LEFT": "aaa",
    "ARROW_RIGHT": "aad",

    # house

    "HOUSE_": "bh",
    "HOUSE_DOWN": "bhs",
    "HOUSE_UP": "bhw",
    "HOUSE_LEFT": "bha",
    "HOUSE_RIGHT": "bhd",

    # fort

    "FORTRESS_": "bf",
    "FORTRESS_DOWN": "bfs",
    "FORTRESS_UP": "bfw",
    "FORTRESS_LEFT": "bfa",
    "FORTRESS_RIGHT": "bfd",

    # shield fort

    "SHIELD_FORTRESS_": "bshf",
    "SHIELD_FORTRESS_DOWN": "bshfs",
    "SHIELD_FORTRESS_UP": "bshfw",
    "SHIELD_FORTRESS_LEFT": "bshfa",
    "SHIELD_FORTRESS_RIGHT": "bshfd",

    # sword fort

    "SWORD_FORTRESS_": "bsf",
    "SWORD_FORTRESS_DOWN": "bsfs",
    "SWORD_FORTRESS_UP": "bsfw",
    "SWORD_FORTRESS_LEFT": "bsfa",
    "SWORD_FORTRESS_RIGHT": "bsfd",

    # arrow fort

    "ARROW_FORTRESS_": "baf",
    "ARROW_FORTRESS_DOWN": "bafs",
    "ARROW_FORTRESS_UP": "bafw",
    "ARROW_FORTRESS_LEFT": "bafa",
    "ARROW_FORTRESS_RIGHT": "bafd",

    # drop shield

    "DROP_SHIELD": "dsh",

    # pick up your weapons and fight

    "TAKE_WEAPON_": "tw",
    "TAKE_WEAPON_DOWN": "tws",
    "TAKE_WEAPON_UP": "tww",
    "TAKE_WEAPON_LEFT": "twa",
    "TAKE_WEAPON_RIGHT": "twd"
}


class Bot(object):

    def play_single_turn(self, current_game_state: GameState):
        pass

    def get_policy_list(self):
        return list()

    def get_child_bot(self, current_game_state: GameState):
        for policy in self.get_policy_list():
            if policy.should_execute(current_game_state):
                return policy.bot
        return None
