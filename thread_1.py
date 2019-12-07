from GamePlaySingleBot import GamePlaySingleBot
from BotRandom import BotRandom
from Client import get

gameId = 2
playerOne = 0
playerTwo = 1

get("http://localhost:9080/admin/createGame?gameId=" + str(gameId) +
           "&playerOne=" + str(playerOne) +
           "&playerTwo=" + str(playerTwo)  +
           "&mapName=mapConfig")

gamePlay = GamePlaySingleBot('http://localhost:9080', gameId, playerOne, BotRandom())

gamePlay.play()

