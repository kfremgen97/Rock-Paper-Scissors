# imports
import random


# player class
class Player:

    # class variable - hold the choices the player can choose
    choices = ['rock','paper','scissors']

    # initializer
    def __init__(self, name):
        # instance variable - player name
        self.name = name
        # instance variable - hold current player choice
        self.current_move = None  # Hold the value of none since game did not start yet
        # instance variable - hold the player choices
        self.moves = []

    # choose hand choice
    def move(self):
        # do nothing, have subclasses implement
        pass


# computer player
class Computer(Player):

    # initializer
    def __init__(self, player='computer'):
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
class Person(Player):
    pass