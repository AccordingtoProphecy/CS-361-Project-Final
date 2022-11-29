import random


class Player:
    def __init__(self, max_health, max_stamina, name):
        self.max_health = max_health
        self.current_health = max_health

        self.max_stamina = max_stamina
        self.current_stamina = max_stamina

        self.defending = False
        self.attacking = False

        self.forfeit = False

        self.name = name

    def display_stats(self):
        print(self.name + ':')
        print('Health: ' + str(self.current_health) + '/' + str(self.max_health))
        print('Stamina: ' + str(self.current_stamina) +
              '/' + str(self.max_stamina))

    # GETTERS for stats
    def get_max_health(self):
        return self.max_health

    def get_current_health(self):
        return self.current_health

    def get_max_stamina(self):
        return self.max_stamina

    def get_current_stamina(self):
        return self.current_stamina

    def get_defense_state(self):
        return self.defending

    def get_attack_state(self):
        return self.attacking

    def get_forfeit(self):
        return self.forfeit

    def get_name(self):
        return self.name

    def reset_stats(self):
        self.current_health = self.max_health
        self.current_stamina = self.max_stamina

    def toggle_defend(self, state):
        if state == True:
            self.lose_stamina('defend')
            print('You raise your shield in defense, preparing for the next attack.\n')
        self.defending = state

    def toggle_attack(self, state):
        self.attacking = state

    def take_damage(self, damage):
        self.current_health -= int(damage)

    def take_crit_damage(self, damage):
        damage = int(damage * 1.5)
        self.take_damage(int(damage))
        return 1

    # Player loses stamina based on different actions they take
    def lose_stamina(self, action):
        if action == 'attack':
            stamina_loss = random.randrange(
                int(self.get_max_stamina() * 0.15), int(self.get_max_stamina() * 0.22))
        elif action == 'defend':
            stamina_loss = random.randrange(
                int(self.get_max_stamina() * 0.06), int(self.get_max_stamina() * 0.1))
        elif action == 'dodge':
            stamina_loss = random.randrange(
                int(self.get_max_stamina() * 0.13), int(self.get_max_stamina() * 0.28))
        self.current_stamina -= stamina_loss

    # Displays different attack messages depending on if player normally attacks, deals crit damage, or crit fails
    def display_crit(self, crit, damage, enemy):
        if crit == 0:
            print('You attack ' + enemy.get_name() +
                  ' for ' + str(damage) + ' damage.\n')
        elif crit == 1:
            print(
                'Your weapon seeks its target with ease, striking ' + enemy.get_name() + ' for ' + str(int(damage)) + ' damage.\n')
        elif crit == -1:
            print(
                'Your weapon nearly misses, grazing ' + enemy.get_name() + ' for ' + str(int(damage)) + ' damage.\n')

    def attack(self, enemy):
        crit_success = 0
        damage = int(random.randrange(
            int(enemy.get_max_health() * 0.05), int(enemy.get_max_health() * 0.2)))

        # 20% chance to deal 1.5 times the damage, 10% to deal half damage
        crit = random.randint(1, 10)
        if crit == 10:
            crit_success = 1
            damage = int(damage * 1.5)
        elif crit == 1:
            crit_success = -1
            damage = int(damage * 0.5)

        # If enemy is blocking, they take half damage
        if enemy.get_defense_state() == True:
            damage = int(damage * 0.5)

        self.lose_stamina('attack')
        enemy.take_damage(damage)
        self.toggle_attack(True)
        self.display_crit(crit_success, damage, enemy)

    def print_dodge(self, crit, enemy):
        if crit == 0:
            print('You dodge ' + enemy.get_name() + '\'s swing with ease.\n')
        elif crit == 1:
            print(
                'You trip, allowing ' + enemy.get_name() + '\'s blow to magnify in power as it hits you.\n')

    def dodge(self, damage, enemy):
        self.lose_stamina('dodge')

        # If player recently attacked or defended, dodging becomes harder
        fail = False
        if self.get_attack_state() or self.get_defense_state():
            fail = True

        crit = 0

        dodge_chance = random.randint(1, 100)

        if fail == False:
            if dodge_chance < 10:
                crit = self.take_crit_damage(damage)
        else:
            if dodge_chance < 15:
                crit = self.take_crit_damage(damage)

        self.print_dodge(crit, enemy)

    # Regens between 2% and 4% of total health
    def regen_health(self):
        gain = random.randint(1, 4)

        self.current_health += gain

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    # Regens a round amount of stamina, between 8% and 20% of total
    def regen_stamina(self):
        gain = int(random.randrange(int(self.max_stamina * 0.08),
                                    int(self.max_stamina * 0.2)))

        self.current_stamina += gain

        if self.current_stamina > self.max_stamina:
            self.current_stamina = self.max_stamina

    def print_options(self):
        print('\nYour turn begins')
        print('1. Attack')
        print('2. Defend')
        print('3. Hold')
        print('4. Forfeit')

    # Prompts options for the start of the player turn
    def prompt_options(self):
        self.print_options()

        choice = input('\nWhat action would you like to take? ')

        choices = ['attack', 'defend', 'hold', 'forfeit']

        while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choices.count(choice.lower() == 0):
            print('Invalid input')
            choice = input('\nWhat action would you like to take? ')

        print('')

        if choice == '1' or choice.lower() == 'attack':
            return 1
        elif choice == '2' or choice.lower() == 'defend':
            return 2
        elif choice == '3' or choice.lower() == 'hold':
            return 3
        elif choice == '4' or choice.lower() == 'forfeit':
            forfeit_choice = input(
                'Are you sure you want to forfeit the duel [y/n]? ')
            if forfeit_choice == 'y' or forfeit_choice == 'Y':
                return 4
            else:
                return 3

    def check_stamina(self):
        if self.current_stamina <= 0:
            self.current_stamina = 0
            return True
        return False

    def print_hold_options(self):
        if self.get_defense_state() == True:
            print('2. Hold (defend)')
        else:
            print('2. Hold')

    def response_option(self, choice):
        if choice == '1':
            return 'dodge'
        else:
            return 'hold'

    # Prompts responses to an enemy attack
    def prompt_responses(self, enemy):
        print(enemy.get_name() + ' attacks.\n')

        no_stamina = self.check_stamina()

        # If player has no stamina, they cannot dodge and must hold
        if no_stamina:
            print('But alas, your legs fail you.\n')
            return 'hold'

        print('1. Dodge')
        self.print_hold_options()

        choice = input('\nHow would you like to respond? ')
        print('')
        return self.response_option(choice)

    def start_turn(self):
        self.regen_health()
        self.regen_stamina()
        self.toggle_defend(False)
        self.toggle_attack(False)
        self.display_stats()

    def turn_option(self, choice, enemy):
        if choice == 1:
            self.attack(enemy)
            return 'attack'
        elif choice == 2:
            self.toggle_defend(True)
            return 'defend'
        elif choice == 4:
            self.current_health = 0
            self.forfeit = True
            return 'forfeit'
        else:
            return 'hold'

    def turn(self, enemy):
        self.start_turn()

        no_stamina = self.check_stamina()

        if no_stamina:
            print('\nYour hand trembles, too weak to hold your blade.\n')
            return 'hold'

        choice = self.prompt_options()

        return self.turn_option(choice, enemy)

    def is_dead(self):
        if self.get_current_health() <= 0:
            return True
        return False
