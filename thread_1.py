from BotRandom import BotRandom
import Client
from BotLeft import BotLeft
from BotKeyboard import BotKeyboard
from BotGrbic import BotGrbic

#Client.get("http://localhost:9080/admin/createGame?gameId=0&playerOne=1&playerTwo=2&mapName=mapConfig")
bot = BotGrbic('http://localhost:9080', 0, 1)
bot.connect()

bot.game()
