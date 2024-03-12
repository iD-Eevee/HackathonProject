# Master Code File for Team Dungeon Masters

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

# Class Objects
player1 = Character("Warbler", 10, 100, 2)
player2 = Character("Melinda", 8, 100, 4)

# Create arena battle
print(player1.name + " vs. " + player2.name)
print(str(player1.health) + " vs. " + str(player2.health))

# Add While Loop next to check if they're alive (once class code is ready)
