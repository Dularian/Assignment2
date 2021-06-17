import pandas as pan


data = pan.DataFrame({'Alabama': [75, 65, 77, 52, 55, 76], 'Tennessee': [55, 65, 75, 85, 79, 71],
                        'Florida': [65,88, 92, 95, 93, 91], 'Arizona': [88, 87, 92, 97, 91, 94],
                        'Georgia': [56, 65, 56, 82, 71, 72]})
data.set_index([["Day1", "Day2", "Day3", "Day4", "Day5", "Day6"]], inplace=True)
print(data,"\n")

"""gathers the Tennessee column and prints it."""
print("Tennessee:")
tennessee = data['Tennessee']
print(tennessee,"\n")

"""gathers the Day3 row and prints it."""
print("Day 3:")
day3_temps = data.iloc[2, 0:5]
print(day3_temps,"\n")

"""gathers the Day2 row and prints it."""
print("Day 2:")
day2_temps = data.iloc[1, 0:5]
print(day2_temps,"\n")

"""gathers the Day4 row and prints it."""
print("Day 4:")
day4_temps = data.iloc[3, 0:5]
print(day4_temps,"\n")

"""prints the Florida column"""
print("Florida:")
florida = data['Florida']
print(florida,"\n")

"""prints the Georgia column"""
print("Georgia:")
georgia = data['Georgia']
print(georgia,"\n")

"""gathers specific days of an area by row and column and prints the result"""
day2_temps = data.iloc[1, 2]
day2_temps1 = data.iloc[1,1]
print("Florida temp on Day 2 is: ", day2_temps)
print("Tennessee temp on Day 2 is: ", day2_temps1,"\n")
day5_temps = data.iloc[4, 1]
day5_temps1 = data.iloc[4, 2]
print("Tennessee temp on Day 5 is: ", day5_temps,)
print("Florida temp on Day 5 is:: ", day5_temps1, "\n")

"""transposes the table and sorts the transposed list alphabetically."""
"""prints the tables each time."""
data = data.transpose()
print(data)
data = data.sort_index()
print(data)