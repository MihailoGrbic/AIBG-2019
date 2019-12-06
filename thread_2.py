from BotWalker import BotWalker

# bot = BotKeyboard('http://localhost:9080', 0, 2)
bot = BotWalker('http://localhost:9080', 0, 2)

bot.connect()
bot.game()
