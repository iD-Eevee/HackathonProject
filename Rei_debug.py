# Rei (Team Dungeon Master)

# Testing using a new class... need to get the class code to test it first

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

