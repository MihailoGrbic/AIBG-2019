from BotRandom import BotRandom
import Client
from BotLeft import BotLeft
from BotKeyboard import BotKeyboard

Client.get("http://localhost:9080/admin/createGame?gameId=0&playerOne=1&playerTwo=2&mapName=mapConfig")
bot = BotKeyboard('http://localhost:9080', 0, 1)

bot.game()