# from utils import *

# Example dict:
# {'buildings': [],
#  'health': 100,
#  'id': 1,
#  'initX': 0,
#  'initY': 0,
#  'kills': 0,
#  'lives': 5,
#  'notFinishedBuildings': [],
#  'resources': {'METAL': 0, 'STONE': 0, 'WOOD': 0},
#  'score': 0,
#  'stringType': 'Player',
#  'stupidMoves': 7,
#  'weapon1': None,
#  'weapon2': None,
#  'x': 3,
#  'y': 2}


class PlayerInfo(object):
    def __init__(self, res, player1):
        # TODO (djokjulapfe): nisam siguran kako ovo player1/2 radi
        if player1:
            self.player_info = res["player1"]
        else:
            self.player_info = res["player2"]
        self.x = self.player_info['x']
        self.y = self.player_info['y']

    def get_space_left(self):
        res = self.player_info["resources"]
        return 5 - (res["WOOD"] + res["METAL"] + res["STONE"])

    def get_resource(self, resource: str):
        return self.player_info["resources"][resource]

    # def find_nearest_building(self, building_name = "SWORD_FORTRESS"):
    #     min_dist = 100000
    #     for building in self.player_info["buildings"]:
    #         if building["itemType"] == building_name:
    #             if min_dist > dist(self.x, self.y, building["x"], building["y"]):
    #                 min_dist = dist(self.x, self.y, building["x"], building["y"])
    #                 the_building = building
        
    #     if min_dist == 100000: return None, None
    #     else: return min_dist, the_building
