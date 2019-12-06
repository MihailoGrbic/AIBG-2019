from BotRandom import BotRandom
import Client
from BotLeft import BotLeft
from BotKeyboard import BotKeyboard
from BotGrbic import BotGrbic

gameId = 4
playerOne = 0
playerTwo = 1

Client.get("http://localhost:9080/admin/createGame?gameId=" + str(gameId) +
           "&playerOne=" + str(playerOne) +
           "&playerTwo=" + str(playerTwo) +
           "&mapName=mapConfig")
bot = BotRandom('http://localhost:9080', gameId, playerOne)

bot.game()
