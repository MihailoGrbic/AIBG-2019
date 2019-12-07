from Bot import Bot
from BotRandom import BotRandom
from BotGrbic import BotGrbic
from Policy import *
from GamePlay import GamePlay
from BotBuildSwordAndAttack import BotBuildSwordAndAttack

class GamePlayExample(GamePlay):

    def get_policy_list(self):
        return [
            PolicyIsEnemyCloseAndDangerous(BotRandom()),
            PolicyAlwaysAllow(BotBuildSwordAndAttack()),

        ]
