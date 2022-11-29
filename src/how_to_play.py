import os


def display_player_instructions():
    print('During your turn, you may choose to either attack your opponent, defend yourself until your next turn, or hold your ground.')
    print('- Attacking allows you to damage your opponent\'s health, but uses stamina and leaves you open to attack.')
    print('- Defending uses little stamina and reduces the amount of damage you can take from an opponent\'s attack, but allows them to regenerate health and stamina.')
    print('- Holding your ground uses no stamina and leaves you wide open to attack, but may cause the opponent to miss an attack entirely.\n')

    print('- You may also decide to forfeit the current duel during your turn. If you choose the option and then decide not to, you will instead hold your ground for the duration of your turn, as you hesitated.\n')


def display_opponent_instructions():
    print('When an opponent attacks, you may choose to either dodge the attack or take the hit.')
    print('- Dodging uses a lot of stamina, but has a high chance to negate all damage, with a low chance to take increased damage from the attack.')
    print('--- The chance to negate all damage is decreased after you have attacked or are defending, with the chance to take increased damage increasing.')
    print('- Taking the hit can guarantee no stamina loss, but does guarantee damage taken to health.')
    print('--- Taking the hit while defending will decrease the amount of damage taken.')
    print('An opponent may also decide to defend until their next turn, but cannot dodge when you attack them.\n')


def display_how_to_play():
    print('\nHow to play:\n')
    print('You and your opponent both begin with maximum health and stamina.')
    print('Turns alternate between you and your opponent, and each turn the respective player regenerates both health and stamina.\n')

    display_player_instructions()

    display_opponent_instructions()


def how_to_play():
    display_how_to_play()
    input('Press ENTER to return to title screen. ')
    os.system('cls')
    return 1
