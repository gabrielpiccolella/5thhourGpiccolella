#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW24

import random
import time
#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class stats:
    def __init__(self, health, damage, speed, max_health):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health
    def damage_time(self):
        for i in range(1,10):
            self.health -= random.randint(1,6)
            time.sleep(1)
            print({self.health})

    def heal_time(self):
        self.health += 30
        if self.health > 100:
            print("You have maximum health maximum health")
            self.health= 100
        else:
            print("here is the thiefs new health", self.health)
#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = stats(100,   20, 30, 100)
healer = stats(60,10,30, 60)
thief = stats( 50,  30,  40, 50)
mage = stats(45, 35, 25, 45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
gamer = random.randint(1,4)
if gamer == 1:
    warrior.damage_time()
elif gamer == 2:
    healer.damage_time()
elif gamer == 3:
    thief.damage_time()
elif gamer == 4:
    mage.damage_time()


#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.\
if warrior.health == warrior.max_health:
    print("warrior health is now at its maximum")
elif warrior.health < warrior.max_health:
    warrior.heal_time()
    print(f"Here is the warriors new health," , warrior.health)
if healer.health == healer.max_health:
    print("Healer health is now at its maximum")
elif healer.health < healer.max_health:
    healer.heal_time()
    print(f"Here is the healer new health," , healer.health)
if thief.health == thief.max_health:
    print("thief health is now at its maximum")
elif thief.health < thief.max_health:
    thief.heal_time()
    print(f"Here is the thief new health," , thief.health)
if mage.health == mage.max_health:
    print("Mage health is now at its maximum")
elif mage.health < mage.max_health:
    mage.heal_time()
    print(f"Here is the mage new health," , mage.health)




