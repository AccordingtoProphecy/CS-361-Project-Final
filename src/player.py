import random


class Player:
    def __init__(self, health, stamina):
        self.health = health
        self.stamina = stamina

    def take_damage(self, damage):
        self.health -= damage
