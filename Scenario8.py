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
Goblin =


#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)