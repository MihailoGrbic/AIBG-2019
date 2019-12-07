from Bot import Bot
from BotRandom import BotRandom
from BotGrbic import BotGrbic
from Policy import *
from GamePlay import GamePlay

class GamePlayExample(GamePlay):

    def get_policy_list(self):
        return [
            PolicyIsEnemyCloseAndDangerous(BotRandom()),
            PolicyIsBeginningAndNoSwordBuilding(BotGrbic()),
        ]
