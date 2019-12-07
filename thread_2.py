from BotWalker import BotWalker
import Client

gameId = 1
playerOne = 0
playerTwo = 1

Client.get("http://localhost:9080/admin/createGame?gameId=" + "0" +
           "&playerOne=" + "1" +
           "&playerTwo=" + "2"  +
           "&mapName=mapConfig")

# bot = BotKeyboard('http://localhost:9080', 0, 2)
bot = BotWalker('http://localhost:9080', 0, 2)

bot.connect()
bot.game()
