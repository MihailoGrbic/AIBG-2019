from GamePlaySingleBot import GamePlaySingleBot
from BotRandom import BotRandom
from BotBuildSwordAndAttack import BotBuildSwordAndAttack
from Client import get

gameId = 2
playerOne = 0
playerTwo = 1

gamePlay = GamePlaySingleBot('http://localhost:9080', gameId, playerTwo, BotBuildSwordAndAttack())

gamePlay.play()

