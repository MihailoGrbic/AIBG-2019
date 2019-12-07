from Bot import Bot


class Policy:
    def __init__(self, bot: Bot):
        self.bot = bot

    def should_execute(self, current_game_state, current_map, self_info, other_info):
        return True
