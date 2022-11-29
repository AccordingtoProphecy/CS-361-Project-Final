import random


class Enemy:
    def __init__(self, max_health, max_stamina, name, level):
        self.max_health = max_health
        self.current_health = max_health

        self.max_stamina = max_stamina
        self.current_stamina = max_stamina

        self.defending = False

        self.name = name

        self.level = level

    def display_stats(self):
        print(self.name + ':')
        print('Health: ' + str(self.current_health) + '/' + str(self.max_health))
        print('Stamina: ' + str(self.current_stamina) +
              '/' + str(self.max_stamina))

    # GETTERS
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

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    # SETTERS for damage/health and defending state
    def take_damage(self, damage):
        self.current_health -= damage

    def toggle_defend(self, state):
        self.defending = state

    # Different levels of enemies have different damage ranges
    def get_damage(self, player):
        damage = 0
        if self.get_level() == 1:
            damage = int(random.randrange(
                int(player.get_max_health() * 0.07), int(player.get_max_health() * 0.12)))
        elif self.get_level() == 2:
            damage = int(random.randrange(
                int(player.get_max_health() * 0.06), int(player.get_max_health() * 0.16)))
        elif self.get_level() == 3:
            damage = int(random.randrange(
                int(player.get_max_health() * 0.04), int(player.get_max_health() * 0.15)))
        return damage

    # Enemies have a 5% chance to crit, 7% chance to fail, otherwise damage is normal
    def determine_crit(self, damage):
        crit = random.randint(1, 100)
        if crit >= 95:
            damage = int(damage * 1.5)
        elif crit <= 7:
            damage = int(damage * 0.5)
        return damage

    # Determines whether an attack on a holding player will hit or not
    def determine_hold_attack(self, player, damage):
        if player.get_defense_state() == True:
            damage = int(damage * 0.5)
        else:
            fail = random.randint(1, 10)
            if fail == 1:
                damage = 0
        return damage

    def attack(self, player):
        # Different level enemies have different damage ranges
        damage = self.get_damage(player)

        # Enemies have a chance to crit
        damage = self.determine_crit(damage)

        player_response = player.prompt_responses(self)

        if player_response == 'hold':
            damage = self.determine_hold_attack(player, damage)
        elif player_response == 'dodge':
            player.dodge(damage, self)
            return

        player.take_damage(damage)

    def regen_health(self):
        gain = random.randint(1, 2)

        self.current_health += gain

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def regen_stamina(self):
        gain = int(random.randrange(int(self.get_max_stamina()
                   * 0.05), int(self.get_max_stamina() * 0.1)))

        self.current_stamina += gain

        if self.current_stamina > self.max_stamina:
            self.current_stamina = self.max_stamina

    # Checks whether enemy has no stamina or not
    def check_stamina(self):
        if self.get_current_stamina() <= 0:
            return True
        return False

    def start_turn(self):
        self.regen_health()
        self.regen_stamina()
        self.toggle_defend(False)

    def turn(self, player):
        no_stamina = self.check_stamina()

        self.start_turn()

        # If enemy has no stamina, they do nothing on their turn
        if no_stamina:
            print(self.get_name() + ' takes a moment to catch their breath.\n')
            return

        action = random.randint(1, 10)

        # If enemy has stamina, they will always either attack or defend
        if action > 3:
            self.attack(player)
        else:
            self.toggle_defend(True)
            print(self.get_name() + ' raises their shield in defense.\n')

    def is_dead(self):
        if self.get_current_health() <= 0:
            return True
        return False
