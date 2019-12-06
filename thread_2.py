# from BotKeyboard import BotKeyboard
from BotRandom import BotRandom
from BotLeft import BotLeft
import Client

# bot = BotKeyboard('http://localhost:9080', 0, 2)
Client.get("http://localhost:9080/admin/createGame?gameId=0&playerOne=1&playerTwo=2&mapName=mapConfig")
bot = BotLeft('http://localhost:9080', 0, 2)
bot.connect()

bot.game()
