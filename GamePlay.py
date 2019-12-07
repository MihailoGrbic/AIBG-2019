from GameState import GameState
from Client import get


def update_peaceful(current_game_state):
    # Check if peaceful
    if current_game_state.state_of_mind["Peaceful"] == True:
        res = current_game_state.other_info.player_info['resources']
        current_res = sum([res['STONE'], res['WOOD'], res['METAL']])
        if abs(current_res - current_game_state.state_of_mind["OpponentResources"]) > 0:
            current_game_state.state_of_mind["Peaceful"] = False

    return current_game_state.state_of_mind["Peaceful"]


class GamePlay(object):
    def __init__(self, url, gameId, playerId):
        self.url = url
        self.gameId = gameId

        self.playerId = playerId
        self.current_game_state = None

        self.connect()

    def get_policy_list(self):
        return list()

    def get_child_bot(self):
        for policy in self.get_policy_list():
            if policy.should_execute(self.current_game_state):
                return policy.bot
        return None

    def doAction(self, a):
        res = get('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, a))
        print('{0}/doAction?playerId={1}&gameId={2}&action={3}'.format(
            self.url, self.playerId, self.gameId, a))
        self.update_data(res)
        ss = self.current_game_state.self_info
        print("self player " + str(ss.is_me) + " " + str(ss.x) + " " + str(ss.y))

    def play(self):
        while True:
            update_peaceful(self.current_game_state)
            action = self.get_child_bot().play_single_turn(self.current_game_state)
            self.doAction(action)

    def update_data(self, res):
        if not res['success']:
            print("Nesto tu nije u reeeedu!")

        res = res['result']

        self.current_game_state = GameState(res, self.gameId, self.playerId)

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.update_data(res)
        print(res)
