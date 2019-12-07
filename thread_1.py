from GamePlaySingleBot import GamePlaySingleBot
from BotRandom import BotRandom

gamePlay = GamePlaySingleBot('http://localhost:9080', 2, 1, BotRandom())

gamePlay.play()
