def confirm_quit():
    confirmation = input("Are you sure you want to quit [y/n]? ")
    if confirmation == 'y' or confirmation == 'Y':
        return 1
    else:
        return 0
