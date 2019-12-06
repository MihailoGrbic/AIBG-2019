class PlayerInfo(object):
    def __init__(self):
        self.x = 0
        self.y = 0

        self.lives = 5
        self.health = 100

    def dec_health(self, val):
        self.health -= val

    # ...
