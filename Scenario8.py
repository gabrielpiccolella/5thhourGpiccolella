#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

class stats:
    def __init__(self, health, ac, damage, attack_mod):
        self.health = health
        self.ac = ac
        self.damage = damage
        self.attack_mod = attack_mod

"party"
LaeZel = stats(12, 17, (random.randint(1,6) + random.randint(1,6)  + 3), 6 )
Shadowheart = stats(10, 14, (random.randint(1,6) + 3), 3 )
Gale = stats(8, 14, (random.randint(1,10)), 2 )
Astarion = stats(10, 14, (random.randint(1,6) + 4), 5 )

"enemys"
Goblin = stats(11, 12, (random.randint(1,6) + 2), 3)
Dust_Mephit = stats(12,13, (random.randint(1,4) + 2), 4)
Ogre = stats(12,13, (random.randint(1,8) + random.randint(1,8) + 8), 4)
Worg = stats(12,13, (random.randint(1,6) + random.randint(1,6) + 3), 4)

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

party_attack_roll = (LaeZel.attack_mod) + random.randint(1,20)

print("You rolled a", party_attack_roll)

if party_attack_roll >= (Goblin.ac):
    Goblin.health -= LaeZel.damage
    if Goblin.health <= 0:
        print("Goblin is dead!"),
        exit()
    else:
        print("Goblin is still alive!"),
else:
    print("Attack Misses!")


enemy_attack_roll = Goblin.attack_mod + random.randint(1, 20)

print("Goblin rolled a", enemy_attack_roll)

if enemy_attack_roll >= LaeZel.ac:
    LaeZel.health -= Goblin.damage
    if LaeZel.health <= 0:
        print("LaeZel is dead!"),
        exit()
    else:
        print("LaeZel is still alive!")
