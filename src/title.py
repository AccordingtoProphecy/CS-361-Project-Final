import os


def display_title():
    print('\nWelcome to DUEL!\n')
    print('1. New Game')
    print('2. How to Play')
    print('3. Quit\n')


def confirm_quit():
    confirmation = input('Are you sure you want to quit [y/n]? ')
    if confirmation == 'y' or confirmation == 'Y':
        return 1
    else:
        return 0


def title():
    display_title()
    while True:
        title_choice = input('What would you like to do? ')
        if title_choice == '1':
            return 1
        elif title_choice == '2':
            return 2
        elif title_choice == '3':
            return 3
        else:
            os.system('cls')
            return 4
