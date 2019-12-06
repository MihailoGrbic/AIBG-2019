import requests

def get(url):
    r = requests.get(url)
    res = r.json()
    return res

player1Actions = []
player2Actions = []


for i in range(0, 200):
    player1Actions.append('d')
    player1Actions.append('d')
    player1Actions.append('d')
    player1Actions.append('a')
    player1Actions.append('a')
    player1Actions.append('a')

for i in range(0, 200):
    player2Actions.append('a')
    player2Actions.append('a')
    player2Actions.append('a')
    player2Actions.append('d')
    player2Actions.append('d')
    player2Actions.append('d')

class Bot:
    def __init__(self, url, playerId, gameId):
        self.url = url
        self.playerId = playerId
        self.gameId = gameId

    def join(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        print(res)

    def doAction(self, str):
        res = get('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, str))
        print(res)

gameId = 10
playerId = 2
Bot1 = Bot("http://localhost:9080", playerId, gameId)

Bot1.join()

if playerId == 1:
    for action in player1Actions:
        Bot1.doAction(action)
else:
    for action in player1Actions:
        Bot1.doAction(action)