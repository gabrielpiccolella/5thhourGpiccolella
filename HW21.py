#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).

sports = {
"sport1": {
    "Name" : "basketball",
    "players": 5,
    "ball": True,
},
"sport2": {
    "Name" : "Wrestling",
    "players": 1,
    "ball": False,
},
"sport3": {
    "Name" : "jousting",
    "players": 1,
    "ball": False,
},
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def sport_pull(a,b,c):
    sum = a + b + c
    print("Total number of players for each sport is", sum)

#3. Call the function with arguments here
sport_pull(sports["sport1"]["players"], sports["sport2"]["players"], sports["sport3"]["players"])

