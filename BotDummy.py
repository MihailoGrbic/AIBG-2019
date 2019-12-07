from Bot import Bot


class BotDummy(Bot):

    def __init__(self, type):
        self.type = type

    def play_single_turn(self, current_game_state, current_map, self_info, other_info):
        pass
