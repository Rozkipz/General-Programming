import math, random


class RPSGame:
    def __init__(self):
        self.valid_moves = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        self.menu()
        self.number_to_win = math.ceil((self.number_of_turns + 1) / 2.0)
        self.rounds = 0
        self.p1_wins, self.p2_wins = 0.0, 0.0
        self.moves = []

    def person_input(self, player_num):
        while True:
            move = raw_input("Player {0}, what's your move? ".format(player_num))
            if self.check_valid_move(move):
                return move.lower().capitalize()

    def check_valid_move(self, move):
        if move.lower().capitalize() in self.valid_moves:
            return True
        else:
            return False

    def menu(self):
        while True:
            self.opponent = raw_input("Who would you like to play? ")
            self.opponent = self.opponent.lower().capitalize()
            if self.opponent in ['Person', 'Computer']:
                break
            else:
                print "That isn't a valid opponent, please try again."

        while True:
            try:
                self.number_of_turns = int(input("How many turns would you like to play? "))
                if self.number_of_turns > 0:
                    break
                else:
                    print "That isn't a valid number of turns, please try again."
            except NameError:
                print "That isn't a number, please try again."

    def check_winner(self, p1, p2):
        # Would use a case statement here, but python doesn't have them.
        self.moves.extend([p1, p2])
        if p1 == p2:
            print "Tie round."
            return 0

        elif p1 == 'Rock':  # Rock beats Scissors, Lizard
            if p2 == 'Scissors':
                print "{0} won".format(self.p1)
                self.p1_wins += 1
            elif p2 == 'Paper':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'Spock':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'Lizard':
                print "{0} won".format(self.p1)
                self.p1_wins += 1

        elif p1 == 'Scissors':  # Scissors beats Paper, Lizard
            if p2 == 'Rock':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'Paper':
                print "{0} won".format(self.p1)
                self.p1_wins += 1
            elif p2 == 'Spock':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'Lizard':
                print "{0} won".format(self.p1)
                self.p1_wins += 1

        elif p1 == 'Paper':  # Paper beats Rock, Spock
            if p2 == 'Rock':
                print "{0} won".format(self.p1)
                self.p1_wins += 1
            elif p2 == 'Scissors':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'Spock':
                print "{0} won".format(self.p1)
                self.p1_wins += 1
            elif p2 == 'Lizard':
                print "{0} won".format(self.p2)
                self.p2_wins += 1

        elif p1 == 'Spock':  # Spock beats Rock, Scissors
            if p2 == 'Rock':
                print "{0} won".format(self.p1)
                self.p1_wins += 1
            elif p2 == 'Paper':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'Scissors':
                print "{0} won".format(self.p1)
                self.p1_wins += 1
            elif p2 == 'Lizard':
                print "{0} won".format(self.p2)
                self.p2_wins += 1

        elif p1 == 'Lizard':  # Lizard beats Spock, Paper
            if p2 == 'Rock':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'paper':
                print "{0} won".format(self.p1)
                self.p1_wins += 1
            elif p2 == 'Scissors':
                print "{0} won".format(self.p2)
                self.p2_wins += 1
            elif p2 == 'Spock':
                print "{0} won".format(self.p1)
                self.p1_wins += 1

        self.rounds += 1

    def random_move(self):
        return random.choice(self.valid_moves)

    def play(self):
        while self.p1_wins < self.number_to_win and self.p2_wins < self.number_to_win:
            first_move = self.person_input(1)
            if self.opponent == 'Person':
                self.p1 = 'Player 1'
                self.p2 = 'Player 2'
                second_move = self.person_input(2)
            else:
                self.p1 = 'You'
                self.p2 = 'Computer'
                second_move = self.random_move()
                print "Computer chose: {0}".format(second_move)
            self.check_winner(first_move, second_move)

        print "\n"
        print "{0} won the game".format(self.p1) if self.p1_wins > self.p2_wins else "{0} won the game".format(self.p2)
        print "Number of each move:"
        print "Rock: {0}\nPaper: {1}\nScissors: {2}\nSpock: {3}\nLizard: {4}".format(self.moves.count('Rock'),
                                                                                     self.moves.count('Paper'),
                                                                                     self.moves.count('Scissors'),
                                                                                     self.moves.count('Spock'),
                                                                                     self.moves.count('Lizard'))

        print "{0} won: {1}. {2} won: {3}. Total rounds: {4}".format(self.p1, int(self.p1_wins), self.p2,
                                                                     int(self.p2_wins),
                                                                     self.rounds)

    def run(self):
        self.play()


if __name__ == "__main__":
    new_game = RPSGame()
    new_game.run()
