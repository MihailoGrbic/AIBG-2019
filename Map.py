import pprint


class Map(object):
    def __init__(self, res):
        res = res['map']
        self.width = res['width']
        self.height = res['height']
        self.tiles = res['tiles']
        self.items = []
        for i in range(self.height):
            for j in range(self.width):
                if self.tiles[i][j]['item'] is not None:
                    self.items.append(self.tiles[i][j]['item'])
