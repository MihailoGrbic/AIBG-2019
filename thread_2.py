from GamePlaySingleBot import GamePlaySingleBot
from BotRandom import BotRandom
from BotBuilder import BotBuilder
from BotBuildSwordAndAttack import BotBuildSwordAndAttack
from BotBuildSwordAndAttackStupidEnemy import BotBuildSwordAndAttackStupidEnemy
from BotBuildSwordAndAttackWithRunaway import BotBuildSwordAndAttackWithRunaway
from Client import get

gameId = 0
playerOne = 0
playerTwo = 1

gamePlay = GamePlaySingleBot('http://localhost:9080', gameId, playerTwo, BotBuildSwordAndAttackWithRunaway(500))

gamePlay.play()

