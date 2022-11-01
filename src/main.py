import title
from player import Player
from enemy import Enemy


def main():
    while True:
        title_input = title.title()
        if title_input == 3 and title.checking.confirm_quit() == 1:
            return


if __name__ == '__main__':
    main()
