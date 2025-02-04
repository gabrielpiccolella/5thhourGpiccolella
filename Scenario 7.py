#Name:
#Class: 5th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
from SC6 import stat_roll, final_stats
stat_roll()






listAverage = 0

def final_average():
    if isinstance(final_stats, list):
        listAverage = sum(final_stats) / len(final_stats)
        return listAverage
    else:
        return "final_stats is not a list"


average = final_average()
print("here is your final average" ,average)