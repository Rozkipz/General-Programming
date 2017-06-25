class RPSGame():
    def __init__(self):
        self.valid_moves = ['Rock', 'Paper', 'Scissors']

    def person_input(self, player_num):
        while True:
            move = raw_input("Player {0} What's your move? ".format(player_num))
            if self.check_valid_move(move):
                return move.lower().capitalize()

    def check_valid_move(self, move):
        if move.lower().capitalize() in self.valid_moves:
            return True
        else:
            return False

    def run(self):
        first_move = self.person_input(1)
        print first_move
        second_move = self.person_input(2)
        print second_move

new_game = RPSGame()
new_game.run()
