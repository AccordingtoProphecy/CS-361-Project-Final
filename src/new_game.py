import requests
import os
import enemy
from player import Player


# Requests a single stat block from microservice, returns JSON of response
def request_stat_block(url):
    response = requests.get(url)
    return response.json()


# Sends 3 requests to microservice website, one for each difficulty of enemy and puts them into a list, returns list
def request_stats():
    stats = []

    stats.append(request_stat_block(
        'https://cs361.moritamcvey.net/gen?difficulty=1'))
    stats.append(request_stat_block(
        'https://cs361.moritamcvey.net/gen?difficulty=2'))
    stats.append(request_stat_block(
        'https://cs361.moritamcvey.net/gen?difficulty=3'))

    return stats


# Grabs stats from a JSON object and returns an enemy with those stats
def enemy_setup(stats_json):
    health = stats_json['health']
    stamina = stats_json['stamina']
    name = stats_json['name']
    level = stats_json['difficulty']
    return enemy.Enemy(health, stamina, name, level)


# Takes stats array and returns array of 3 opponents with respective stats
def opponents_list(enemy_stats):
    opponents = []

    opponent_1 = enemy_setup(enemy_stats[0])
    opponent_2 = enemy_setup(enemy_stats[1])
    opponent_3 = enemy_setup(enemy_stats[2])

    opponents.append(opponent_1)
    opponents.append(opponent_2)
    opponents.append(opponent_3)

    return opponents


# Plays a single round, beginning with the player's turn and alternating until someone dies
def game(player, enemy):
    print('\nYou face ' + enemy.get_name() + ' in battle. Prepare to fight!\n')
    player.reset_stats()

    while True:
        player.turn(enemy)

        if enemy.is_dead():
            return True
        elif player.is_dead():
            return False

        enemy.turn(player)

        if player.is_dead():
            return False
        elif enemy.is_dead():
            return True


def lose_round(player):
    if player.get_forfeit():
        input(player.get_name() +
              ' forfeits!\nPress ENTER to continue. ')
    else:
        input(player.get_name() + ' fell in battle...\nPress ENTER to continue. ')


def win_round(player, enemy):
    input(enemy.get_name() + ' fell in battle, and ' +
          player.get_name() + ' is victorious!\nPress ENTER to continue. ')


def show_score(score, num_rounds):
    os.system('cls')
    input('You won ' + str(score) + ' out of ' +
          str(num_rounds) + ' duels.\nPress ENTER to continue. ')


# Determines the outcome of a game and returns number to add to score based on win or lose
def determine_outcome(player, enemy):
    os.system('cls')

    fail = game(player, enemy)
    if fail == False:
        lose_round(player)
        return 0
    else:
        win_round(player, enemy)
        return 1


# Play 3 games and return the score
def play_games(player, enemy_list):
    score = 0
    score += determine_outcome(player, enemy_list[0])
    score += determine_outcome(player, enemy_list[1])
    score += determine_outcome(player, enemy_list[2])
    return score


# Gets player input for name, creates 3 opponents, then plays 3 games, and then shows the score
def new_game():
    num_rounds = 3
    name = input('\nWhat do you call yourself, traveler? ')
    player = Player(100, 100, name)

    enemy_stats = request_stats()
    opponents = opponents_list(enemy_stats)

    score = play_games(player, opponents)

    show_score(score, num_rounds)


def confirm_new_game():
    choice = input('Are you sure you want to start a new game [y/n]? ')
    if choice == 'y' or choice == 'Y':
        return True
    else:
        return False
