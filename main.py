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


# Extend a Class
class Rogue(Character):
    # attack() Method
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(0, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt


# Class Objects
player1 = Character("Warbler", 10, 100, 2)
player2 = Character("Melinda", 8, 100, 4)

# Create arena battle
print(player1.name + " vs. " + player2.name)
print(str(player1.health) + " vs. " + str(player2.health))

while player1.is_alive() and player2.is_alive():
    print(player1.name + ": " + str(player1.health))
    print(player2.name + ": " + str(player2.health))

    damage = player1.attack(player2)
    print(player1.name + " hits " + player2.name + " for " + str(damage))

    damage = player2.attack(player1)
    print(player2.name + " hits " + player1.name + " for " + str(damage))


# Declaring the winner
if player1.is_alive():
    print(player1.name + " wins!")
elif player2.is_alive():
    print(player2.name + " wins!")
else:
    print("It's a draw!")
