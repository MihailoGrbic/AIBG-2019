# Bob The Builder

from Bot import Bot
from BotResourceGather import BotResourceGatherer
from GameState import GameState
from BotConstructor import BotConstructor
from Policy import Policy
from Bot import actions


class BotBuilder(Bot):

    def get_policy_list(self):
        return [
            BuildSwordFort(),
            GatherWoodForSwordFort(),
            GatherMetalForSwordFort(),
            BuildFort(),
            GatherWoodForFort(),
            GatherStoneForFort(),
            BuildHouse(),
            GatherStoneForHouse(),
            GatherWoodForHouse()
        ]

    def play_single_turn(self, current_game_state: GameState):
        return self.get_child_bot(current_game_state).play_single_turn(current_game_state)


class StarterPolicy(Policy):
    def __init__(self):
        super().__init__(BotBuilder())

    def should_execute(self, current_game_state: GameState):
        return "SWORD_FORTRESS" not in [item["itemType"] for item in
                                        current_game_state.self_info.player_info["notFinishedBuildings"] +
                                        current_game_state.self_info.player_info["buildings"]]


class BuildSwordFort(Policy):
    def __init__(self):
        super().__init__(BotConstructor("SWORD_FORTRESS"))

    def should_execute(self, current_game_state: GameState):
        return "FORTRESS" in [item["itemType"] for item in
                              current_game_state.self_info.player_info["notFinishedBuildings"] +
                              current_game_state.self_info.player_info["buildings"]] \
               and current_game_state.self_info.player_info['resources']['METAL'] >= 3 \
               and current_game_state.self_info.player_info['resources']['WOOD'] >= 1


class GatherMetalForSwordFort(Policy):
    def __init__(self):
        super().__init__(BotResourceGatherer("METAL_SHOP"))

    def should_execute(self, current_game_state: GameState):
        return "FORTRESS" in [item["itemType"] for item in
                              current_game_state.self_info.player_info["notFinishedBuildings"] +
                              current_game_state.self_info.player_info["buildings"]] \
               and (current_game_state.self_info.player_info['resources']['WOOD'] >= 1
                    and current_game_state.self_info.player_info['resources']['METAL'] < 3)


class GatherWoodForSwordFort(Policy):
    def __init__(self):
        super().__init__(BotResourceGatherer("WOOD_SHOP"))

    def should_execute(self, current_game_state: GameState):
        return "FORTRESS" in [item["itemType"] for item in
                              current_game_state.self_info.player_info["notFinishedBuildings"] +
                              current_game_state.self_info.player_info["buildings"]] \
               and current_game_state.self_info.player_info['resources']['WOOD'] < 1


class BuildFort(Policy):
    def __init__(self):
        super().__init__(BotConstructor("FORTRESS"))

    def should_execute(self, current_game_state: GameState):
        return "HOUSE" in [item["itemType"] for item in
                           current_game_state.self_info.player_info["notFinishedBuildings"] +
                           current_game_state.self_info.player_info["buildings"]] \
               and current_game_state.self_info.player_info['resources']['WOOD'] >= 2 \
               and current_game_state.self_info.player_info['resources']['STONE'] >= 3


class GatherWoodForFort(Policy):
    def __init__(self):
        super().__init__(BotResourceGatherer("WOOD_SHOP"))

    def should_execute(self, current_game_state: GameState):
        return "HOUSE" in [item["itemType"] for item in
                           current_game_state.self_info.player_info["notFinishedBuildings"] +
                           current_game_state.self_info.player_info["buildings"]] \
               and (current_game_state.self_info.player_info['resources']['WOOD'] < 2
                    and current_game_state.self_info.player_info['resources']['STONE'] == 3)


class GatherStoneForFort(Policy):
    def __init__(self):
        super().__init__(BotResourceGatherer("STONE_SHOP"))

    def should_execute(self, current_game_state: GameState):
        return "HOUSE" in [item["itemType"] for item in
                           current_game_state.self_info.player_info["notFinishedBuildings"] +
                           current_game_state.self_info.player_info["buildings"]] \
               and current_game_state.self_info.player_info['resources']['STONE'] < 3


class BuildHouse(Policy):
    def __init__(self):
        super().__init__(BotConstructor("HOUSE"))

    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.player_info['resources']['WOOD'] >= 4 \
               and current_game_state.self_info.player_info['resources']['STONE'] >= 1


class GatherStoneForHouse(Policy):
    def __init__(self):
        super().__init__(BotResourceGatherer("STONE_SHOP"))

    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.player_info['resources']['WOOD'] == 4 \
               and current_game_state.self_info.player_info['resources']['STONE'] < 1


class GatherWoodForHouse(Policy):
    def __init__(self):
        super().__init__(BotResourceGatherer("WOOD_SHOP"))

    def should_execute(self, current_game_state: GameState):
        return current_game_state.self_info.player_info['resources']['WOOD'] < 4
