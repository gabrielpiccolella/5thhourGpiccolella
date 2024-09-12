#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW4


# 1. Print Hello World!
print("Hello World!")

# 2. Create a dictionary with 3 keys and a value for each key.
valorantdict = {
   "player":"Kevin",
    "role":"carried",
    "agent": ["Harbor", "Yoru", "Iso"]
}

# One of the keys must have a value with a list containing

# three numbers inside.


# 3. Print one of the three numbers by itself

print(valorantdict["agent"][0])

# 4. Using the update function, add a fourth key to the dictionary

valorantdict.update({"gunPreference": "vandal"})

# and give it a value.



# 5. Print the entire dictionary

print(valorantdict)


# 6. Clear all of the data inside of the dictionary and print it.

valorantdict.clear()
print(valorantdict)

# 7. Make a nested dictionary with three entries containing the name
# of another classmate and two other pieces of information within each entry.

classMates = {
"student1": {
    "Name" : "Kevin",
    "Grade": "11th",
    "lowerClassMan": True,
},
"student2": {
    "Name" : "Ethan",
    "Grade": "12th",
    "lowerClassMan": False,
},
"student3": {
    "Name" : "Dom",
    "Grade": "12th",
    "lowerClassMan": False,
},
}







# 8. Print the names of all three classmates on the same line.

print(classMates["student1"]["Name"],classMates["student2"]["Name"],classMates["student3"]["Name"])