#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: Scenario 3
from random import random

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.



#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).



#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

import random



#Party Dictionary Goes Here


partyAttackDictionary = { #Created Party Attack Dictionary
    "Greatsword" :{
        "Damage": random.randint(1,6) + random.randint(1,6) + 3
    },
    "Mace" :{
        "Damage": random.randint(1,6) + 3
    },
    "Firebolt": {
        "Damage": random.randint(1,10)
    },
    "ShortBow":{
        "Damage": random.randint(1,6) + 4
    }



}
partyDictionary = { #Imported Party Dictionary
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : (partyAttackDictionary["Greatsword"]["Damage"]),
        "Attack Modifier": 6
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : (partyAttackDictionary["Mace"]["Damage"]),
        "Attack Modifier": 3
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : (partyAttackDictionary["Firebolt"]["Damage"]),
        "Attack Modifier": 2
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : (partyAttackDictionary["ShortBow"]["Damage"]),
        "Attack Modifier": 5
    }
}


#Enemy Dictionary Goes Here
enemyWeaponDictionary = { #Created enemy attack dictionary.
    "Scimitar":{
        "Damage" : random.randint(1,6) + 2
    },
    "Claws":{
        "Damage": random.randint(1,4) + 2
    },
    "GreatClub": {
        "Damage": random.randint(1,8) + random.randint(1,8) + 8
    },
    "Bite":{
        "Damage": random.randint(1,6) + random.randint(1,6) + 3
    }

}
enemyDictionary = { #Created Enemy Dictionary
    "Goblin" :{
        "Health": 11,
        "AC": 12,
        "Damage": (enemyWeaponDictionary["Scimitar"]["Damage"]),
        "Attack Modifier": 3
    },
    "Dust Mephit" :{
        "Health": 12,
        "AC": 13,
        "Damage": (enemyWeaponDictionary["Claws"]["Damage"]),
        "Attack Modifier": 4
    },
    "Ogre" :{
        "Health": 54,
        "AC": 14,
        "Damage": (enemyWeaponDictionary["GreatClub"]["Damage"]),
        "Attack Modifier": 6
    },
    "Worg" :{
        "Health" : 22,
        "AC" : 13,
        "Damage" : (enemyWeaponDictionary["Bite"]["Damage"]),
        "Attack Modifier": 5
    }

}

#Combat Code Goes Here
party_attack_roll = (partyDictionary["LaeZel"]["Attack Modifier"]) + random.randint(1,20)

print("You rolled a", party_attack_roll)

if party_attack_roll >= (enemyDictionary["Goblin"]["AC"]):
    enemyDictionary["Goblin"]["Health"] -= partyDictionary["LaeZel"]["Damage"]
    if (enemyDictionary["Goblin"]["Health"]) <= 0:
        print("Goblin is dead!"),
        exit()
    else:
        print("Goblin is still alive!"),
else:
    print("Attack Misses!")


enemy_attack_roll = (enemyDictionary["Goblin"]["Attack Modifier"]) + random.randint(1, 20)

print("Goblin rolled a", enemy_attack_roll)

if enemy_attack_roll >= (partyDictionary["LaeZel"]["AC"]):
    partyDictionary["LaeZel"]["Health"] -= enemyDictionary["Goblin"]["Damage"]
    if (partyDictionary["LaeZel"]["Health"]) <= 0:
        print("LaeZel is dead!"),
        exit()
    else:
        print("LaeZel is still alive!")









