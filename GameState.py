from Map import Map
from PlayerInfo import PlayerInfo


class GameState(object):
    def __init__(self, res, gameId, playerId):
        self.playerId = playerId
        self.gameId = gameId
        self.game_state = res
        self.turns_left = res['turn']
        self.map = Map(res)
        self.self_info = PlayerInfo(res, player1=res['player1']['id'] == playerId)
        self.other_info = PlayerInfo(res, player1=res['player1']['id'] != playerId)
        self.state_of_mind = {}
