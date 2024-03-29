import Bot
from Bot import actions, Bot
from InteligenceUtil import find_best_sword_settlement

from utils import *
import random

def find_best_building(buildings):
    pass

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

        # nx, ny = next_position(path[-1], current_map, self_info)
        # if current_map.tiles[nx][ny]["item"] is not None and current_map.tiles[nx][ny].item

class BotGrbic(Bot):
    state = 1
    
    def play_single_turn(self, current_game_state):
        current_map = current_game_state.map
        self_info = current_game_state.self_info
        other_info = current_game_state.other_info
        print(self.state)
        # Survey the area
        if self.state == 1:
            self.min_settle_pos, self.wood_pos, self.metal_pos, self.stone_pos = find_best_sword_settlement((self_info.x, self_info.y), current_map)
            self.min_settle_pos = (self.min_settle_pos[1], self.min_settle_pos[0])
            self.wood_pos = (self.wood_pos[1], self.wood_pos[0])
            self.stone_pos = (self.stone_pos[1], self.stone_pos[0])
            self.metal_pos = (self.metal_pos[1], self.metal_pos[0])

            self.state += 1

        # Goto wood
        if self.state == 2:
            path = find_path_to(self_info, current_map, self.wood_pos[0], self.wood_pos[1])
            if len(path) > 1: self.doAction(path[0])
            else: self.state += 1
                
        # Take wood
        if self.state == 3:
            print(self.wood_pos)
            path = find_path_to(self_info, current_map, self.wood_pos[0], self.wood_pos[1])
            if self_info.player_info["resources"]["WOOD"] < 4: return "tr" + path[0]
            else: self.state += 1
                
        # Goto stone
        if self.state == 4:
            path = find_path_to(self_info, current_map, self.stone_pos[0], self.stone_pos[1])
            if len(path) > 1: return path[0]
            else: self.state += 1  

        # Take stone
        if self.state == 5:
            path = find_path_to(self_info, current_map, self.stone_pos[0], self.stone_pos[1])
            if self_info.player_info["resources"]["STONE"] < 1: return "tr" + path[0]
            else: self.state += 1

        # Goto house
        if self.state == 6:
            path = find_path_to(self_info, current_map, self.min_settle_pos[0], self.min_settle_pos[1])

            if len(path) == 0: 
                path2 = find_path_to(self_info, current_map, self.stone_pos[0], self.stone_pos[1])
                for i in ['w', 'a', 's', 'd']:
                    if i != path2:
                        self.doAction(i)
                        return

            if len(path) > 1: self.doAction(path[0])
            else: 
                self.state += 1

        # Build house
        if self.state == 7:
            path = find_path_to(self_info, current_map, self.min_settle_pos[0], self.min_settle_pos[1])
            return "bh" + path[0]
            self.state += 1
            return

        # Goto stone 2
        if self.state == 8:
            path = find_path_to(self_info, current_map, self.stone_pos[0], self.stone_pos[1])
            if len(path) > 1: return path[0]
            else: self.state += 1

        # Take stone 2
        if self.state == 9:
            path = find_path_to(self_info, current_map, self.stone_pos[0], self.stone_pos[1])
            if self_info.player_info["resources"]["STONE"] < 3: return "tr" + path[0]
            else: self.state += 1

        # Goto house
        if self.state == 10:
            path = find_path_to(self_info, current_map, self.min_settle_pos[0], self.min_settle_pos[1])
            if len(path) > 1: return path[0]
            else: self.state += 1

        # Build fort
        if self.state == 11:
            path = find_path_to(self_info, current_map, self.min_settle_pos[0], self.min_settle_pos[1])
            return "bf" + path[0]
            self.state += 1
            return

        # Goto wood 2
        if self.state == 12:
            path = find_path_to(self_info, current_map, self.wood_pos[0], self.wood_pos[1])
            if len(path) > 1: return path[0]
            else: self.state += 1
                
        # Take wood 2
        if self.state == 13:
            path = find_path_to(self_info, current_map, self.wood_pos[0], self.wood_pos[1])
            if self_info.player_info["resources"]["WOOD"] < 1: return "tr" + path[0]
            else: self.state += 1

        # Goto metal
        if self.state == 14:
            path = find_path_to(self_info, current_map, self.metal_pos[0], self.metal_pos[1])
            if len(path) > 1: return path[0]
            else: self.state += 1

        # Take metal
        if self.state == 15:
            path = find_path_to(self_info, current_map, self.metal_pos[0], self.metal_pos[1])
            if self_info.player_info["resources"]["METAL"] < 3: return "tr" + path[0]
            else: self.state += 1

        # Goto fort
        if self.state == 16:
            path = find_path_to(self_info, current_map, self.min_settle_pos[0], self.min_settle_pos[1])
            if len(path) > 1: return path[0]
            else: self.state += 1

        # Upgrade fort
        if self.state == 17:
            path = find_path_to(self_info, current_map, self.min_settle_pos[0], self.min_settle_pos[1])
            return "bsf" + path[0]
            self.state += 1
            self.sword_fort_position = self.min_settle_pos


            self.state = 50
            return
        



        # Wait untill sword fort is built
        if self.state == 50:
            if current_map.tiles[self.sword_fort_position[1]][self.sword_fort_position[0]]['item'] is None: return ""
            else: self.state += 1

        # Take 2 swords
        if self.state == 51:
            path = find_path_to(self_info, current_map, self.sword_fort_position[0], self.sword_fort_position[1])
            if self_info.player_info["weapon1"] is None or self_info.player_info["weapon2"] is None:
                return "tw" + path[0]
            else:
                self.state += 1

        # READY TO KILL
        if self.state == 52:
            if self_info.player_info["weapon1"] is None or self_info.player_info["weapon2"] is None:
                self.state = 56
            elif len(other_info.player_info["buildings"]) > 0:

            play_single_turn(self, current_game_state)
            other_info.player_info["buildings"]
            
        # Goto building to kill
        if self.state == 53:
            path = find_path_to(self_info, current_map, self.enemy_building[0], self.enemy_building[1])
            if len(path) > 1: self.doAction(path[0])
            else: self.state += 1

        # Kill building
        if self.state == 54:
            path = find_path_to(self_info, current_map, self.enemy_building[0], self.enemy_building[1])
            if current_map.tiles[self.enemy_building[1]][self.enemy_building[0]]['item'] is not None and \
            current_map.tiles[self.enemy_building[1]][self.enemy_building[0]]['shop'] == False:
                self.doAction("sa" + path[0])
            else: 
                self.state = 52
                self.play_single_turn(current_game_state)
        
        # Goto player to kill
        if self.state == 55:
            path = find_path_to(self_info, current_map, other_info.y, other_info.x)
            if len(path) > 1: self.doAction(path[0])
            else: 
                state = 52
                self.doAction("sa" + path[0])

        # Goto sword fort to refill
        if self.state == 56:
            path = find_path_to(self_info, current_map, self.sword_fort_position[0], self.sword_fort_position[1])
            if len(path) > 1: self.doAction(path[0])
            else: 
                self.state = 51
                self.play_single_turn(current_game_state)

        if self.state == 90:
            return ""
        # Try to build 
        # print(current_map.tiles[self_info.x][self_info.y])
