from GameState import GameState
from Client import get


def update_peaceful(current_game_state):
    # Check if peaceful
    if current_game_state.state_of_mind["Peaceful"] == True:
        res = current_game_state.other_info.player_info['resources']
        current_res = sum([res['STONE'], res['WOOD'], res['METAL']])
        # if abs(current_res - current_game_state.state_of_mind["OpponentResources"]) > 0:
        #     current_game_state.state_of_mind["Peaceful"] = False

        print("Peacefull mode: Health Diff: ", current_game_state.state_of_mind['AllSelfHealthDiff'])
        print("Peacefull mode: Last was stupid: ", current_game_state.state_of_mind['LastMoveWasStupid'])

        if not current_game_state.state_of_mind['LastMoveWasStupid'] and current_game_state.state_of_mind['AllSelfHealthDiff'] < 0:
            current_game_state.state_of_mind["Peaceful"] = False


    return current_game_state.state_of_mind["Peaceful"]

def default_state_of_mind():
    return {
        "Peaceful": False,
        "TieTurns": 0,
        "OpponentResources": 0
    }


class GamePlay(object):
    def __init__(self, url, gameId, playerId):
        self.url = url
        self.gameId = gameId

        self.playerId = playerId
        self.current_game_state: GameState = None

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
        print("self player " + str(ss.x) + " " + str(ss.y))

    def play(self):
        while True:
            update_peaceful(self.current_game_state)
            print(self.current_game_state.state_of_mind)
            action = self.get_child_bot().play_single_turn(self.current_game_state)
            self.doAction(action)

    def update_data(self, res):
        if not res['success']:
            print("Nesto tu nije u reeeedu!")

        res = res['result']

        prev_all_health = 0
        prev_stupid_moves = 0
        prev_state_of_mind = default_state_of_mind()
        if self.current_game_state is not None:
            prev_state_of_mind = self.current_game_state.state_of_mind
            prev_all_health = self.current_game_state.self_info.player_info['health'] \
                              + sum(
                [building['health'] for building in self.current_game_state.self_info.player_info['buildings']])
            prev_stupid_moves = self.current_game_state.self_info.player_info['stupidMoves']

        self.current_game_state = GameState(res, self.gameId, self.playerId)
        self.current_game_state.state_of_mind = prev_state_of_mind

        new_all_health = self.current_game_state.self_info.player_info['health'] \
            + sum([building['health'] for building in self.current_game_state.self_info.player_info['buildings']])

        next_stupid_moves = self.current_game_state.self_info.player_info['stupidMoves']

        self.current_game_state.state_of_mind['AllSelfHealthDiff'] = new_all_health - prev_all_health
        self.current_game_state.state_of_mind['LastMoveWasStupid'] = prev_stupid_moves != next_stupid_moves

    def connect(self):
        res = get(self.url + '/game/play?playerId=' + str(self.playerId) + '&gameId=' + str(self.gameId))
        self.update_data(res)
        print(res)
