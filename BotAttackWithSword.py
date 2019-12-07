from Bot import Bot
from Bot import actions
from BotWalker import BotWalker
from GameState import GameState
import utils


class BotAttackWithSword(Bot):

    def __init__(self, priority_buildings = True):
        super().__init__()
        self.bot_walker = BotWalker()
        self.priority_buildings = priority_buildings

    def play_single_turn(self, current_game_state: GameState):
        if not self.priority_buildings or len(current_game_state.other_info.player_info["buildings"]) == 0:
            target = current_game_state.other_info.x, current_game_state.other_info.y
        else:
            swords = []
            forts = []
            arrows = []
            shields = []
            houses = []
            for building in current_game_state.other_info.player_info["buildings"]:
                if building["itemType"] == "SWORD_FORTRESS": swords.append(building)
                elif building["itemType"] == "FORTRESS": forts.append(building)
                elif building["itemType"] == "ARROW_FORTRESS": arrows.append(building)
                elif building["itemType"] == "SHIELD_FORTRESS": shields.append(building)
                elif building["itemType"] == "HOUSE": houses.append(building)
            
            if len(swords) > 0: target_list = swords
            elif len(forts): target_list = forts
            elif len(arrows): target_list = arrows
            elif len(shields): target_list = shields
            elif len(houses): target_list = houses
            target = utils.find_nearest((current_game_state.self_info.x, current_game_state.self_info.y), target_list)
            

        if utils.dist(current_game_state.self_info.x, current_game_state.self_info.y, target[0], target[1]) == 1:
            current_game_state.state_of_mind["TieTurns"] = 0
            if target[0] == current_game_state.self_info.x + 1:
                return actions["SWORD_RIGHT"]
            if target[0] == current_game_state.self_info.x - 1:
                return actions["SWORD_LEFT"]
            if target[1] == current_game_state.self_info.y + 1:
                return actions["SWORD_DOWN"]
            if target[1] == current_game_state.self_info.y - 1:
                return actions["SWORD_UP"]
        else:
            current_game_state.state_of_mind["TieTurns"] += 1
            if current_game_state.state_of_mind["TieTurns"] == 100:
                current_game_state.state_of_mind["Peaceful"] = True
                res = current_game_state.other_info.player_info['resources']
                current_game_state.state_of_mind["TieTurns"] = 0
                current_game_state.state_of_mind["OpponentResources"] = sum([res['STONE'], res['WOOD'], res['METAL']])


            self.bot_walker.x_sel = target[0]
            self.bot_walker.y_sel = target[1]
            return self.bot_walker.play_single_turn(current_game_state)
