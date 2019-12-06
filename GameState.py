class GameState(object):
    def __init__(self):
        self.current_turn = 0

    def inc_turn(self):
        self.current_turn += 1

    # ...