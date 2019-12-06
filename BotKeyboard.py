from Bot import Bot

class BotKeyboard(Bot):

    def play_single_turn(self, current_game_state, current_map, self_info, other_info):
        command = input("Your move, bitch: ")
        self.doAction(command)

