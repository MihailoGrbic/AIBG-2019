import Map
import PlayerInfo
from utils import *

def find_best_sword_settlement(start_pos: tuple, map: Map):

    settle_costs = [[-1 for i in range(map.width)] for j in range(map.height)]
    min_settle_pos = None
    wood_metal_stone_pos = None

    nearest_stones_map = nearest_to_map((map.height, map.width), map.stone_shops)
    for x in range(map.height):
        for y in range(map.width):
            if map.tiles[x][y]["item"] is not None:
                continue

            settle_pos = (x,y)
            stone_pos = nearest_stones_map[x][y]

            nearest_wood_dist = None
            wood_pos = None
            for wood in map.wood_shops:
                curr_dist = 0
                curr_dist += dist(*start_pos, *wood)
                curr_dist += dist(*wood, *stone_pos)
                curr_dist += dist(*settle_pos, *wood)
                if wood_pos is None or curr_dist < nearest_wood_dist:
                    nearest_wood_dist = curr_dist
                    wood_pos = wood

            nearest_metal_dist = None
            metal_pos = None
            for metal in map.metal_shops:
                curr_dist = 0
                curr_dist += dist(*wood_pos, *metal)
                curr_dist += dist(*metal, *settle_pos)
                if metal_pos is None or curr_dist < nearest_metal_dist:
                    nearest_metal_dist = curr_dist
                    metal_pos = metal

            settle_cost = 0
            settle_cost += dist(*start_pos, *wood_pos)
            settle_cost += dist(*wood_pos, *stone_pos)
            settle_cost += 3 * dist(*stone_pos, *settle_pos)
            settle_cost += dist(*settle_pos, *wood_pos)
            settle_cost += dist(*wood_pos, *metal_pos)
            settle_cost += dist(*metal_pos, *settle_pos)

            settle_costs[settle_pos[0]][settle_pos[1]] = settle_cost

            if min_settle_pos is None or settle_cost < settle_costs[min_settle_pos[0]][min_settle_pos[1]]:
                min_settle_pos = settle_pos
                wood_metal_stone_pos = (wood_pos, metal_pos, stone_pos)

    return (min_settle_pos, *wood_metal_stone_pos)




