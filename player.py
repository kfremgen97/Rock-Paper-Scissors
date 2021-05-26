# imports
import random


# player class
class Player:

    # class variable - hold the choices the player can choose
    choices = ['rock', 'paper', 'scissors']

    # initializer
    def __init__(self, name):
        # instance variable - player name
        self.name = name
        # instance variable - hold current player choice
        self.current_move = None
        # instance variable - hold the player choices
        self.moves = []
        # instance variables - hold the opponent moves
        self.opponent_moves = []

    # choose hand choice
    def move(self):
        # do nothing, have subclasses implement
        pass

    # add the opponent move for reference
    def learn(self, opponent_move):
        # set the opponent moves
        self.opponent_moves.append(opponent_move)


# always rock
class AlwaysRock(Player):
    # initializer
    def __init__(self, player='rock'):
        # super initializer
        super().__init__(player)

    def move(self):
        # set the choice to rock
        choice = Player.choices[0]
        # set the current move
        self.current_move = choice
        # add the choice to current move list
        self.moves.append(choice)
        # return the choice
        return choice


# random player
class Random(Player):

    # initializer
    def __init__(self, player='random'):
        # super initializer
        super().__init__(player)

    # choose hand choice
    def move(self):
        # get a random choice from the lis tof available choices
        choice = random.choice(Player.choices)
        # set the current move
        self.current_move = choice
        # add the choice to current move list
        self.moves.append(choice)
        # return the choice
        return choice


# person Player
class Human(Player):

    # initializer
    def __init__(self, player):
        # super initializer
        super().__init__(player)

    # choose hand choice
    def move(self):
        # get a choice from the user input
        choice = ''

        print("")
        # Loop until user enters valid input
        while choice not in Player.choices:
            try:
                choice = input(f'{self.name} enter a choice '
                               f'({Player.choices}): ').lower()
            except Exception as e:
                print('Invalid input.')

        # set the current move
        self.current_move = choice
        # add the choice to current move list
        self.moves.append(choice)
        # return the choice
        return choice


# reflect player
class Reflect(Player):

    # initializer
    def __init__(self, player='reflect'):
        # super initializer
        super().__init__(player)

    def move(self):

        if len(self.opponent_moves) > 0:
            # get the last opponent move
            choice = self.opponent_moves[-1]
        else:
            # set it to rock
            choice = Player.choices[0]
        # set the current move
        self.current_move = choice
        # add the choice to current move list
        self.moves.append(choice)
        # return the choice
        return choice


# reflect player
class Cycle(Player):

    # initializer
    def __init__(self, player='cycle'):
        # super initializer
        super().__init__(player)

    def move(self):

        # Set the player choice
        if self.current_move == Player.choices[0]:
            choice = Player.choices[1]
        elif self.current_move == Player.choices[1]:
            choice = Player.choices[2]
        else:
            choice = Player.choices[0]

        # set the current move
        self.current_move = choice
        # add the choice to current move list
        self.moves.append(choice)
        # return the choice
        return choice
