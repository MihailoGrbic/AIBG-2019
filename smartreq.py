"""
A class for handling requests.
"""
import numpy as np


class SmartReq:
    """
    Class for parsing request, call constructor on the json from get().
        Field item mapping: (None/0)(WATER/1)(FIRE/2)(GRASS/3)(OBSTACLE/4)
        Field type mapping: (NORMAL/0)(WATER/1)(FIRE/2)(GRASS/3)

    """

    def __init__(self, dict):

        self.map_height = int(dict['result']['map']['height'])
        self.map_width = int(dict['result']['map']['width'] / 2)


        raw_map = dict['result']['map']['tiles']

        self.map_items = np.zeros(shape=[self.map_height, self.map_width], dtype=np.int16)
        self.map_types = np.zeros(shape=[self.map_height, self.map_width], dtype=np.int16)

        for x in range(self.map_height):
            for y in range(self.map_width):
                if (raw_map[x][y]['item'] == None):
                    self.map_items[x][y] = 0
                elif (raw_map[x][y]['item'] == 'WATER'):
                    self.map_items[x][y] = 1
                elif (raw_map[x][y]['item'] == 'FIRE'):
                    self.map_items[x][y] = 2
                elif (raw_map[x][y]['item'] == 'GRASS'):
                    self.map_items[x][y] = 3
                else:
                    self.map_items[x][y] = 4

                if (raw_map[x][y]['type'] == 'NORMAL'):
                    self.map_types[x][y] = 0
                elif (raw_map[x][y]['type'] == 'WATER'):
                    self.map_types[x][y] = 1
                elif (raw_map[x][y]['type'] == 'FIRE'):
                    self.map_types[x][y] = 2
                else:
                    self.map_types[x][y] = 3

        self.turn = dict['result']['turn']
        self.winner = dict['result']['winner']
        self.succes = dict['success']

        self.player1 = dict['result']['player1']
        self.player2 = dict['result']['player2']

        self.next_player = None

        if ((self.player1['x'] == dict['result']['nextPlayer']['x']) and (
                self.player1['y'] == dict['result']['nextPlayer']['y'])):
            self.next_player = 1
        else:
            self.next_player = 2

        self.player_index = dict['playerIndex']
        self.Id = dict['result']['id']

    def get_current_player(self):
        if self.player_index == 1:
            return self.player1
        else:
            return self.player2

    def get_next_player(self):
        if self.player_index == 1:
            return self.player2
        else:
            return self.player1