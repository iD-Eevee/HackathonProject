# Sammy K's Debug File

# Character Class
class Character:
    # Constructor
    def __init__(self, name, strength, health, defense):
        self.name = name
        self.strength = strength
        self.health = health
        self.defense = defense

    # take_damage() Method
    def take_damage(self, damage):
        damage_taken = damage - self.defense
        self.health -= damage_taken
        return damage_taken

    # attack() Method
    def attack(self, target):
        damage = self.strength * 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt

    # is_alive() Method
    def is_alive(self):
        return self.health > 0