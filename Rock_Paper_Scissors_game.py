import math
import random


class RPSGame:
    def __init__(self):
        """Set up the initial variables with new class is created."""
        self.valid_moves = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        self.menu()

        # Not PEP8 compliant.
        lambda_example = lambda x: math.ceil((x + 1) / 2.0)
        self.number_to_win = lambda_example(self.number_of_turns)

        self.rounds = 0
        self.p1_wins, self.p2_wins = 0.0, 0.0
        self.moves = []

        self.p1 = 'You'
        self.p2 = 'Computer'

        self.values = {'Rock': 1, 'Paper': 2, 'Scissors': 3, 'Spock': 4, 'Lizard': 5}

    def person_input(self, player_num):
        """Get player input, and run validation on it."""
        while True:
            move = raw_input("Player {0}, what's your move? ".format(player_num))
            if self.check_valid_move(move):
                return move.lower().capitalize()

    def check_valid_move(self, move):
        """Validate player move."""

        # Returns either an empty array, or an array with the move in it.
        list_of_moves = list(filter(lambda x, m=move.lower().capitalize(): x == m, self.valid_moves))

        # Check if lambda list comes back empty or with a move in it.
        if list_of_moves:
            return True

        else:
            return False

    def menu(self):
        """Initial menu, see who they want the opponent to be, and the number of turns."""
        while True:
            self.opponent = raw_input("Who would you like to play? ").lower().capitalize()

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
        """Check all combinations of win/lose"""
        self.moves.extend([p1, p2])
        self.rounds += 1
        total = self.values[p1] - self.values[p2]

        if total == 0:
            # Tied game
            print "Tie round."

        elif total in [-4, -2, 1, 3]:
            # Player 1 wins
            print "{0} won".format(self.p1)
            self.p1_wins += 1

        else:
            # Player 2 wins
            print "{0} won".format(self.p2)
            self.p2_wins += 1

    def run(self):
        """The main function that plays the game"""
        while self.p1_wins < self.number_to_win and self.p2_wins < self.number_to_win:
            first_move = self.person_input(1)
            if self.opponent == 'Person':
                self.p1 = 'Player 1'
                self.p2 = 'Player 2'
                second_move = self.person_input(2)

            else:
                second_move = random.choice(self.valid_moves)
                print "Computer chose: {0}".format(second_move)

            self.check_winner(first_move, second_move)

        # Not PEP8, but adding a new line for a single character adds nothing for readability.
        print "\n{0} won the game".format(self.p1) if self.p1_wins > self.p2_wins else "{0} won the game".format(self.p2)

        print "Number of each move:"
        print "Rock: {0}\nPaper: {1}\nScissors: {2}\nSpock: {3}\nLizard: {4}".format(self.moves.count('Rock'),
                                                                                     self.moves.count('Paper'),
                                                                                     self.moves.count('Scissors'),
                                                                                     self.moves.count('Spock'),
                                                                                     self.moves.count('Lizard'))

        print "{0} won: {1}. {2} won: {3}. Total rounds: {4}".format(self.p1,
                                                                     int(self.p1_wins),
                                                                     self.p2,
                                                                     int(self.p2_wins),
                                                                     self.rounds)


if __name__ == "__main__":
    new_game = RPSGame()
    new_game.run()
