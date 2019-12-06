import Bot
from Bot import actions, Bot

from utils import dist, find_path_to#, find_path_to_nearest
import random

def is_empty(move, current_map, self_info):
    checkx, checky = next_position(move, current_map, self_info)
    return current_map.tiles[checkx][checky]['item'] is None

def next_position(move, current_map, self_info):
    if move == 'w' :
        checkx = self_info.x - 1
        checky = self_info.y 
    elif move == 'a': 
        checkx = self_info.x
        checky = self_info.y - 1
    elif move == 's' :
        checkx = self_info.x + 1
        checky = self_info.y
    elif move == 'd': 
        checkx = self_info.x
        checky = self_info.y + 1

    return checkx, checky

class BotGrbic(Bot):

    def play_single_turn(self, current_game_state, current_map, self_info, other_info):
        #print(current_map.items)

        # Take wood
        path = find_path_to_nearest(current_map, self_info, "Wood")
        while len(path) > 1: 
            path = find_path_to_nearest(current_map, self_info, "Wood")
            self.doAction(path[0])
            
        # nx, ny = next_position(path[-1], current_map, self_info)
        # if current_map.tiles[nx][ny]["item"] is not None and current_map.tiles[nx][ny].item
        
        self.doAction("tr" + path[0]), self.doAction("tr" + path[0]), self.doAction("tr" + path[0]), self.doAction("tr" + path[0])

        # Take stone
        path = find_path_to_nearest(current_map, self_info, "Stone")
        while len(path) > 1: 
            path = find_path_to_nearest(current_map, self_info, "Stone")
            self.doAction(path[0])
        self.doAction("tr" + path[-1])
        stone_dir = path[-1]

        # Build house next to stone
        path = find_path_to_nearest(current_map, self_info, "Metal")
        potential_spots = ['w', 'a', 's', 'd']
        
        for spot in potential_spots:
            if path[0] != spot:
                if is_empty(spot, current_map, self_info):
                   self.doAction("bh" + spot)
                   house_spot = next_position(spot, current_map, self_info)
                   break

        # Take stone and upgrade house to fortress
        self.doAction("tr" + stone_dir), self.doAction("tr" + stone_dir), self.doAction("tr" + stone_dir)
        self.doAction("bf" + spot)
        
        # Take metal and wood for sword fortress TODO Optimize this
        while len(path) > 1: 
            path = find_path_to_nearest(current_map, self_info, "Metal")
            self.doAction(path[0])
        self.doAction("tr" + path[-1]), self.doAction("tr" + path[-1]), self.doAction("tr" + path[-1])

        path = find_path_to_nearest(current_map, self_info, "Wood")
        while len(path) > 1: 
            path = find_path_to_nearest(current_map, self_info, "Wood")
            self.doAction(path[0])
        self.doAction("tr" + path[-1])

        # Build sword fortress
        path = find_path_to(self_info, current_map, house_spot[0], house_spot[1])
        while len(path) > 1: 
            path = find_path_to(self_info, current_map, house_spot[0], house_spot[1])
            self.doAction(path[0])
        self.doAction("bsf" + path[-1])

        print(current_map.tiles[self_info.x][self_info.y])

        # # Pickup the needed ammount
        # for item in current_map.items:
        #     if dist(item['x'], item['y'], self_info.x, self_info.y) == 1:
        #         if item['itemType'] == 'WOOD_SHOP':
        #             self.doAction(actions["UP"]), 
                

        # for i in range(len(path)): self.doAction(path[i])


        x = random.randint(0, 4)
        if x == 0:
            self.doAction(actions["UP"])
        if x == 1:
            self.doAction(actions["DOWN"])
        if x == 2:
            self.doAction(actions["LEFT"])
        if x == 3:
            self.doAction(actions["RIGHT"])