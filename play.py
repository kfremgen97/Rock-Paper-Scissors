# import game
import player
import game

if __name__ == '__main__':

    print("Welcome to Rock,Paper,Scissors")
    print('Before we start, we need some information')

    # get the player 1 name
    p1_name = input('Enter your name: ').strip()

    # initialize players
    p1 = player.Person(p1_name)
    p2 = player.Computer('p2')
    rounds = 0

    # Get the amount of rounds for the game
    while rounds not in range(1,21):
        try:
            rounds = int(input('Enter the amount of rounds for the game(1-20): '))
        except Exception as e:
            print('Invalid input')

    # initialize game
    game = game.Game(rounds,p1, p2)

    # play the game
    game.play_game()
