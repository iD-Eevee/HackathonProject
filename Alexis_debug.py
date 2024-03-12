# Alexis A [Team Dungeon Masters]

# Player variables (replace with classes when that code's done)
player1_name = "Warbler"
player2_name = "Melinda"
player1_health = 100
player2_health = 100

# Battle Arena Start
print(player1_name + " vs. " + player2_name)
print(str(player1_health) + " vs. " + str(player2_health))

# While Loop should in theory work if classes are set up right? Check this in the final later
while player1.is_alive() and player2.is_alive():
    print(player1.name + ": " + str(player1.health))
    print(player2.name + ": " + str(player2.health))

    damage = player1.attack(player2)
    print(player1.name + " hits " + player2.name + " for " + str(damage))

    damage = player2.attack(player1)
    print(player2.name + " hits " + player1.name + " for " + str(damage))