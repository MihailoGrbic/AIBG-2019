class Map(object):
    def __init__(self):
        pass

    def init_from_json(self, json_dict):
        # ovde kucaj djole
        self.tiles = [[0 for i in range(25)] for j in range(25)]
        self.buildings = []

    def add_building(self, i, j):
        self.buildings += [(i,j)]
