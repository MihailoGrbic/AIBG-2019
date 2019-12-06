import requests
import pprint as pp
import numpy as np
import smartreq
import random as rnd

url = 'http://localhost:9080'


def get(url):
    r = requests.get(url)
    res = r.json()
    return res


class Communicator:
    action_map = {
        0: "w",
        1: "s",
        2: "a",
        3: "d",
        4: "mw",
        5: "mf",
        6: "mg",
        7: "mn",
        8: "rw",
        9: "rs",
        10: "ra",
        11: "rd",
    }

    infty = 1000000

    def __init__(self, playerId):
        self.playerId = playerId
        self.last_morph_counter = 0

    def create_game(self):
        res = get(url + '/train/random?playerId=' + str(self.playerId))
        self.game_state = smartreq.SmartReq(res)
        # TODO: use self.game_state for the stuff below
        # pp.pprint(res)
        self.game = res['result']
        self.gameId = self.game['id']
        # print("Player " + str(self.playerId) + " created a game with gameId: " + str(self.gameId))

    def join_game(self):
        res = get(url + '/train/random?playerId=' + str(self.playerId))
        self.game = res['result']
        self.gameId = self.game['id']
        res = get(url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.game_state = smartreq.SmartReq(res)
        # TODO: use self.game_state for the stuff below
        self.game = res['result']
        self.gameId = self.game['id']
        # print("Player " + str(self.playerId) + " joined a game with gameId: " + str(self.gameId))

    def do_action(self, action_vector, bypass_sanity_check=False):
        # TODO: add sanity check
        self.last_morph_counter -= 1
        if not bypass_sanity_check:
            current_player = self.game_state.get_current_player()
            px = current_player['x']
            py = current_player['y']

            # Check if hitting the wall
            if py - 1 >= 0 and self.game_state.map_items[py - 1][px] == 4:
                action_vector[0] = -self.infty
            if py + 1 < self.game_state.map_height and self.game_state.map_items[py + 1][px] == 4:
                action_vector[1] = -self.infty
            if px - 1 >= 0 and self.game_state.map_items[py][px - 1] == 4:
                action_vector[2] = -self.infty
            if px + 1 < self.game_state.map_width and self.game_state.map_items[py][px + 1] == 4:
                action_vector[3] = -self.infty

            # Check if one can morph
            if self.last_morph_counter > 0:
                action_vector[4] = -self.infty
                action_vector[5] = -self.infty
                action_vector[6] = -self.infty
                action_vector[7] = -self.infty
            if "WATER" not in current_player['morphItems']:
                action_vector[4] = -self.infty
            if "FIRE" not in current_player['morphItems']:
                action_vector[5] = -self.infty
            if "GRASS" not in current_player['morphItems']:
                action_vector[6] = -self.infty

            # Check if one can shoot
            if current_player['type'] == 'NEUTRAL':
                action_vector[8] = -self.infty
                action_vector[9] = -self.infty
                action_vector[10] = -self.infty
                action_vector[11] = -self.infty

        action_index = np.argmax(action_vector)
        if action_index in [4, 5, 6, 7]:
            self.last_morph_counter = 7
        self.game_state = get(
            url + '/doAction?playerId=' + str(self.playerId) + '&gameId=' + str(self.game['id']) + '&action=' +
            self.action_map[action_index])
        self.game_state = smartreq.SmartReq(self.game_state)
        return self.game_state

down_action = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
right_action = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
up_action = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
left_action = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# player = Communicator(int(input("Enter Player ID: ")))
# if input("Are you host?: ").lower()[0] == 'y':
#     player.create_game()
# else:
#     player.join_game()
#
# action_map = {
#     ',': up_action,
#     'o': down_action,
#     'a': left_action,
#     'e': right_action
# }
#
# while True:
#     player.do_action(action_map[input("Next Action:")])
#
# import threading
# import time
#
# def player1():
#     P = Communicator(1)
#     P.create_game()
#     print(P.gameId)
#     while True:
#         P.do_action(np.array([rnd.random(), rnd.random(), rnd.random(), rnd.random(), 0, 0, 0, 0, 0, 0, 0, 0]))
#         time.sleep(0.1)
#
#
# def player2():
#     P = Communicator(2)
#     P.join_game()
#     while True:
#         P.do_action(np.array([rnd.random(), rnd.random(), rnd.random(), rnd.random(), 0, 0, 0, 0, 0, 0, 0, 0]))
#         time.sleep(0.1)
#
#
# class myThread(threading.Thread):
#
#     def __init__(self, pid):
#         threading.Thread.__init__(self)
#         self.pid = pid
#
#     def run(self):
#         if self.pid == 1:
#             player1()
#         else:
#             player2()
#
#
# T1 = myThread(1)
# T2 = myThread(2)
# T1.start()
# T2.start()
