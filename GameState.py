class GameState(object):
    def __init__(self, res):
        self.game_state = res
        self.turns_left = res['turn']
