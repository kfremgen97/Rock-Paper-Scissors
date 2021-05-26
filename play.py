# import game
import player
import game

if __name__ == '__main__':

    # create new instances for game
    p1 = player.Computer('p1')
    p2 = player.Computer('p2')
    game = game.Game(p1, p2)

    # set the rounds
    game.rounds["total"] = 1
    # print the game intro
    game.print_game_intro()
    # play the game
    game.play_game()
    # print game recap
    game.print_game_recap()
