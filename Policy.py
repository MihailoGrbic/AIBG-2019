from Bot import Bot


class Policy:
    def __init__(self, bot: Bot):
        self.bot = bot

    def should_execute(self, args):
        return True
