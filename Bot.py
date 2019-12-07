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

    def play_single_turn(self, current_game_state : GameState):
        pass
