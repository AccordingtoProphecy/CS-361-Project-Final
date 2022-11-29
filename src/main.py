import title
import how_to_play
import new_game
import random
import os

random.seed()


def main():
    while True:
        os.system('cls')
        title_input = title.title()
        if title_input == 1 and new_game.confirm_new_game():
            os.system('cls')
            new_game.new_game()
        elif title_input == 2:
            os.system('cls')
            how_to_play.how_to_play()
        elif title_input == 3 and title.confirm_quit() == 1:
            break
    os.system('cls')


if __name__ == '__main__':
    main()
