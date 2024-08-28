#Name Gabriel Piccolella
#Class 5th Hour
#Assignment HW3

#Print Hello World!
print("Hello World!")

#Create a list with 5 strings containing 5 different names in it
nameList = ["Kevin", "Grayson", "Nate", "Gabriel", "Allen"]
print(f"{nameList [1]}")

#Append a new name onto the Name List
nameList.append(input())
#Print out the 4th name on the list
print(f"{nameList[4]}")

#Create a list with 4 different integers in it
numList = [6, 3, 9, 12]
#Insert a new integer into the 2nd spot
numList.insert(1, 3)
#Print the Integer List
print(numList)
#Sort the list from lowest to highest
numList.sort()
print(numList)
#Add the 1st three numbers on the sorted list together
sum = numList[0] + numList[1] + numList[2]
#Print the sum
print(sum)