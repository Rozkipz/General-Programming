import math


class RPSGame:
    def __init__(self):
        self.valid_moves = ['Rock', 'Paper', 'Scissors']
        self.menu()
        self.number_to_win = math.ceil((self.number_of_turns + 1) / 2.0)
        self.rounds = 0
        self.p1_wins, self.p2_wins = 0.0, 0.0
        self.moves = []

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

    def menu(self):
        while True:
            try:
                self.number_of_turns = int(input("How many turns would you like to play? "))
                if self.number_of_turns > 0:
                    break
                else:
                    print "That isn't a valid number of turns, please try again."
            except NameError:
                print "That isn't a valid number, please try again."

    def check_winner(self, p1, p2):
        # Would use a case statement here, but python doesn't have them.
        self.moves.extend([p1, p2])
        if p1 == p2:
            print "Tie round."
            return 0

        elif p1 == 'Rock':
            if p2 == 'Scissors':
                print "Player 1 wins"
                self.p1_wins += 1
            else:
                print "Player 2 wins"
                self.p2_wins += 1

        elif p1 == 'Scissors':
            if p2 == 'Rock':
                print "Player 2 wins"
                self.p2_wins += 1
            else:
                print "Player 1 wins"
                self.p1_wins += 1

        else:
            if p2 == 'Rock':
                print "Player 1 wins"
                self.p1_wins += 1
            else:
                print "Player 2 wins"
                self.p2_wins += 1
        self.rounds += 1

    def run(self):
        print self.number_of_turns
        print self.number_to_win
        while self.p1_wins < self.number_to_win and self.p2_wins < self.number_to_win:
            first_move = self.person_input(1)
            second_move = self.person_input(2)
            self.check_winner(first_move, second_move)
        print "\n"
        print "Player 1 wins the game" if self.p1_wins > self.p2_wins else "Player 2 wins the game"
        print "Number of each moves:"
        print "Rock: {0}\nPaper: {1}\nScissors: {2}".format(self.moves.count('Rock'), self.moves.count('Paper'), self.moves.count('Scissors'))
        print "Player 1 wins: {0} Player 2 wins: {1} Total rounds: {2}".format(int(self.p1_wins), int(self.p2_wins), self.rounds)


new_game = RPSGame()
new_game.run()
