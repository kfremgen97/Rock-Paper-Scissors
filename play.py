# import game
import player
import game

if __name__ == '__main__':

    # create new instances for game
    p1 = player.Person('kevin')
    p2 = player.Computer('p2')
    game = game.Game(3,p1, p2)

    # play the game
    game.play_game()
