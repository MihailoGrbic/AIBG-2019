import pprint

class Map(object):
    def __init__(self, res):
        res = res['map']
        self.width = res['width']
        self.height = res['height']
        self.tiles = res['tiles']

        self.items = []
        self.wood_shops = []
        self.metal_shops = []
        self.stone_shops = []
        for i in range(self.height):
            for j in range(self.width):
                if self.tiles[i][j]['item'] is not None:
                    self.items.append(self.tiles[i][j]['item'])
                    item = self.tiles[i][j]['item']
                    if item['itemType'] == 'WOOD_SHOP':
                        self.wood_shops += [(i, j)]
                    elif item['itemType'] == 'METAL_SHOP':
                        self.metal_shops += [(i, j)]
                    elif item['itemType'] == 'STONE_SHOP':
                        self.stone_shops += [(i, j)]
