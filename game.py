# imports
import time


# game class
class Game:

    # initializer
    def __init__(self, rounds, player1, player2):
        # instance variable - players
        self.player1 = player1
        self.player2 = player2
        # instance variables - hold the round info
        self.rounds = {
            'current': 0,
            'total': rounds,
            'winners': []
        }

    # play a round
    def play_round(self):
        # Update round
        self.rounds["current"] += 1
        # get the player choices
        self.player1.move()
        self.player2.move()
        # learn the player choices
        self.player1.learn(self.player2.current_move)
        self.player2.learn(self.player1.current_move)
        # determine winner
        self.determine_round_winner()
        # print the round info
        self.print_round_info()

    # determine round winner
    def determine_round_winner(self):
        # Get the current move from each player
        one = self.player1.current_move
        two = self.player2.current_move
        winner = 'Unknown'

        # determine winner based on move
        if one == 'rock' and two == 'paper':
            winner = self.player2.name
        elif one == 'rock' and two == 'scissors':
            winner = self.player1.name
        elif one == 'scissors' and two == 'rock':
            winner = self.player2.name
        elif one == 'scissors' and two == 'paper':
            winner = self.player1.name
        elif one == 'paper' and two == 'rock':
            winner = self.player1.name
        elif one == 'paper' and two == 'scissors':
            winner = self.player2.name
        elif one == two:
            winner = 'tie'

        # append winner to round winners list
        self.rounds['winners'].append(winner)

    # print the round info
    def print_round_info(self):
        print(f'-----Round {self.rounds["current"]}-----')
        print(f"{self.player1.name}: {self.player1.current_move}")
        print(f"{self.player2.name}: {self.player2.current_move}")
        # print the round winner based on current round
        print(f'Winner: {self.rounds["winners"][self.rounds["current"] - 1]}')

    # print the intro
    def print_game_intro(self):
        print(f'\nGame Start: {self.player1.name} vs {self.player2.name}')
        print(f'====================')

    # print the game recap
    def print_game_recap(self):
        print('\nGame Recap:')
        print(f'====================')
        # loop through the range of the rounds
        for game_round in range(self.rounds["total"]):
            # print the round and winner
            print(f'Round {game_round + 1}: '
                  f'{self.rounds["winners"][game_round]}')
            # print the player choices
            print(f'\t{self.player1.name}: {self.player1.moves[game_round]} '
                  f', {self.player2.name}: {self.player2.moves[game_round]}')

    # play the game
    def play_game(self):
        # print the intro
        self.print_game_intro()

        # play the amount of rounds
        for game_round in range(self.rounds['total']):
            # play the round
            self.play_round()

        # print the recap
        time.sleep(1)
        self.print_game_recap()
