import time


def display_title():
    print("\nWelcome to the game!\n")
    time.sleep(0.1)
    print("1. New Game")
    time.sleep(0.1)
    print("2. How to Play")
    time.sleep(0.1)
    print("3. Quit\n")


def title():
    display_title()
    while True:
        title_choice = input("What would you like to do? ")
        if title_choice == '1':
            print("Starting new game")
            return 1
        elif title_choice == '2':
            print("Showing you how to play the game")
            return 2
        elif title_choice == '3':
            return 3
        else:
            print("Invalid input")
            return 4
