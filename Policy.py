from Bot import Bot
import GameState

class Policy:
    def __init__(self, bot: Bot):
        self.bot = bot

    def should_execute(self, current_game_state : GameState):
        pass

class PolicyAlwaysAllow(Policy):
    def should_execute(self, current_game_state : GameState):
        return True

class PolicyIsBeginningAndNoSwordBuilding(Policy):
    def should_execute(self, current_game_state: GameState):
        return current_game_state.turns_left > 3900 # and current_game_state.map.swordBuildings.empty

class PolicyIsEnemyCloseAndDangerous(Policy):
    def should_execute(self, current_game_state : GameState):
        return current_game_state.self_info.health < current_game_state.other_info.health
            # and len(current_game_state.other_info.weapons) == 2
